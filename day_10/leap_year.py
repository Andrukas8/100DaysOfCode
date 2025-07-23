def leap_year(year):
    """
    Function that returns True if the year is Leap
    and False if the year is not Leap
    """
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap


print(leap_year(2000))  # leap
print(leap_year(2100))  # not leap
print(leap_year(2400))  # leap
print(leap_year(1989))  # not leap
