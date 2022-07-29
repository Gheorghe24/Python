# Creating a class
class Student:  
 
    # init method or constructor   
    def __init__(self, name):
        # instance attributes
        self.name = name 
        
 
    # sample method  
    def change_grade(self, grade):  
        self.grade = grade
 
# creating an object instance from a class   
p = Student('Alice')
# calling an instance method  
p.change_grade(10)
 
# creating an object instance from a class   
b = Student('Bob')
# calling an instance method  
b.change_grade(8) 



