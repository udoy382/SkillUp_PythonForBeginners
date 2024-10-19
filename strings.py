# Python strings

stg = "Tim's birthday"
print(stg)


stg2 = "Tim said \"I am busy today"
print(stg2)


stg3 = """ hey there
this is multiple line sting
"""
print(stg3)

# print(len(stg3))
# print(stg[6])

# for i in stg3:
#     # print(i)
#     print(i, end="")


# print(stg[:7])
# print(stg[3:])
# print(stg[2:5])


# print(stg.upper())
# print(stg.lower())
# print(stg3.find("s"))
# print(stg3.index("l"))
# print(stg.split(" "))
# print(stg.replace('Tim', "Udoy"))


x = "good"
y = "morning"

z = x + " " + y
# print(z)
# print(x + " " + y)


a = "Hey"
b = "there"
c = "all"
# d = "{} {} {}".format(a, b, c)
d = f"{a} {b} {c}"
print(d)