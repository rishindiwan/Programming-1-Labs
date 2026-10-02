# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))

# area = length * breadth
# print(area)









# side = int(input("enter the side of square in feet "))

# area = (0.305*(side * side))
# print("Area of sqaure: ", area)











# x = int(input("Enter integer x: "))
# y = int(input("Enter integer y: "))

# if x < 0 or y < 0:
#     print("Invalid input")
# elif x == 0:
#     print("Division by zero is not allowed")
# # Check divisibility using the modulo operator
# elif y % x == 0:
#     print(f"{y} is divisible by {x}")
# else:
#     print(f"{y} is not divisible by {x}")













# n = int(input("Enter the number: "))

# if n%2==0 :
#     print("Even number")
# else:
#     print("Odd number")







# import math

# r = int(input("Enter the radius: "))

# if 0<=r<=100:
#     area = math.pi * r*r
#     print(area)
# else:
#     print("Invalid number")








# temp = float(input("Enter the temp in celsius: "))

# kelvin = temp + 273
# farh = (temp * 9/5) + 32

# print(f"Temp in Farheniet: {farh} f")
# print(f"Temp in kelvin: {kelvin} k")










# celsius = 32 / (1 - 9/5)

# print("Celsius and Fahrenheit are equal at:", celsius)










# y = int(input("Enter the year: "))

# if y % 4 ==0 :
#     print(f"Year {y} is a leap year")
# else:
#     print(f"Year {y} is not a leap year")









# amount = int(input("Enter monthly installment: "))
# months = int(input("Enter duration in months: "))

# if amount < 500:
#     print("Invalid monthly installment")
# elif months < 6:
#     print("Invalid duration")
# else:
#     # ==========================================
#     # ADD THIS LOGIC TO CALCULATE RECURRING DEPOSIT RETURNS
#     # ==========================================
#     rate_pa = 7.1  # Bank Interest Rate: 7.1%
    
#     # Standard IBA Quarterly Compounding Formula
#     # n = number of quarters the installment remains in the bank
#     total_invested = amount * months
#     maturity_amount = 0.0
    
#     for i in range(1, months + 1):
#         months_left = months - i + 1
#         # Convert remaining months into fractional quarters
#         quarters_left = months_left / 3.0
#         # Formula: Principal * (1 + R/400) ^ quarters
#         maturity_amount += amount * ((1 + rate_pa / 400) ** quarters_left)
        
#     interest_earned = maturity_amount - total_invested
    
#     # Displaying the results to the user
#     print("\n--- RD Calculation Summary ---")
#     print(f"Total Amount Invested: Rs. {total_invested:,.2f}")
#     print(f"Interest Money Earned: Rs. {interest_earned:,.2f}")
#     print(f"Final Maturity Value : Rs. {maturity_amount:,.2f}")
#     # ==========================================

















# # 1. Take input from the user
# total_seconds = int(input("Enter seconds (1 to 86400): "))

# # 2. Validate the input range
# if total_seconds < 1 or total_seconds > 86400:
#     print("Invalid input! Please enter a number between 1 and 86,400.")
# else:
#     # 3. Calculate hours, minutes, and remaining seconds
#     hours = total_seconds // 3600
#     remaining_seconds = total_seconds % 3600
#     minutes = remaining_seconds // 60
#     seconds = remaining_seconds % 60

#     # 4. Output the result in 24-hour format
#     print(f"{total_seconds:,} sec is {hours} hours, {minutes} minutes, and {seconds} seconds.")
