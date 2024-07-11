from datetime import datetime


def find_day(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    day_of_week = date_obj.strftime("%A")
    return day_of_week


# Example usage
date = input("Enter a date in YYYY-MM-DD format: ")
day = find_day(date)
print(f"The day on {date} is {day}.")
