# Threadings in Python


from threading import *
import time


"""
def show():
    print("this is a child thread")


t = Thread(target=show())
t.start()
print("This is a parent thread")
"""


"""
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("This is an child class")


t = MyThread()
t.start()

for i in range(5):
    print("\nThis is the main thread")
"""


"""
class Demo:
    def show(self):
        for i in range(5):
            print("This is the cild thread")


obj = Demo()
t = Thread(target=obj.show())

for i in range(5):
    print("\n This is the main thread")
"""


class Demo:
    def num(self):
        for i in range(1, 6):
            print("the number is ", i)
            time.sleep(1)

    def double(self):
        for i in range(1, 6):
            print("the double of the number ", 2*i)
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print("The square of the number is ", i*i)
            time.sleep(1)


obj = Demo()

t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

print("This is the main thread.")
