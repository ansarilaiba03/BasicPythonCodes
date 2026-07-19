#multilevel inheritence

class Factory:
    def __init__(self,material,zip):
        self.material = material
        self.zip = zip

class BhopalFactory(Factory):
    def __init__(self,material,zip,color):
        super().__init__(material,zip)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self,material,zip,color,pocket):
        super().__init__(material,zip,color)
        self.pocket = pocket

    def show(self):
        print(f"material: {self.material}\nzip: {self.zip}\ncolor: {self.color}\npocket: {self.pocket}")

obj = PuneFactory("leather",2,"black",1)

obj.show()