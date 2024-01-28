import datetime
def find_day_of_week(month, day, year):

    date_obj = datetime.date(year, month, day)

    day_of_week_int = date_obj.weekday()

    days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    day_of_week = days_of_week[day_of_week_int]

    return day_of_week