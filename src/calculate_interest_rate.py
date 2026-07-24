import src.common.date_operations

class Rate:
    def __init__(self) -> None:
        self.year_operations = src.common.date_operations.Year()

    def _take_inputs_by_date(self):
        self.principle = int(input("Principle Amount: "))
        self.start_date = input("Enter start date in dd-mm-yyyy format: ")
        self.end_date = input("Enter end date in dd-mm-yyyy format: ")
        self.compounding_rate = int(input("Enter the compounding rate n: "))
        self.amount = float(input("Maturity Amount: "))

    def _take_inputs_by_days(self):
        self.principle = int(input("Principle Amount: "))
        self.days = int(input("Enter number of days: "))
        self.compounding_rate = int(input("Enter the compounding rate n: "))
        self.amount = float(input("Maturity Amount: "))

    def _calculate_rate(self, years):
        exp = 1 / (self.compounding_rate * years)
        coeff = ((self.amount / self.principle) ** exp) -1
        self.rate = round(coeff * 100 * self.compounding_rate, 4)
        return self.rate
    
    def calculate_rate_by_date(self):
        self._take_inputs_by_date()
        years = self.year_operations.calculate_year_by_date(self.start_date, self.end_date)
        interest_rate = self._calculate_rate(years)
        print(f"Interest rate is: {interest_rate} %")

    def calculate_rate_by_days(self):
        self._take_inputs_by_days()
        years = self.year_operations.calculate_year_by_days(self.days)
        interest_rate = self._calculate_rate(years)
        print(f"Interest rate is: {interest_rate} %")