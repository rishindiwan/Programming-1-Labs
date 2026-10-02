# ============================================================
# Programming 1: Lab 2 - Operators, Expressions and Conditions
# ============================================================


# ============================================================
# Q1. Write a program to display "10" if the number entered
# by the user is divisible by 5, otherwise print "Bye".
# ============================================================

number = int(input("Enter a number: "))

if number % 5 == 0:
    print("10")
else:
    print("Bye")


# ============================================================
# Q2. If the length of the two parallel sides of a trapezoid
# are X metres and Y metres respectively, and the height is
# H metres, calculate the area of the trapezoid.
# Take X, Y and H as input from the user.
# ============================================================

x = float(input("Enter first parallel side (X): "))
y = float(input("Enter second parallel side (Y): "))
h = float(input("Enter height (H): "))

if x <= 0 or y <= 0 or h <= 0:
    print("Invalid input")
else:
    area = ((x + y) * h) / 2
    print("Area of trapezoid =", area)


# ============================================================
# Q3. Write a program that interprets the Body Mass Index
# (BMI) based on a user's weight and height.
#
# Under 18.5          -> Underweight
# 18.5 to below 25    -> Normal weight
# 25 to below 30      -> Slightly overweight
# 30 to below 35      -> Obese
# 35 and above        -> Clinically obese
#
# BMI = weight / height^2
# Take height and weight from the user.
# ============================================================

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))

if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Slightly overweight")
    elif bmi < 35:
        print("Obese")
    else:
        print("Clinically obese")


# ============================================================
# Q4. Write a Python program to check whether an alphabet
# is a vowel or consonant.
# ============================================================

ch = input("Enter an alphabet: ")

if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# ============================================================
# Q5. Suppose a surface initially contained 2.19 x 10^11
# bacterial cells. After some time, the surface contained
# 4.65 x 10^13 bacterial cells.
#
# Calculate the percentage of bacterial growth.
# Display the answer rounded to the nearest whole number.
# ============================================================

initial = 2.19 * (10 ** 11)
final = 4.65 * (10 ** 13)

growth = ((final - initial) / initial) * 100

print("Percentage of bacterial growth =", round(growth), "%")


# ============================================================
# Q6. Write a program that asks the user to enter a whole
# number of months and then converts that amount of time
# to years and months.
#
# The program should use both integer division and the
# modulus operator.
# ============================================================

months = int(input("Enter number of months: "))

if months < 0:
    print("Invalid input")
else:
    years = months // 12
    remaining_months = months % 12

    print("Years =", years)
    print("Months =", remaining_months)


# ============================================================
# Q7. The color of the beacon light atop Bonneville's
# old John Hancock building forecast the weather:
#
# Steady blue, clear skies
# Flashing blue, cloudy skies
# Steady red, rain ahead
# Flashing red, snow ahead
#
# Write a program that accepts a color (Blue or Red) and
# a mode (Steady or Flashing) as input and displays the
# weather forecast.
# ============================================================

color = input("Enter color (Blue/Red): ").strip().lower()
mode = input("Enter mode (Steady/Flashing): ").strip().lower()

if color == "blue" and mode == "steady":
    print("Clear skies")
elif color == "blue" and mode == "flashing":
    print("Cloudy skies")
elif color == "red" and mode == "steady":
    print("Rain ahead")
elif color == "red" and mode == "flashing":
    print("Snow ahead")
else:
    print("Invalid input")


# ============================================================
# Q8. Write a program that requests the cents and compares
# for a cupcake and displays the message "Break even" if
# the costs and revenues are equal, otherwise displays
# the profit or loss.
# ============================================================

cost = float(input("Enter cost of cupcake: "))
revenue = float(input("Enter revenue of cupcake: "))

if cost < 0 or revenue < 0:
    print("Invalid input")
elif cost == revenue:
    print("Break even")
elif revenue > cost:
    print("Profit =", revenue - cost)
else:
    print("Loss =", cost - revenue)


# ============================================================
# Q9. A store sells widgets at 25 cents each for small orders
# or at 20 cents each for orders of 100 or more.
# Write a program that requests the number of widgets ordered
# and displays the total cost.
# ============================================================

widgets = int(input("Enter number of widgets: "))

if widgets < 0:
    print("Invalid input")
elif widgets >= 100:
    cost = widgets * 0.20
    print("Total cost = $", format(cost, ".2f"))
else:
    cost = widgets * 0.25
    print("Total cost = $", format(cost, ".2f"))


# ============================================================
# Q10. A supermarket sells apples for $2.50 per pound.
# Write a cashier's program that requests the number of pounds
# and the amount of cash tendered as input and displays the
# change from the transaction.
#
# If the cash is not enough, display:
# "You owe $x.xx more."
# ============================================================

pounds = float(input("Enter number of pounds of apples: "))
cash = float(input("Enter cash tendered: "))

if pounds < 0 or cash < 0:
    print("Invalid input")
else:
    total = pounds * 2.50

    if cash >= total:
        change = cash - total
        print("Change = $", format(change, ".2f"))
    else:
        amount_due = total - cash
        print("You owe $", format(amount_due, ".2f"), "more.")


# ============================================================
# Q11. Find the largest of 3 numbers using nested if-else
# conditions.
# ============================================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number =", largest)


# ============================================================
# Q12. Calculate the gross salary of an employee by taking
# basic salary as input.
#
# HRA = 20% of basic salary
# TA  = 5% of basic salary
# DA  = 10% of basic salary
#
# Gross Salary = Basic Salary + HRA + TA + DA
# ============================================================

basic_salary = float(input("Enter basic salary: "))

if basic_salary < 0:
    print("Invalid input")
else:
    hra = 0.20 * basic_salary
    ta = 0.05 * basic_salary
    da = 0.10 * basic_salary

    gross_salary = basic_salary + hra + ta + da

    print("HRA =", hra)
    print("TA =", ta)
    print("DA =", da)
    print("Gross Salary =", gross_salary)


# ============================================================
# Q13. For the above question, find the income tax slab
# in which the employee lies.
#
# Gross Salary       Income Tax
# < Rs. 3 LPA        0%
# Rs. 3,00,000 -
# Rs. 10,00,000      10% of gross salary
# Rs. 10,00,000 -
# Rs. 25,00,000      20% of gross salary
# Above Rs. 25,00,000 30% of gross salary
# ============================================================

gross_salary = float(input("Enter gross salary: "))

if gross_salary < 0:
    print("Invalid input")
elif gross_salary < 300000:
    tax_rate = 0
elif gross_salary <= 1000000:
    tax_rate = 10
elif gross_salary <= 2500000:
    tax_rate = 20
else:
    tax_rate = 30

if gross_salary >= 0:
    income_tax = gross_salary * tax_rate / 100

    print("Income tax rate =", tax_rate, "%")
    print("Income tax =", income_tax)


# ============================================================
# Q14. The flowchart given in the question calculates a
# person's income tax. Write a program corresponding to
# the flowchart.
#
# The flowchart uses:
# Income <= 200000  -> Tax = 0
# Income <= 500000  -> Tax = 10% of the applicable amount
# Income > 500000   -> Tax = 20% of the applicable amount
# ============================================================

income = float(input("Enter income: "))

if income < 0:
    print("Invalid input")
elif income <= 200000:
    tax = 0
elif income <= 500000:
    tax = (income - 200000) * 0.10
else:
    tax = (income - 500000) * 0.20 + (300000 * 0.10)

print("Income tax =", tax)