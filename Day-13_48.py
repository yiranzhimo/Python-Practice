class Circle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return(self.length*self.width)
circle = Circle(3,4)
print(circle.area())