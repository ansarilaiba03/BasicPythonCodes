'''
muliple inheritence : 2 parents and 1 child
'''

class Animal:
    def __init__(self,name):
        pass

class Human(Animal):
    def __init__(self,name,age):
        pass

#the contructor function will be inherited of the first class that has been inherited. this is MRO(Method resolution order) followed by python

# class Robots(Animal, Human):
class Robots(Human, Animal):
    name3 = "r1"

obj = Robots()

print(obj.name)