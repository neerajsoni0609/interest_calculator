from datetime import datetime, timedelta
import csv
from decimal import Decimal, getcontext

# increase precision for financial calculations
getcontext().prec = 28

class FDCompoundingSimulator:
    def __init__(self, principal, nominal_rate_percent, fd_start_str, fd_end_str,
                 day_count_base=365, include_start=False):
        """
        Initialize the FD simulator with principal, rate, and date range.
        """
        if principal < 0:
            raise ValueError("Principal must be non-negative")

        try:
            self.fd_start = datetime.strptime(fd_start_str, "%d-%m-%Y")
            self.fd_end = datetime.strptime(fd_end_str, "%d-%m-%Y")
        except ValueError as e:
            raise ValueError("Dates must be in dd-mm-yyyy format") from e

        self.principal = Decimal(principal)
        self.nominal_rate_percent = Decimal(nominal_rate_percent)
        self.day_count_base = day_count_base
        self.include_start = include_start

        # Precompute daily rate
        self.r_daily = self._convert_quarterly_to_daily_rate()

        # Storage for results
        self.daily_report = []
        self.summary = {}

    def _convert_quarterly_to_daily_rate(self):
        """
        Convert nominal APR (compounded quarterly) to effective daily rate.
        """
        r_nominal = self.nominal_rate_percent / Decimal(100)
        ear = (Decimal(1) + r_nominal / Decimal(4)) ** Decimal(4) - Decimal(1)
        r_daily = (Decimal(1) + ear) ** (Decimal(1) / Decimal(self.day_count_base)) - Decimal(1)
        return r_daily

    def simulate(self):
        """
        Run the daily compounding simulation.
        """
        balance = self.principal
        current_date = self.fd_start if self.include_start else self.fd_start + timedelta(days=1)

        if current_date > self.fd_end:
            self.summary = {
                "final_balance": balance,
                "total_interest": Decimal(0)
            }
            return self.daily_report, self.summary

        while current_date <= self.fd_end:
            interest_today = balance * self.r_daily
            balance += interest_today
            self.daily_report.append({
                "date": current_date.strftime("%d-%m-%Y"),
                "interest_today": float(interest_today.quantize(Decimal('0.01'))),
                "balance": float(balance.quantize(Decimal('0.01')))
            })
            current_date += timedelta(days=1)

        self.summary = {
            "final_balance": balance.quantize(Decimal('0.01')),
            "total_interest": (balance - self.principal).quantize(Decimal('0.01'))
        }
        return self.daily_report, self.summary

    def export_to_csv(self, filename="daily_balance_report.csv"):
        """
        Export the daily report to a CSV file.
        """
        if not self.daily_report:
            print("No data to export.")
            return
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "interest_today", "balance"])
            writer.writeheader()
            writer.writerows(self.daily_report)
        print(f"Report exported to {filename}")

    def print_summary(self):
        """
        Print the summary of final balance and total interest.
        """
        final_balance = float(self.summary["final_balance"])
        interest = float(self.summary["total_interest"])
        print("\nSummary:")
        print(f"Final balance = ₹{final_balance:,.2f}")
        print(f"Total interest = ₹{interest:,.2f}")


def generate_daily_balance_report():
    principal = float(input("Enter the principal amount (₹): "))
    nominal_rate = float(input("Enter the nominal rate (%): "))
    fd_start = input("Enter the FD start date (dd-mm-yyyy): ")
    fd_end = input("Enter the FD end date (dd-mm-yyyy): ")

    simulator = FDCompoundingSimulator(principal, nominal_rate, fd_start, fd_end)
    daily_report, summary = simulator.simulate()

    if daily_report:
        simulator.export_to_csv()
    else:
        print("No compounding days in the given range (fd_end <= fd_start).")

    simulator.print_summary()
