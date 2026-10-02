# ============================================================
# Programming 1: Lab 1 - Basic Syntax and Example Programs
# ============================================================


# ============================================================
# Q1. Input the length and width (in metres) of a plot
# and calculate its area.
# ============================================================

length = float(input("Enter length in metres: "))
width = float(input("Enter width in metres: "))

if length <= 0 or width <= 0:
    print("Invalid input")
else:
    area = length * width
    print("Area of the plot =", area, "square metres")


# ============================================================
# Q2. Modify the above question to take input in feet
# and calculate the area in square metres.
# ============================================================

length = float(input("Enter length in feet: "))
width = float(input("Enter width in feet: "))

if length <= 0 or width <= 0:
    print("Invalid input")
else:
    # Convert feet to metres
    length_m = length * 0.3048
    width_m = width * 0.3048

    area = length_m * width_m

    print("Area of the plot =", area, "square metres")


# ============================================================
# Q3. Take 2 integers x and y as input and find whether
# y is divisible by x or not. For negative integers,
# display "Invalid input".
# ============================================================

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x < 0 or y < 0:
    print("Invalid input")
elif x == 0:
    print("Invalid input")
elif y % x == 0:
    print(y, "is divisible by", x)
else:
    print(y, "is not divisible by", x)


# ============================================================
# Q4. Take an integer as input and check whether it is
# even or odd.
# ============================================================

n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# ============================================================
# Q5. Find the area of a Circle of radius r.
# Only radius between 1 and 100 should be accepted.
# ============================================================

import math

r = float(input("Enter radius: "))

if r < 1 or r > 100:
    print("Invalid input")
else:
    area = math.pi * r ** 2
    print("Area of the circle =", area)


# ============================================================
# Q6. Take a value of temperature as input (in Celsius)
# and convert it into Fahrenheit. Also display the
# equivalent temperature in Kelvin.
# ============================================================

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Temperature in Fahrenheit =", fahrenheit)
print("Temperature in Kelvin =", kelvin)


# ============================================================
# Q7. Using the temperature conversion formula, calculate
# the value at which the Celsius and corresponding
# Fahrenheit values are the same.
# ============================================================

# Formula:
# Fahrenheit = (Celsius * 9 / 5) + 32

# When Celsius = Fahrenheit:
# C = (C * 9 / 5) + 32
# C = -40

celsius = -40
fahrenheit = (celsius * 9 / 5) + 32

print("Celsius =", celsius)
print("Fahrenheit =", fahrenheit)


# ============================================================
# Q8. Take the value of year as input and find whether
# it is a leap year or not. Consider all valid and
# invalid inputs.
# ============================================================

year = int(input("Enter year: "))

if year <= 0:
    print("Invalid input")
elif year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# ============================================================
# Q9. A bank calculates interest on RD accounts at 7.1% p.a.
# Calculate the return for a given duration and monthly
# installment amount.
#
# Monthly installment must not be less than Rs. 500
# and duration should be at least 6 months.
# Check for valid and invalid inputs.
# ============================================================

monthly = float(input("Enter monthly installment: "))
months = int(input("Enter duration in months: "))

rate = 7.1

if monthly < 500:
    print("Invalid input: Monthly installment must be at least Rs. 500")
elif months < 6:
    print("Invalid input: Duration must be at least 6 months")
else:
    total_deposit = monthly * months

    interest = (monthly * months * (months + 1) * rate) / (2 * 12 * 100)

    maturity_amount = total_deposit + interest

    print("Total deposit =", total_deposit)
    print("Interest =", interest)
    print("Maturity amount =", maturity_amount)


# ============================================================
# Q10. A day has 86,400 seconds. Given a number in the
# range 1 to 86,400, output the current time as hours,
# minutes and seconds with a 24-hour clock.
#
# Example:
# 70,000 seconds = 19 hours, 26 minutes, 40 seconds
# ============================================================

seconds = int(input("Enter number of seconds: "))

if seconds < 1 or seconds > 86400:
    print("Invalid input")
else:
    hours = seconds // 3600

    remaining = seconds % 3600

    minutes = remaining // 60

    secs = remaining % 60

    # 86400 seconds represents 24:00:00,
    # which is displayed as 00:00:00 on a 24-hour clock.
    if hours == 24:
        hours = 0

    print("Time =", hours, "hours,", minutes, "minutes,", secs, "seconds")