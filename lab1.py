# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))

# area = length * breadth
# print(area)









# side = int(input("enter the side of square in feet "))

# area = (0.305*(side * side))
# print("Area of sqaure: ", area)










# Take input for x and y
x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))

# Check for negative integers
if x < 0 or y < 0:
    print("Invalid input")
# Check if x is 0 to avoid division by zero error
elif x == 0:
    print("Division by zero is not allowed")
# Check divisibility using the modulo operator
elif y % x == 0:
    print(f"{y} is divisible by {x}")
else:
    print(f"{y} is not divisible by {x}")






