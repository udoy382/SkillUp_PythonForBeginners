# Array in Python


from array import *


arr = array('i', [1, 2, 2, 3, 4, 5])

# print(type(arr))
# print(arr)
# print(arr.buffer_info())
# print(arr[2])


# for i in arr:
#     print(i)


# for pnt in range(4):
#     print(pnt, arr[pnt])


# arr.reverse()
# print(arr)


# arr.append(10)
# print(arr)


# arr.remove(2)
# print(arr)

# print(arr[2])
# print(arr.index(2))


arr = array("i", [])
x = int(input("Enter size of array: "))
print("Enter %d elements" % x)

for i in range(x):
    n = int(input())
    arr.append(n)
print(arr)
