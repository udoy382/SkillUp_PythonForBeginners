# Python Numbers

import math

# Numbers ~
num = 5
# print(type(num))

num2 = 23323232323
# print(num2)
# print(type(num2))

num3 = 5.4
# print(num3)
# print(type(num3))

num4 = 2 + 5j
# print(num4)s
# print(type(num4))
# print(num4.real)
# print(num4.imag)

num5 = -565656.675
# print(num5)

num6 = 10
num7 = 2
# print(num6 + num7)
# print(num6 - num7)
# print(num6 * num7)
# print(num6 ** num7)
# print(num6 / num7)
# print(num6 // num7)
# print(num6 % num7)

x = "123"
# print(type(x))

x = int(x)
# print(type(x))

x = float(x)
# print(type(x))

y = -7.5
# print(abs(y))

z = 10
# print(math.exp(z))
# print(math.pi)
# print(math.sqrt(9))

# List ~
lis = [1, 2, 3, 4]
# print(lis)

letter = ['a', 'b', 'c', 'd']
# print(letter)

stg = ["get", "certified", "get", "ahead"]
# print(stg)

mix = [1, 4, "simplilearn", "get", "certified"]
# print(mix)

mat = [[1, 2], ['a', 'b']]
# print(mat)


# print(mix[3])
# print(mix[-2])
# print(mix[:3])
# print(mix[3:])
# print(mix[2:4])
# print(mix[::2])
# print(mix[::-1])

t = [0]*100
# print(t)

conc = letter + stg
# print(conc)

var = list("hey there")
# print(var)

one, *other = lis
# print(one)
# print(other)

lis.extend(stg)
print(lis)

lis.insert(5, "simplilearn")
print(lis)

lis.remove(2)
print(lis)


myvar = ['b', 'c', 'a', 'd', 'f', 'h', 'g', 'e']
myvar.sort()
# print(myvar)


pp = [4, 5, 6, 7, 8, 4, 5]
print(len(pp))
print(min(pp))
print(max(pp))
print(sum(pp))
print(sum(pp) / len(pp))
