#eval
print(eval("345"))
print(eval("34-5"))
print(eval("3+4"))

#area
#r=float(input("Enter the radius:"))
#area=3.14*pow(float(r),2)
#print("The area of your circle is",area)

#average calculator
N=int(input("Enter number of terms "))
num=[]
for i in range(N):
    i=int(input("Enter a number: "))
    num.append(i)
total=sum(num)
average= total/N
print("Your average is:", average)
#class
class Dog:
    def __init__(self, name):
       self.name= name
    
    def bark(self):
        print(f"{self.name} says Woof! ")
dog1 = Dog("Binod")
dog2 = Dog("Vinod")
dog1.bark()
dog2.bark()

class car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Car brand: {self.brand}, Model: {self.model}")

car1 = car("Toyota", "Corolla")
car2 = car("Tesla", "Model S")

car1.display()  
car2.display()  

#inheretance
class Animal:
    def __init__ (self, name):
        self.name = name

    def speak(self):
        print(f"(self.name) makes a sound.")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# protected classes
class person:
    def __init__ (self, name, age):
        self._name= name
        self.__age= age
    def get_age(self):
        return self.__age
p= person("John", 30)
print(p._name)  # Accessing protected attribute
print(p.get_age())