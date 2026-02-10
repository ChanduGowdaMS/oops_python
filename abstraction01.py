from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Sleeping..........")

class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
class Cow(Animal):
    def sound(self):
        print("Moo")

a1=Dog()
a2=Cat()
a3=Cow()
a1.sound()
a1.sleep()
a2.sound()
a2.sleep()
a3.sound()
a3.sleep()