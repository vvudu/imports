from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def print_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print_current_date()