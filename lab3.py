# ============================================================
# Programming 1: Lab 3 - Operators, Expressions and Conditions
# ============================================================


# ============================================================
# Q1. Enter the three points (x1, y1), (x2, y2), and (x3, y3)
# of a triangle and display its area.
#
# Formula:
# side1 = distance between point 1 and point 2
# side2 = distance between point 2 and point 3
# side3 = distance between point 3 and point 1
#
# s = (side1 + side2 + side3) / 2
#
# Area = sqrt(s(s-side1)(s-side2)(s-side3))
# ============================================================

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

if side1 == 0 or side2 == 0 or side3 == 0:
    print("Invalid triangle")
elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid triangle")
else:
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    print("Area of triangle =", area)


# ============================================================
# Q2. Enter the side of a hexagon and display its area.
#
# Formula:
# Area = (3 * sqrt(3) / 2) * s^2
#
# where s is the length of a side.
# ============================================================

s = float(input("Enter side of hexagon: "))

if s <= 0:
    print("Invalid input")
else:
    area = (3 * math.sqrt(3) / 2) * s ** 2

    print("Area of hexagon =", area)


# ============================================================
# Q3. Take 3 numbers as input and find whether they form
# the sides of a triangle or not.
# Consider invalid cases also.
# ============================================================

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input")
elif a + b > c and a + c > b and b + c > a:
    print("The numbers form a triangle")
else:
    print("The numbers do not form a triangle")


# ============================================================
# Q4. Take a 3-digit number as input and find the sum
# of its digits. Also check if the sum is divisible by 3.
# ============================================================

n = int(input("Enter a 3-digit number: "))

if n < 100 or n > 999:
    print("Invalid input")
else:
    digit1 = n // 100
    digit2 = (n // 10) % 10
    digit3 = n % 10

    total = digit1 + digit2 + digit3

    print("Sum of digits =", total)

    if total % 3 == 0:
        print("The sum is divisible by 3")
    else:
        print("The sum is not divisible by 3")


# ============================================================
# Q5. Take a 5-digit number as input and print the reverse
# of the number. Do not use any built-in reversing functions.
# Check whether the input number and reversed number are
# the same.
# ============================================================

n = int(input("Enter a 5-digit number: "))

if n < 10000 or n > 99999:
    print("Invalid input")
else:
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    print("Reverse =", reverse)

    if original == reverse:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")


# ============================================================
# Q6. Swap the values of two integer variables without using
# a third variable or multiple assignment operation.
# ============================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)


# ============================================================
# Q7. Take a 3-digit number as input. Check if it is an
# Armstrong number or not.
#
# Example:
# 1^3 + 5^3 + 3^3 = 153
# ============================================================

n = int(input("Enter a 3-digit number: "))

if n < 100 or n > 999:
    print("Invalid input")
else:
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    if original == total:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


# ============================================================
# Q8. Suppose you save a fixed amount every month into a
# savings account with an annual interest rate of 5%.
#
# Monthly interest rate = 0.05 / 12 = 0.00417
#
# After each month:
# balance = (balance + monthly saving) * (1 + monthly rate)
#
# Write a program that takes monthly saving amount and
# number of months (N) and displays the account value
# after the Nth month.
#
# Check valid and invalid cases.
# Do not use loops.
# ============================================================

saving = float(input("Enter monthly saving amount: "))
months = int(input("Enter number of months: "))

if saving <= 0 or months <= 0:
    print("Invalid input")
else:
    rate = 0.05 / 12

    # Formula for the account value after N months
    balance = saving * (((1 + rate) ** months - 1) / rate) * (1 + rate)

    print("Account value =", round(balance, 3))


# ============================================================
# Q9. Enter the coefficients of a quadratic equation and
# display its solutions.
#
# Equation:
# ax^2 + bx + c = 0
#
# Handle all invalid cases and display solutions to exactly
# 2 decimal places.
#
# Complex solutions need not be calculated.
# ============================================================

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Invalid input: This is not a quadratic equation")
else:
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)

        print("Root 1 =", format(root1, ".2f"))
        print("Root 2 =", format(root2, ".2f"))

    elif discriminant == 0:
        root = -b / (2 * a)

        print("Both roots are equal")
        print("Root =", format(root, ".2f"))

    else:
        print("No real solutions")
        print("Complex solutions are not calculated.")