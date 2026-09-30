# salary = int(input("Enter your salary: "))
# time = int(input("Enter the time of your service: "))

# if time>=5:
#     print((0.05 * salary) + salary)
# elif  0 <= time <= 5:
#     print("Not eligible for hike")
# else:
#     print("Inavlid")






# password = input("Enter your password: ")

# if password == "s3cr3t!P@ssw0rd":
#     print("Welcome, to the world!")
# else:
#     print("Invalid Password")






# import math

# shape = input("Ask user the shape: ")

# if shape == "square":
#     x = float(input(" the length of its side: "))
#     area = x * x
#     print(f"{area:.3f}")
    
# elif shape == "rectangle":
#     a = float(input(" the length of its first side: "))
#     b = float(input(" the length of its second side: "))
#     area = a * b
#     print(f"{area:.3f}")
    
# elif shape == "circle":
#     r = float(input("the radius of circle: "))
#     area = math.pi * (r ** 2)
#     print(f"{area:.3f}")
    
# elif shape == "triangle":
#     z = float(input("the base of triangle: "))
#     y = float(input("the altitude of triangle: "))
#     area = 0.5 * z * y
#     print(f"{area:.3f}")
    
# else:
#     print("Invalid Shape")







# hours = int(input("Enter hours (0-23): "))
# minutes = int(input("Enter minutes (0-59): "))

# minutes += 15

# extra_hours = minutes // 60
# minutes = minutes % 60

# hours = (hours + extra_hours) % 24

# print(f"{hours}:{minutes:02d}")







# n = float(input("Enter kilometers: "))
# period = input("Enter period (day/night): ")

# # Calculate initial taxi price
# if period == "day":
#     cheapest = 33.58 + n * 37.89
# else:
#     cheapest = 33.58 + n * 43.17

# # Update if bus is available and cheaper
# if n >= 20:
#     cheapest = min(cheapest, n * 4.32)

# # Update if train is available and cheaper
# if n >= 100:
#     cheapest = min(cheapest, n * 2.88)

# print(f"Cheapest price: {cheapest:.2f} INR")







# holidays = int(input())
# workdays = 365 - holidays

# total_play_minutes = (workdays * 63) + (holidays * 127)
# norm = 30000
# difference = abs(total_play_minutes - norm)

# hours = difference // 60
# minutes = difference % 60

# if total_play_minutes <= norm:
#   print("Tom sleeps well")
#   print(f"{hours} hours and {minutes} minutes less for play")
# else:
#   print("Tom will run away")
#   print(f"{hours} hours and {minutes} minutes more for play")








# budget = float(input())
# season = input().lower()

# destination = ""
# accommodation = ""
# spend_percentage = 0.0

# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         accommodation = "Camp"
#         spend_percentage = 0.30
#     else:
#         accommodation = "Hotel"
#         spend_percentage = 0.70

# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         accommodation = "Camp"
#         spend_percentage = 0.40
#     else:
#         accommodation = "Hotel"
#         spend_percentage = 0.80

# else:
#     destination = "Europe"
#     accommodation = "Hotel"
#     spend_percentage = 0.90

# amount_spent = budget * spend_percentage

# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {amount_spent:.2f}")








# for num in range(1, 1001):
#     if num % 10 == 6:
#         print(num)







# n = int(input())
# total_sum = 0

# for _ in range(n):
#     num = int(input())
#     total_sum += num

# print(total_sum)










# N = int(input())

# for i in range(1, 21):
#     result = N * i
#     print(f"{N} x {i} = {result}")
