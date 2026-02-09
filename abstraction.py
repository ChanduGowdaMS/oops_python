from abc import ABC, abstractmethod
    
class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        print("Engine started.....")
class Car(Vehical):
    def start_engine(self):
        print("Car: Engine started.....")
class Bike(Vehical):
    def start_engine(self):
        print("Bike: Engine started.....")
class Bus(Vehical):
    def start_engine(self):
        print("Bus: ENgine started.....")


o1=Car()
o2=Bike()
o3=Bus()
o1.start_engine()
o2.start_engine()
o3.start_engine()