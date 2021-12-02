from application import salary
from application.db import people
import datetime

print(datetime.date.today())
if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()