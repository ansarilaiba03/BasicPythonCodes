'''
Polymorphism: 
word means 'many form', it allows the same interface or method name to behave differently depending on the object or context

it can be achieved in python in 2 ways... in compile time language (java, c++) there a 3 types but python does not support Method overloading
Method overloading : means having same name method inside a class but parameters will be different but in python the latest definition will overwrite the previous one
Method overriding : it is where a child class overrides a method to call, based on the object type
Duck typing: different class (no inheritence) same method name
'''

#method overriding 

class Animal:
    def show(self):
        print("hello")

class Human(Animal):
    def show(self):
        print("hii")

obj = Human()

obj.show()