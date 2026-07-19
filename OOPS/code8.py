#method overloading (incorrect)

class Animal:
    def show(self):
        print("hello")

    def show(self,name):
        self.name = name
        print(f"name : {self.name}")

obj = Animal()

obj.show()