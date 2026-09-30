# x = int(input("Enter the number: "))

# if x % 5 == 0:
#     print("Hi! ")
# else:
#     print("Bye! ")





# X = int(input("Enter the legth of first side: "))
# Y = int (input("Enter the legth of second side: "))
# H = int(input("Enter the height of teh figure: "))

# if X == Y:
#     area = ((X + Y) / 2) * H 
#     print(area)

# else: 
#     print("Invalid values")








# W = float(input("Enter the weight in kg: "))
# H = float(input("Enter the height in meters: "))

# if W > 0 and H > 0:
#     x = W / (H ** 2)
#     print("Your BMI is:", x)
    
#     if x < 18.5:
#         print("Underweight")
#     elif 18.5 <= x < 25:
#         print("Normal weight")
#     elif 25 <= x < 30:
#         print("Slightly overweight")
#     elif 30 <= x <= 35:
#         print("Obese")
#     elif x > 35:
#         print("Clinically obese")
# else:
#     print("Invalid values")






# character = input("Enter an alphabet: ")

# if character.isalpha():
#     if character in "aeiouAEIOU":
#         print("It is a vowel")
#     else:
#         print("It is a consonant")
# else:
#     print("Invalid input! Please enter a letter.")






# initial_cells = 2.19e14
# final_cells = 4.68e14

# growth_percentage = ((final_cells - initial_cells) / initial_cells) * 100

# print(round(growth_percentage))









# # Get user input
# total_months = int(input("Enter a whole number of months: "))

# # Calculate years and remaining months
# years = total_months // 12
# months = total_months % 12

# # Display results
# print(f"{total_months} months is equal to {years} years and {months} months.")





# # Get user inputs
# color = input("Enter a color (Blue or Red): ").strip().capitalize()
# mode = input("Enter a mode (Steady or Flashing): ").strip().capitalize()

# # Determine and display forecast
# if color == "Blue" and mode == "Steady":
#     print("Forecast: Clear view.")
# elif color == "Blue" and mode == "Flashing":
#     print("Forecast: Clouds due.")
# elif color == "Red" and mode == "Steady":
#     print("Forecast: Rain ahead.")
# elif color == "Red" and mode == "Flashing":
#     print("Forecast: Snow instead.")
# else:
#     print("Invalid color or mode entered.")







# cost = float(input("Enter total costs: "))
# revenue = float(input("Enter total revenue: "))

# # Conditional evaluation
# if revenue == cost:
#     print("Break even")
# elif revenue > cost:
#     profit = revenue - cost
#     print(f"Profit: ${profit:.2f}")
# else:
#     loss = cost - revenue
#     print(f"Loss: ${loss:.2f}")






# # Input order quantity
# widgets = int(input("Enter the number of widgets ordered: "))

# # Bulk discount evaluation
# if widgets < 100:
#     price_per_widget = 0.25
# else:
#     price_per_widget = 0.20

# # Final cost calculation
# total_cost = widgets * price_per_widget
# print(f"Total cost: ${total_cost:.2f}")






# Store constants
PRICE_PER_POUND = 2.50

# Input transactional values
pounds = float(input("Enter the number of pounds of apples: "))
cash_tendered = float(input("Enter the amount of cash tendered: "))

# Calculate financial requirements
total_cost = pounds * PRICE_PER_POUND

# Determine checkout output
if cash_tendered >= total_cost:
    change = cash_tendered - total_cost
    print(f"Change: ${change:.2f}")
else:
    amount_owed = total_cost - cash_tendered
    print(f"You owe ${amount_owed:.2f} more.")
 