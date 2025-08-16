# abstract class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
#experience the real power oif abstract classes
from abc import ABC, abstractmethod
class transport(ABC):
    @abstractmethod
    def travel_time(self, distance):
        pass
class Bus(transport):
    def travel_time(self, distance):
        return distance/50
class Train(transport):
    def travel_time(self, distance):
        return distance/100
class Airplane(transport):
    def travel_time(self, distance):
        return distance/600
distance=300
transports = [Bus(), Train(), Airplane()]
for t in transports:
    print(f"Travel time by {t.__class__.__name__} for {distance} km: {t.travel_time(distance)} hours")
#one more way
from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__ (self, speed):
        self.speed = speed

    def tarvel_time(self, distance):
        return distance / self.speed   
    @abstractmethod
    def travel_time(self, diatance):
        pass

class Bus(Transport):
    def travel_time(self, distance):
        return distance / self.speed

class Train(Transport):
    def travel_time(self, diatance):
        return distance / self.speed
class Airplane(Transport):
    def travel_time(self, distance):
        return distance / self.speed    
distance =300
transports =[Bus(50), Train(100), Airplane(600)]
for t in transports:
    print(f"Travel time by {t.__class__.__name__} for {distance} km: {t.travel_time(distance)} hours")
