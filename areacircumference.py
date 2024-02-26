class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getarea(self):
        return 3.142 * self.radius**2
        
    def getcircumference(self):
        return self.radius * 2 * 3.142
        
    
if __name__ == "__main__":
    circle = Circle(7)
    print("area of circle:", circle.getarea())
    print("circumference of circle:", circle.getcircumference())