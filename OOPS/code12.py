'''
dunder methods: are special methos in python that start and ends with double underscores, like __init__, __str__, __add__, etc
they automatically get called when you perform certain actions on an object
use return not print
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"
    
    def __add__(self,other):
        return f"your sum of ages are {self.age + other.age}"
    
obj = Animal("lion",12)
obj2 = Animal("dolphin",14)

print(obj + obj2)


# sum of 3

class Animal2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"
    
    def __add__(self,other):
        sum = 0
        for i in other:
            sum = sum + i.age

        return f"your sum of ages are {self.age + sum}"
    
obj = Animal2("lion",12)
obj2 = Animal2("dolphin",14)
obj3 = Animal2("tiger", 34)

print(obj + (obj2, obj3))