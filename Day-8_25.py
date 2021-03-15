class Fruits:
    name = "Fruits"
    def __init__(self,name = None):
        self.name = name
    
orange = Fruits("Orange")
print("orange name is",orange.name)

grape = Fruits()
grape.name = "Grape"
print("grape name is",grape.name)
#这一题做的不明不白的。