# for loop in Python


import random

# i = 1
# while i <= 10:
#     print("Simplilearn")
#     i += 1


# i = 10
# while i >= 1:
#     print("Simplilearn")
#     i -= 1


# i = 1
# sum = 0
# while i <= 10:
#     # sum = sum + i
#     if i % 2 == 0:
#         sum = sum + i
#     i += 1
# print(sum)


# n = int(input("Enter a number: "))
# nr = 0
# while n % 10 != 0:
#     c = n % 10
#     nr = nr * 10 + c
#     n = n // 10
# print(nr)


# x = [1, 2, 3, "Simplilearn"]
# length = 0
# i = 0
# try:
#     while x[i]:
#         length += 1
#         i += 1
# except IndexError:
#     print(length)


# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(i, end="")
#         j += 1
#     i += 1
#     print()


# Game ~

nump = random.randint(1000, 9999)
n = int(input("Enter a 4 digit number: "))

while n != 10:
    num = nump
    cor = 0
    while num % 10:
        numc = num % 10
        nc = n % 10
        num = num // 10
        n = n // 10
        if numc == nc:
            cor = cor + 1
    if cor == 4:
        print("Congrats! You guessed it right")
        break
    else:
        print("%d digits were guessed right" % cor)
        n = int(input("Enter a 4 digit number: "))
else:
    print("You quite a game")
