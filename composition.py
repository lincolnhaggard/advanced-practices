#composition is a class that exists insie of another class (class ha s other class)

class Car:
    def __init__(self, make, modle, year,engine):
        self.make=make
        self.modle=modle
        self.year=year
        self.engine=engine

    def __str__(self):
        return f"{self.year} {self.make} {self.modle}"
    
class Engine:
    def __init__(self,configuration,displacement,horsepower,torque):
        self.configuration=configuration
        self.displacement=displacement
        self.horsepower=horsepower
        self.torque=torque
    
    def ignite(self):
        print("Vroom, vroom")


myengine = Engine("V8",5.8,326,344)
mycar = Car("Mazda","Mazda3", 2013,myengine)

#to call a composit class you must acces where it is saved within the class
print(mycar)
mycar.engine.ignite()