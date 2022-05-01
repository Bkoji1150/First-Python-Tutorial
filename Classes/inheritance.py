class Animal:
    """constructor"""
    def __init__(self):
        self.age = 1
        print("Mammal Construstor")
        
    def eat(self):
        print("eat")
       

# Animal is the Parent, Base
# Mammal is the Child, sub class
class Mammal(Animal):
    def walk(self):
        print("walk") 
        
        print("Mammal Construstor")
         self.weight = 2   
        supper().__init__() 

class Fish(Animal):
    def swim(self):
        print("swim")   

m = Mammal()
m.eat()  
m.walk()     
print(m.age)
f = Fish()
