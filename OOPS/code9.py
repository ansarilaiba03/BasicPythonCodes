#duck typing

class Animal:
    def show(self):
        print("hello")

class Human:
    def show(self):
        print("hii")

obj1 = Human()
obj2 = Animal()

obj1.show()
obj2.show()