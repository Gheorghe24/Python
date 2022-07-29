# Creating a class
class Person:  
    # class attributes
    kind = "human"
 
    # init method or constructor   
    def __init__(self, name):
        # instance attributes
        self.name = name  
 
    # sample method  
    def say_hi(self):  
        print('Hello, my name is', self.name)  