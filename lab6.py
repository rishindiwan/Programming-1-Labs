# # # Display multiplication table from 1 to 9

# # print("             Multiplication Table")
# # print("     ", end="")

# # # Print column headings
# # for i in range(1, 10):
# #     print(f"{i:4}", end="")

# # print()
# # print("-" * 42)

# # # Print rows
# # for i in range(1, 10):
# #     print(f"{i:2} |", end="")

# #     for j in range(1, 10):
# #         print(f"{i * j:4}", end="")

# # print()









# # Take a positive number N
# n = int(input("Enter a positive number N: "))

# if n <= 0:
#     print("Invalid input. N must be positive.")
# else:
#     i = 1

#     while i <= 1000:

#         # If i is divisible by N, skip this iteration
#         if i % n == 0:
#             i += 1
#             continue

# # This executes only when i is NOT divisible by N
# print(i, end=" ")

# i += 1











# # Take number of lines
# n = int(input("Enter N: "))

# if n <= 0:
#     print("Invalid input. N must be positive.")
# else:
#     i = 1

#     while i <= n:
#         j = 1

#         while j <= i:
#             print("*", end=" ")
#             j += 1

# print()
# i += 1













# Take number of lines
n = int(input("Enter N: "))

if n <= 0:
    print("Invalid input. N must be positive.")
else:
    i = 1

    while i <= n:

        # Print spaces before stars
        space = 1
        while space <= n - i:
            print("  ", end="")
            space += 1

        # Print stars
        j = 1
        while j <= i:
            print("* ", end="")
            j += 1

print()
i += 1











# # Take number of lines
# n = int(input("Enter N: "))

# if n <= 0:
#     print("Invalid input. N must be positive.")
# else:
#     i = 1

#     while i <= n:

#         # Print spaces before stars
#         space = 1
#         while space <= n - i:
#             print("  ", end="")
#             space += 1

#         # Number of stars = 2*i + 1
#         j = 1
#         while j <= 2 * i + 1:
#             print("* ", end="")
#             j += 1

# print()
# i += 1











# # Take a positive integer
# n = int(input("Enter a positive integer: "))

# if n < 0:
#     print("Invalid input. Number must be positive.")
# else:
#     original = n

#     if n == 0:
#         binary = "0"

#     else:
#         binary = ""

#         while n > 0:
#             remainder = n % 2
#             binary = str(remainder) + binary
#             n = n // 2

#     print("Binary equivalent:", binary)

#     # Check our answer against Python's built-in bin()
#     built_in = bin(original)[2:]

# if binary == built_in:
#     print("Result matches bin()")
# else:
#     print("Result does not match bin()")












# # Take the number of values
# n = int(input("How many numbers? "))

# if n <= 0:
#     print("Invalid input. N must be positive.")

# else:
#     first = int(input("Enter number 1: "))

#     if first <= 0:
#         print("Invalid input. Numbers must be positive.")

#     else:
#         lcm = first
#         valid = True

#         i = 2

#         while i <= n:

#             num = int(input(f"Enter number {i}: "))

#             if num <= 0:
#                 print("Invalid input. Numbers must be positive.")
#                 valid = False
#                 break

#             # Find GCD of current LCM and new number
#             a = lcm
#             b = num

#             while b != 0:
#                 remainder = a % b
#                 a = b
#                 b = remainder

#             gcd = a

#             # LCM = (a * b) / GCD
#             lcm = (lcm * num) // gcd

#             i += 1

# if valid:
#     print("LCM =", lcm)








# # Take the number of values
# n = int(input("How many numbers? "))

# if n <= 0:
#     print("Invalid input. N must be positive.")

# else:
#     first = int(input("Enter number 1: "))

#     if first <= 0:
#         print("Invalid input. Numbers must be positive.")

#     else:
#         gcd = first
#         valid = True

#         i = 2

#         while i <= n:

#             num = int(input(f"Enter number {i}: "))

#             if num <= 0:
#                 print("Invalid input. Numbers must be positive.")
#                 valid = False
#                 break

#             # Euclidean algorithm
#             a = gcd
#             b = num

#             while b != 0:
#                 remainder = a % b
#                 a = b
#                 b = remainder

#             gcd = a

#             i += 1

# if valid:
#         print("GCD =", gcd)





# import math

# print("Degree\tSin\tCos")

# degree = 0

# while degree <= 360:

#     # Convert degree to radians
#     radians = degree * math.pi / 180

#     sine = math.sin(radians)
#     cosine = math.cos(radians)

#     # Display four digits after decimal point
# print(f"{degree}\t{sine:.4f}\t{cosine:.4f}")

# degree += 10












# # Take number of lines
# n = int(input("Enter N: "))

# if n <= 0:
#     print("Invalid input. N must be positive.")

# else:
#     # Outer loop controls the rows
#     for i in range(1, n + 1):

#         # Inner loop controls the stars in each row
#         for j in range(1, i + 1):
#             print("*", end=" ")

# print()