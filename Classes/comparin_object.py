"""Somtime we can compare object in python"""

class Man:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, other):
        return self.x == other.y and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def genter_type(self):
        return "Male"


    def profession(self):
        return f"My first name is {self.x}, and my last name is {self.y}"


man = Man("koji", "Bello")
result = man.profession()
print(result)
# philo = Man(20, 20)
# kelder = Man(20, 20)
# print(philo == kelder)
# bello = man.profession()
# print(bello)

