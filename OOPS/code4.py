'''
Types of inheritance

single : 1 parent and 1 child
muliple inheritence : 2 parents and 1 child
multilevel : grandparen->parent->child
hierarchical : 1 parent and 2 child
'''

class Factorymumbai: #parent class/ superclass
    a = "i am an attribute inside Factorymumbai"
    
    def hello(self):
        print("i am a methos inside Factorymumbai")

    def __init__ (self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")


class Factorypune(Factorymumbai): #child class/ subclass
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"the name is {self.name} and age is {self.age}")


obj = Factorymumbai("laiba")
obj2 = Factorypune("Laiba", 20)

print(obj.a)
obj.hello()
obj.show()
obj2.show()