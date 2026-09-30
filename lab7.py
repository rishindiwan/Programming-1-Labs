n = int(input("What's n: "))

sum = 0 
for i in range (1 , n + 1):
    sum = sum + 1 / i

print("Sum , {sum:.9f}")







n = int(input("Enter N: "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + 1 / fact

print(f"Sum = {sum:.9f}")










n = int(input("Enter N: "))

sum = 0

for i in range(1, n + 1):

    if i % 2 == 0:
        sum = sum - 1 / (i ** 2)
    else:
        sum = sum + 1 / (i ** 2)

print(f"Sum = {sum:.9f}")













n = int(input("Enter N: "))
x = float(input("Enter x: "))

sum = 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (x ** i) / fact

print(f"Sum = {sum:.9f}")














n = int(input("Enter N: "))
x = float(input("Enter x: "))

sum = 1

for i in range(1, n):
    sum = sum + (x ** i) / i

print(f"Sum = {sum:.9f}")











x = float(input("Enter x: "))
e = float(input("Enter error: "))

sum = 0
n = 1

while True:
    term = (1 / 2) ** n
    sum = sum + term

    if term < e:
        break

    n = n + 1

print("Sum =", sum)
print("Number of terms =", n)













e = float(input("Enter error: "))

sum = 0
n = 1

while True:
    term = (1 / 2) ** n
    sum = sum + term

    if term < e:
        break

    n = n + 1

print("Sum =", sum)
print("Number of terms =", n)














x = float(input("Enter x: "))
e = float(input("Enter error: "))

sum = 0
n = 1

while True:

    power = 2 * n - 1

    fact = 1
    for i in range(1, power + 1):
        fact = fact * i

    term = (x ** power) / fact

    if n % 2 == 0:
        term = -term

    sum = sum + term

    if abs(term) < e:
        break

    n = n + 1

print("F(x) =", sum)
print("Number of terms =", n)












x = float(input("Enter x: "))
e = float(input("Enter error: "))

sum = 1
n = 1

while True:

    power = 2 * n

    fact = 1
    for i in range(1, power + 1):
        fact = fact * i

    term = (x ** power) / fact

    if n % 2 == 1:
        term = -term

    sum = sum + term

    if abs(term) < e:
        break

    n = n + 1

print("F(x) =", sum)
print("Number of terms =", n + 1)
















