# Python tuples


emp = ()
# print(type(emp))
# print(emp)


city = ("Sylhet", "Dhaka", "Borisal")
# print(type(city))
# print(city)

# `list` is mutable it can be change, `tuple` is immutable it cannot be change

list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)

list1.append(5)
# print(list1)

# tuple1.append(5)
# print(tuple1)


# print(city[1])
# print(city[-1])

# print(city + tuple1)


# rep = ('Python',)*5
# print(rep)

# rep2 = ('Python',)
# print(rep2*10)


# print(city[1:])
# print(city[:])
# print(city[:1])


a = tuple("Simplilearn")
# print(a)

# a,b,c,d = tuple1
# print(a,b,c,d)

# This `star` means `b` is a is a list
a, *b, c, d = tuple1
# print(a,b,c,d)


# Built in function ~
tpl = (3, 4, 5, 6, 3, 5, 4, 4, 4, 3, 5, 4, 6, 7, 6)
print(tpl.count(6))
print(len(tpl))
print(max(tpl))
print(min(tpl))

# Nesting tuples in list ~
lst = [1, 2, 3, 4]
# print(type(lst))
x = tuple(lst)
# print(x)
# print(list1)

multpl = [(1, 2, 3), (4, 5, 6)]
# print(multpl)
multpl.append(("Tuple", "inside", "list"))
# print(multpl)

multpl.remove((4, 5, 6))
# print(multpl)

multpl2 = (['a', 'b', 'c'], ['d', 'e', 'f'])
print(multpl2)
# print(type(multpl2))

multpl2[0].append('z')
print(multpl2)

multpl2[1].remove('e')
print(multpl2)
