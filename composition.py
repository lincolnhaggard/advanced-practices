#composition is a class that exists insie of another class (class ha s other class)

class Car:
    def __init__(self, make, modle, year,engine):
        self.make=make
        self.modle=modle
        self.year=year
        self.engine=engine

    def __str__(self):
        return f"{self.year} {self.make} {self.modle}"
    #for other programers, for debugging purposes tell class and all atributes
    def __repr__(self):
        return f"Car({self.make}, {self.modle}, {self.year}, {self.engine})"
    
class Engine:
    def __init__(self,configuration,displacement,horsepower,torque):
        self.configuration=configuration
        self.displacement=displacement
        self.horsepower=horsepower
        self.torque=torque
    
    def ignite(self):
        print("Vroom, vroom")

    def __str__(self):
        return f"The engine is a {self.configuration} with {self.displacement}, {self.horsepower} horsepower and {self.torque} torque"

    def __repr__(self):
        return f"Engine({self.configuration}, {self.displacement}, {self.horsepower}, {self.torque})"

myengine = Engine("V8",5.8,326,344)
mycar = Car("Mazda","Mazda3", 2013,myengine)

#to call a composit class you must acces where it is saved within the class
print(mycar)
mycar.engine.ignite()
print(repr(mycar))