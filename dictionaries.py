# Dictionaries in Python


d1 = {}
print(type(d1))
# print(d1)


d2 = {1: "Welcome", 2: "to", 3: "Python", 4: "tutorial"}
# print(d2)

d3 = {"name": "Udoy", "age": 18, "profession": "student"}
# print(d3)

d4 = dict({1: "Welcome", 2: "to", 3: "Python", 4: "tutorial"})
# print(d4)


d5 = dict([(1, "Welcome"), (2, "to"), (3, "Python"), (4, "tutorial")])
# print(d5)

d6 = {"name": {"first": "Saifur", "last": "Udoy"},
      "age": 18, "profession": "student"}

# print(d6["name"]["first"])

d7 = {}
d7[0] = "Welcome"
d7[1] = ("How", "are", "you")
d7["name"] = "Udoy"
d7["mylove"] = {"first": "Dipty", "middle": "Sopnil", "last": "Sara"}
# print(d7)


# print(d7["mylove"]["last"])
# print(d7.get("name"))
# d7.pop(0)

# d7.popitem()
# print(d7)

# print(d7.values())
# print(d7.keys())


# Set =>

s = set([1, 2, 3, 4])
# print(s)
# print(type(s))

s.add("a")
print(s)

fs = frozenset([1, 2, 3, 4])
print(fs)

s1 = set([1, 3, 5, 7])
s2 = set([3, 4, 6, 7, 8])

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.clear())
