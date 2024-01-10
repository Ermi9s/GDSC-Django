import unittest
#Ex 1
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def displayInfo(self):
        print(f"model: {model}")
        print(f"make: {make}")
        print(f"year: {year}")
#Ex 2
class Electric_Car(Car):
    def __init__(self,make,model,year,battery_capacity):
        Super().__init__(make,model,year)
        self.battery_capacity = battery_capacity
    def displayBatteryCpacity(self):
        print(f"Battery capacity: {self.battery_capacity}")
#Ex 3
class BankACC:
    def __init__(self,AccNO , Balance):
        self.__AccNO = AccNO
        self.__Balance = Balance
        
    def deposite(slef,ammount):
        self.__Balance += ammount
        return self.__Balance

    def withdraw(self , ammount):
        self.__Balance -= ammount
        return self.__Balance

    def showBalance(self):
        return (f"Balance: {self.__Balance}")
#Ex 4
class Shape:
    pass

class Circle(Shape):
    def __init__(self , rad):
        self.radius = rad
    def calcArea():
        return 3.14 *(self.radius ** 2)

class Rct(Shape):
    def __init__(self , length ,width):
        self.length = length
        self.width = width
    def capcArea():
        return self.length * self.width
    
class Tri(Shape):
    def __init__(self , base, height):
        self.width = width
        self.height = height
    def calcArea():
        return (1/2) * (self.width * self.height)

def calculateArea(Shape):
    Shape.calcArea()

#Ex 5
class TestBancAccMethodes(unittest.TestCase):
    def test_withdrarwal(self):
        acc = BankACC(0,500)
        self.assertEqual(acc.withdraw(400),100,"Withdraw is incorrect!")
    def test_deposite(self):
        acc = BankACC(0,500)
        self.assertEqual(acc.deposite(100) , 600 , "Deposite in incorrect!")
    def test_showBalance(self):
        acc = BankACC(0,789)
        self.assertEqual(acc.showBalance(),f"Balance: {789}", "showBAlance in incorrect!")











