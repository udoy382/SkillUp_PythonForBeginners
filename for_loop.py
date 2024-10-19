# for loop in Python


"""
x = [1, 2, 4, " Simplilearn "]
y = " Saifur Rahman Udoy"

for i in x:
    print(i, end="")

for i in y:
    print(i, end="")
"""


"""
# for i in range(0, 21):
#     print(i)

# for i in range(0, 21, 2):
#     print(i)


sum = 0
for i in range(0, 21):
    if i % 2 == 0:
        sum = sum + 1

print(sum)
"""


"""
user = int(input("Enter a number : "))

for i in range(1, user + 1):
    for j in range(1, i):
        print(j, end="")
    print()
"""


r = int(input("Enter number of rows: "))
c = int(input("Enter number of colomns: "))

val = []

x = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input("Enter the %d + %d element " % (i, j))))
    x.insert(i, val)

y = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input("Enter the %d + %d element " % (i, j))))
    y.insert(i, val)
    val = []

sum = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i, val)
    val = []

print(sum)
