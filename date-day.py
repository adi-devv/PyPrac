import datetime


def find_day(date):
    # Create a datetime object from the input date
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')

    # Get the day of the week
    day_of_week = date_obj.strftime("%A")

    return day_of_week


# Example usage
date = input("Enter a date in YYYY-MM-DD format: ")
day = find_day(date)
print(f"The day on {date} is {day}.")
