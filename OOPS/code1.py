'''
a class is a blueprint for you objects

there are 2 types of thing inside class, attributes and methods:
Attributes = variables defined inside the class
Methods = functions defined inside a class

objects = they can call a class outside the class


'''
class Factory: 
    a = 12  #attribute

    def hello(self):  #method
        print('hello how are you')

    print("i am getting initialized")

print(Factory().a)
Factory().hello()

obj = Factory() #object
obj.hello()

