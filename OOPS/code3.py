'''
types of attributes:
class attribute
instance attribute

types of methods:
instance methods

self targets object location, it access instance(objects)
cls targets class location, it access class
static method does not access class or instance(objects)
'''

class Animal:
    name = 'lion' #class attribute

    def __init__(self,age):
        self.age = age # instance attribute

    def show(self): #instance method
        print("how are you")

    @classmethod #decorator
    def hello(cls): #cls will target the class location (Animal)
        print("hello")

    @staticmethod #decorator
    def static():
        print("hiiii")

obj = Animal(12)
obj.show()
obj.hello()
obj.static()