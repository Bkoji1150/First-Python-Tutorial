class Point:
    default_color = "red"
    """magic object"""
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    """{x} and {y} is an instance attribute"""
    def draw(self):
        print(f"point ({self.x}, {self.y})")



point = Point(1,2) 
point.draw()

another = Point(2,3)
another.draw()