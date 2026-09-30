x = int(input("Enter X: "))
y = int(input("Enter Y: "))
n = int(input("Enter N: "))

i = x + 1

while i <= y:
    if i % n == 0:
        print(i)
    i += 1








n = int(input("Enter a positive integer: "))

if n < 0:
    print("Invalid input")
else:
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    print("Sum of digits:", total)








n = int(input("Enter N: "))

if n <= 0:
    print("Invalid N")
else:
    divisible = 0
    not_divisible = 0

    while True:
        num = int(input("Enter a number: "))

        if num == -999:
            break

        if num % n == 0:
            divisible += 1
        else:
            not_divisible += 1

    print("Divisible numbers:", divisible)
    print("Non-divisible numbers:", not_divisible)









n = int(input("Enter a positive integer: "))

if n < 0:
    print("Invalid input")
else:
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        i += 1

    print("Factorial:", factorial)











n = int(input("Enter a positive integer: "))

if n < 0:
    print("Invalid input")
else:
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")













n = int(input("Enter N: "))

if n <= 0:
    print("Invalid input")
else:
    a = 1
    b = 1
    count = 1

    while count <= n:
        print(a, end=" ")

        c = a + b
        a = b
        b = c

        count += 1








n = int(input("Enter an integer: "))

if n <= 1:
    print("Not Prime")
else:
    i = 2
    prime = True

    while i * i <= n:
        if n % i == 0:
            prime = False
            break

        i += 1

    if prime:
        print("Prime")
    else:
        print("Not Prime")















sentence = input("Enter a sentence: ")

capital = 0
small = 0
digit = 0
special = 0

i = 0

while i < len(sentence):

    ch = sentence[i]

    if 'A' <= ch <= 'Z':
        capital += 1

    elif 'a' <= ch <= 'z':
        small += 1

    elif '0' <= ch <= '9':
        digit += 1

    else:
        special += 1

    i += 1

print("Capital letters:", capital)
print("Small letters:", small)
print("Digits:", digit)
print("Special characters:", special)                                       
