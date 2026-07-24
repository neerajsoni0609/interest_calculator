import sys

from src.calculate_interest_rate import Rate
from src.calculate_fd_interest_by_date import Interest
from src.calculate_bank_fd_interest_report import generate_daily_balance_report

def execute_operation():
    options = '''Please select the appropriate option:
1. Calculate Interest rate by providing dates
2. Calculate Interest rate by providing days
3. Calculate Maturity amount by providing dates
4. Calculate Maturity amount by providing days
5. Generate daily interest rate report
6. Exit
Please enter the option: '''

    option = int(input(options))
    match option:
        case 1:
            Rate().calculate_rate_by_date()

        case 2:
            Rate().calculate_rate_by_days()

        case 3:
            Interest().calculate_amount_by_date()

        case 4:
            Interest().calculate_amount_by_days()

        case 5:
            generate_daily_balance_report()

        case 6:
            sys.exit(0)

        case _:
            print("Incorrect option selected, exiting")
            sys.exit(1)

if __name__ == "__main__":
    execute_operation()