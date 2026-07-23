'''
abstraction: does not exist in python but we can achieve it using a library 
abstraction is used to simplifying complex system by focusing on essential features and hiding unnecessary details

'''

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side = side

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pass

    def perimeter(self):
        pass

obj = Square(1)
obj2 = Circle(2)

