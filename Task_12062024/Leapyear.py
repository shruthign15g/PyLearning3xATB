# Write a program to find a leap year

# Divisible by 400
# Divisible by 100 but not by 400
# Divisible by 4 but not by 100
# Not divisible by 4
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

