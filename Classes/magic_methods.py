class Point:
    default_color = "red"
    """magic object"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"{self.x}, {self.y}"
        
        
point = Point(x=1, y=2)
print(point)
