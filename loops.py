# loops in Python


# 1. For loop
# 2. While loop
# 3. Nested loops [for in for / while in while / for in while / while in for]


# While loop ~
"""
val = int(input("Enter a multiple of 7 : "))

while val % 7 != 0:
    val = int(input("Enter a multiple of 7 : "))
else:
    print("%d is a multiple of 7" % val)
"""

# For loop ~
"""
# x = [1, 2, 3, "Simplilearn"]
x = "Simplilearn"

for i in x:
    print(i)
"""

# Nested loops ~
"""
x = [[1, 2,3],[ 'a', 'b', 'c']]

for i in x:
    for j in i:
        print(j, end=" ")
"""


"""
x = "Hey there. how are you"

for i in x:
    if i == ".":
        break
    print(i, end="")
"""

"""
for i in [1, 2, 3, 13, 34, 3, 6]:
    if i > 10:
        continue
    print(i)
"""
