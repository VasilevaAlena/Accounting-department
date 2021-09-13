from application import salary
from db import people
from datetime import datetime


if __name__ == '__main__':
    now = datetime.now()
    print(now)
    salary.calculate_salary()
    people.get_employees()
 


