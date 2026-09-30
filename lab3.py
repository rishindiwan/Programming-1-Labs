# import math 

# x1 = float(input("Enter x1: "))
# x2 = float(input("Enter x2: "))
# x3 = float(input("Enter x3: "))
# y1 = float(input("Enter y1: "))
# y2 = float(input("Enter y2: "))
# y3 = float(input("Enter y3: "))


# side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
# side3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

# s = (side1 + side2 + side3) / 2

# area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
# print("Area of the triangle:", area)







# import math

# s = float(input("Enter the side of the hexagon: "))

# area = (3 * math.sqrt(3) / 2) * s ** 2

# print("Area of the hexagon:", area)







# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a <=0 or b<=0 or c<=0:
#     print("Invalid sides")
# elif a+b >c and b+c > a and a+c > b:
#     print("Triangle can be formed ")
# else:
#     print("Invalid")










# n = int(input("Enter a 3-digit number: "))

# if n >= 100 and n <= 999:
#     digit1 = n // 100
#     digit2 = (n // 10) % 10
#     digit3 = n % 10

#     total = digit1 + digit2 + digit3

#     print("Sum of digits:", total)

#     if total % 3 == 0:
#         print("The sum is divisible by 3")
#     else:
#         print("The sum is not divisible by 3")
# else:
#     print("Invalid input. Please enter a 3-digit number.")







# n = int(input("Enter a 5-digit number: "))

# if n < 10000 or n > 99999:
#     print("Invalid input. Please enter a 5-digit number.")

# else:
#     original = n
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     print("Reverse:", reverse)

#     if original == reverse:
#         print("Number is Palindrome")
#     else:
#         print("Number is not Palindrome")






# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a = a + b
# b = a - b
# a = a - b

# print("After swapping:")
# print("a =", a)
# print("b =", b)






# n = int(input("Enter a 3-digit number: "))

# if n < 100 or n > 999:
#     print("Invalid input. Please enter a 3-digit number.")

# else:
#     original = n
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total = total + digit ** 3
#         n = n // 10

#     if total == original:
#         print("Armstrong number")
#     else:
#         print("Not an Armstrong number")







# saving = float(input("Enter monthly saving amount: "))
# months = int(input("Enter number of months: "))

# if saving <= 0:
#     print("Invalid saving amount")

# elif months <= 0:
#     print("Invalid number of months")

# else:
#     annual_rate = 0.05
#     monthly_rate = annual_rate / 12

#     account_value = saving * ((1 + monthly_rate) ** months - 1) / monthly_rate

#     print("Account value:", account_value)







# import math

# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# if a == 0:
#     print("Not a quadratic equation")

# else:
#     d = b ** 2 - 4 * a * c

#     if d < 0:
#         print("No real solutions")

#     elif d == 0:
#         x = -b / (2 * a)
#         print(f"Solution: {x:.2f}")

#     else:
#         x1 = (-b + math.sqrt(d)) / (2 * a)
#         x2 = (-b - math.sqrt(d)) / (2 * a)

#         print(f"Solution 1: {x1:.2f}")
#         print(f"Solution 2: {x2:.2f}")

