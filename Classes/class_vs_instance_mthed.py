class Point:
    default_color = "red"
    """magic object"""
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    @classmethod   
    def zero(cls):
        return cls(1,2)  

    """{x} and {y} is an instance attribute"""
    def draw(self):
        print(f"point ({self.x}, {self.y})")

"""factory object"""
point =  Point.zero()
point.draw()