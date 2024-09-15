#11. Write a program to find Number of days in a given month of a given year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if month == 2 and is_leap_year(year):
        return 29
    
    return month_days.get(month, "Invalid month")

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

days = days_in_month(month, year)
if isinstance(days, int):
    print(f"Number of days in month {month}, year {year}: {days}")
else:
    print(days)
