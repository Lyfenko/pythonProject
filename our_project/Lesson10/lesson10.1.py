# ZeroDivisionError
#
# class ShortPasswordError(Exception):
#     "Error handling for shourt user passsword"
#
# def password(passw):
#     try:
#         if len(passw)<8:
#         return "Your password is shorter than 8 symbols"
#     except ShortPasswordError:
#         print (f"len of your password is {len(passw)}")
#     else:
#         pass

# classes
# OOP

# class Dog:
#     """Model of dog"""
#     def __init__(self, name, age):
#         """Initialize attributes name and age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Dog sit"""
#         print(self.name.title() + " is sitting now")
#
#     def roll_over(self):
#         """Dog is roll over"""
#         print(self.name.title() + " rolled over")
#
# rex = Dog("Rex", 3)
# # print(rex) #object
# print("My dog name is " + rex.name)
# print("My dog age is " + str(rex.age))
# rex.sit()
# rex.roll_over()
#
# bob = Dog("Bob", 10)
# print("My dog name is " + bob.name)
# print("My dog age is " + str(bob.age))
# bob.sit()
# bob.roll_over()


# class Car:
#     """Model of car"""
#
#     def __init__(self, make, model, year):
#         """Inicialize car atributes"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometr = 0
#
#     def correct_name(self):
#         """Correct name of car"""
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()
#
#     def read_odometr(self):
#         """How many kilometers car ride"""
#         print("This car has " + str(self.odometr) + " km")
#
#     def update_odometr(self, kilometers):
#         """Update odometr value"""
#         if kilometers >= self.odometr:
#             self.odometr = kilometers
#         else:
#             print("You can`t roll back an odometer")
#
#     def increase_odometr(self, kilometers):
#         """Increase kilometers value"""
#         self.odometr += kilometers

# new_car = Car("mercedes", "s600", 2020)
# print(new_car.correct_name())
# new_car.read_odometr()
#
# new_car.odometr = 58
# new_car.read_odometr()

# bmw = Car("Bmw", "x5", 2018)
# print(bmw.correct_name())
# bmw.update_odometr(40000)
# bmw.read_odometr()
#
# bmw.increase_odometr(1000)
# bmw.read_odometr()

#
# class Battery:
#     """Battery"""
#     def __init__(self, battery=40):
#         self.battery = battery
#
#     def battery_inf(self):
#         print("This car has a " + str(self.battery) + "Kwh")
#
#     def get_range(self):
#         if self.battery == 40:
#             range = 150
#         elif self.battery == 75:
#             range = 280
#
#     print("This car can approximately go " + str('range'))
#
#
# class ElectricCar(Car):
#     """Model for electric car"""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def battery_inf(self):
#         """show battery inf"""
#         print("This car has a " + str(self.battery) + "Kwh")
#
#
#
#
# nissan_leaf = ElectricCar("nissan", "leaf", 2022)
# print(nissan_leaf.correct_name())
# nissan_leaf.battery_inf()
# nissan_leaf.battery.get_range()

class Dog:
    vyd = "animal"

    def __init__(self, name, age):
        """Initialize attributes name and age"""
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def sit(self):
        """Dog sit"""
        print(self.name.title() + " is sitting now")

    def roll_over(self):
        """Dog is roll over"""
        print(self.name.title() + " rolled over")

class FrenchBuldog(Dog):
    pass

class Vivcharka(Dog):
    pass

rex = Vivcharka("rex", 5)
lala = FrenchBuldog("lala", 3)

rex.sit()

lala.roll_over()

print("Type ", type(rex))

print(isinstance(rex, Vivcharka))

print(isinstance(rex, Dog))
