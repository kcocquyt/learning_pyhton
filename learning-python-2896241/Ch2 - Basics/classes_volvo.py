#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, horsepower):
        self.mode = "Volvo"
        self.horsepower = horsepower



class XC40(Vehicle):
    def __init__(self, enginetype):
        super().__init__("XC40")
        self.max_km = 830
        self.doors = 4
        self.acceleratie = 7.6
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")
        
class EC40(Vehicle):
    def __init__(self, enginetype):
        super().__init__("EC40")
        self.max_km = 290
        self.doors = 4
        self.acceleratie = 4.6
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")

class V60(Vehicle):
    def __init__(self, enginetype):
        super().__init__("V60")
        self.max_km = 800
        self.doors = 4
        self.acceleratie = 4.6
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")
        
        
class EX40(Vehicle):
    def __init__(self, enginetype):
        super().__init__("V60")
        self.max_km = 574
        self.doors = 4
        self.acceleratie = 4.6
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")

class EX30(Vehicle):
    def __init__(self, enginetype):
        super().__init__("EX30")
        self.max_km = 476
        self.doors = 4
        self.acceleratie = 3.6 
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")

class V60_H(Vehicle):
    def __init__(self, enginetype):
        super().__init__("V60")
        self.max_km = 800
        self.doors = 4
        self.acceleratie = 4.6 
        self.engine = enginetype

    def drive(self, horsepower):
        super().drive(horsepower)
        print("Driving my Volvo", self.engine, "with horsepower of ", self.horsepower, "pk")

car1 = XC40("Petrol")
car2 = EC40("Electric")
car3 = V60("Hybride")
car4 = EX40("Electric")
car5 = EX30("Electric")
car6 = V60_H("Petrol")

print("XC40=",car1.max_km,"km")
print("Ec40=",car2.engine)
print(car3.doors)

car1.drive(197)
car2.drive(442)
car3.drive(455)
car4.drive(574)
car5.drive(428)
car6.drive(197)

