class Circle():
    def __init__(self,r):
        self.radius = r
    def area(self):
        return(3.14*self.radius*self.radius)
circle = Circle(2)
print(circle.area())
#慢慢了解 self,__init__ 的概念。