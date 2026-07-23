'''
encapsulation:
it means hiding the internal details of how things work and only showing what is needed

access modifiers:
1. public attributs and methods : every method and attribute can be accessed 
2. protected attributes and methods : python protected members are created using a single underscore but it still can be accessed from outside the class, python dosent enforce protectec access like other languages (eg. java, C++) but it uses a naming convention to tell developers
3. private attributes and methods :it cannot be accessed from outside the class.. in python we use two underscore (__) before the name to make it private
'''

#public attributes and methods

class Factory():
    a = "pune"

    def show(self):
        print("hello")

class Bhopal(Factory):
    def show2(self):
        print(super().a)

obj = Bhopal()
obj.show2()

#protected attributes and methods

class Factory2():
    _a = "pune"

    def _show(self):
        print("hello")

class Bhopal2(Factory2):
    def show2(self):
        print(super()._a)

obj2 = Bhopal2()
obj2.show2()

#private attributes and methods : should get error

class Factory3():
    __a = "pune"

    def __show(self):
        print("hello")

class Bhopal3(Factory3):
    def show2(self):
        print(super().__a)

obj3 = Bhopal3()

#commented so that rest of the code works (but to check, remove the comments)
# obj3.show2()  
# obj3.__show()

# but but can be printed indirectly 

class Factory4:
    __a = "pune"

    def show(self):
        print(Factory4.__a)

obj4 = Factory4()
obj4.show()