'''
constructor = it is a method that runs automatically when we call a class and this constructor function will target the objects location

'''
class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material # 100.material = leather amd 200.material = nylon
        self.zips = zips # 100.zips = 3 and 200.zips = 1
        self.pockets = pockets # 100.pockets = 2 amd 200.pockets = 3

    def show(self): #this self will store the location of the object that calls this method
        print(f"your objects details are {self.material}, {self.pockets}, {self.zips}")

# self is used to capture the location of object like reebok and campus
reebok = Factory("leather", 3, 2) #assume for reebok self = eg. 100
campus = Factory("nylon", 1,3)  #assume for campus self = eg. 200

print(reebok.pockets)
print(campus.pockets)

reebok.show()