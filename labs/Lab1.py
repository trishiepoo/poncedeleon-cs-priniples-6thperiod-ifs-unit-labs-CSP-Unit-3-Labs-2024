# Name:
# Period:
# Date:
    
# define a function isLeapYear() that takes a given year as
# a parameter and returns true if the given year is a leap
# year and false if the given year is not a leap year.

def leapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


