# Pandas in Python


import pandas as pd
import numpy as np


# Check pandas version ~
# print(pd.__version__)


#               Series create, manipulate, querry, delete ~

# Creating a series from a list ~
"""
arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)
# print(s1)

order = [1, 2, 3, 4, 5]
s2 = pd.Series(arr, index=order)
print(s2)
"""

"""
n = np.random.randn(5) # Create a random Ndarray
index = ['a', 'b', 'c', 'd', 'e']
s3 = pd.Series(n, index=index)
print(s3)
"""

# Create series from dictionary ~
"""
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s4 = pd.Series(d)
print(s4)
"""

# You can modify the index of series ~
"""
arr2 = [0, 1, 2, 3, 4]
s5 = pd.Series(arr2)
s5.index = ['A', 'B', 'C', 'D', 'E']
print(s5)
"""

# Slicing ~
"""
arr3= [0, 1, 2, 3, 4]
s6 = pd.Series(arr3)

# a = s6[:3]
a = s6[3:]
print(a)
"""

# Append and drop secries ~
"""
arr4= [0, 1, 2, 3, 4]
s7 = pd.Series(arr4)

arr5= [5, 6, 7, 8, 9]
s8 = pd.Series(arr4)

s7.drop(3)
print(s7)
"""

"""
ser1 = [0, 1, 2, 3, 4, 5, 7]
ser2 = [6, 7, 8, 9, 5]

x = pd.Series(ser2)
print(x)

y = pd.Series(ser1)
print(y)

# ser2.append(ser1)
# print(ser2)

# x.sub(y)
# print(x)
"""


#               Create Dataframe ~
"""
dates = pd.date_range('today', periods=6)  # Define time sequence as idnex
# print(dates)


num_arr = np.random.randn(6, 4)  # Import numpy random array
# print(num_arr)


columns = ['A', 'B', 'C', 'D']  # Use the table as the column name
df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
# print(df1)


data = {
    "animal": ['cat', 'cat', 'snake', 'dog', 'dog', 'dog', 'snake', 'cat', 'dog', 'dog'],
    "age": [2, 3, 4, 5.7, np.nan, 5, 6, 4, 6, np.nan],
    "visits": [1, 2, 3, 4, 5, 3, 5, 2, 4, 2],
    "priority": ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df2 = pd.DataFrame(data, index=labels)
# print(df2)
# print(df2.index)
# print(df2.columns)

df2.sort_values(by='age')[2:5]
# print(df2)
"""


#               Dataframe file operations

df_animal = pd.read_csv("animal.csv")
# print(df_animal.head(3))
