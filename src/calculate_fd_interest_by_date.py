import src.common.date_operations

class Interest:
    def __init__(self) -> None:
        self.year_operations = src.common.date_operations.Year()

    def _take_inputs_by_date(self):
        self.principle = int(input("Principle Amount: "))
        self.start_date = input("Enter start date in dd-mm-yyyy format: ")
        self.end_date = input("Enter end date in dd-mm-yyyy format: ")
        self.rate = float(input("Interest Rate: "))
        self.compounding = int(input("Enter the compounding rate n: "))

    def _take_inputs_by_days(self):
        self.principle = int(input("Principle Amount: "))
        self.days = int(input("Enter number of days: "))
        self.rate = float(input("Interest Rate: "))
        self.compounding = int(input("Enter the compounding rate n: "))

    def _calculate_amount(self, years):
        exp = self.compounding * years
        coeff = (1 + (self.rate / (self.compounding * 100)))
        multiple = coeff ** exp
        self.amount = round(self.principle * multiple)
        return self.amount

    def calculate_amount_by_date(self):
        self._take_inputs_by_date()
        years = self.year_operations.calculate_year_by_date(self.start_date, self.end_date)
        amount = self._calculate_amount(years)
        print(f"Maturity Amount: {amount}")

    def calculate_amount_by_days(self):
        self._take_inputs_by_days()
        years = self.year_operations.calculate_year_by_days(self.days)
        amount = self._calculate_amount(years)
        print(f"Maturity Amount: {amount}") 
