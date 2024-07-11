from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, '%d/%m/%Y')

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month - 1, 1)).days
    if months < 0:
        years -= 1
        months += 12

    return years, months, days


birth_date = input("Enter your date of birth (dd/mm/yyyy): ")
years, months, days = calculate_age(birth_date)
print(f"Your age is {years} years, {months} months, and {days} days.")

if years >= 60:
    print("You are eligible for a senior citizen discount.")
else:
    print("You are not eligible for a senior citizen discount.")
