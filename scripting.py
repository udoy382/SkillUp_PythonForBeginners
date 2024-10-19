# Scripting in Python

import os
import time
import smtplib


"""
def current_directory():
    cwd = os.getcwdb()
    print(cwd)


def file_path(filename):
    path = os.path.abspath(filename)
    print(path)


current_directory()

filename = "myfile.txt"
file_path(filename)
"""


"""
epc = time.time()
print(epc)


localtime = time.localtime(epc)
print(localtime.tm_year)
print(time.ctime(epc))
"""


"""
smtobj = smtplib.SMTP('smtp.gmail.com', 587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login("srudoy436@gmail.com", "srudoy2299436")
smtobj.sendmail("srudoy436@gmail.com", "srudoy436@gmail.com", "Subject: SMTP check \n This is a test email.")
smtobj.quit()
"""


"""
def creatfile(dest):
    if not (os.path.isfile(dest)):
        f = open(dest, "w")
        f.write("Welcome to Python scripting")
        f.close()


dest = "D:\\SkillUp_PythonForBeginners\\test.txt"

creatfile(dest)

print("File created")
"""


"""
def func1(*args, **kwargs):
    # for i in args:
    #     print(i)

    for i in kwargs.items():
        print(i)

# func1(10, 20, 30, 40, "simplilearn") # This is for args
func1(a=10, b=20, c=30) # This is for kwargs
"""


"""
def func1():
    x = 10
    def func2(x):
        return x + 1
    return func2(x)
    
result = func1()
print(result)
"""


"""
def func1(called_func):
    print("This is the first fucntion")

    def nested_function():
        print("This is te nested funciton")
        called_func()
    return nested_function()

# @func1
def outer_func():
    print("This is the outer function")

obj = func1(outer_func)
"""