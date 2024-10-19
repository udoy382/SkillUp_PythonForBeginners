# Objects and Classes in Python


"""
class Person:
    def __init__(self, n, g, a):
        # self.name = "Udoy"
        # self.gender = "Male"
        # self.age = 18

        self.name = n
        self.gender = g
        self.age = a

    def talk(self):
        print("Hi! I am ", self.name)

    def vote(self):
        if self.age < 18:
            print("I am not eligible to vote")
        else:
            print("I am eligible to vote")


obj = Person("Udoy", "Male", 18)
obj2 = Person("Sara", "Female", 14)

# Two way to call our functions ~

# Person.talk(obj)
# Person.vote(obj)

# obj.talk()
# obj.vote()


print(obj2.name, obj2.gender, obj2.age)

obj2.talk()
obj2.vote()
"""


class Car:
    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getSpeed(self):
        # print("155 mph")
        print("Maximum speed is: ", self.speed)

    def setSpeed(self, speed):
        self.speed = speed


class Sedan(Car):   # Child class
    def accelerate(self):
        print("137")

    def opentrunk(self):
        print("Trunk has been opened")


class SUV(Car):     # Child class
    def accelerate(self):
        print("127")


BMW = Car(2018, 155)
FORD = Car(2027, 140)

# Car.getSpeed(BMW)
# Car.getSpeed(FORD)

# BMW.getSpeed()
# FORD.getSpeed()

# BMW.setSpeed(999)
# BMW.getSpeed()


Honda = Sedan(2018, 150)
# BMW.getSpeed()

# Honda.getSpeed()
# Honda.accelerate()
# Honda.opentrunk()
