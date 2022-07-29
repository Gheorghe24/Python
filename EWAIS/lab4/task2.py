# Extending a class
from student import Student

# Creating an object instance from a class   
s = Student('John')  
s.change_grade(10)
# calling the method defined in the base class
s.say_hi() 
# class variables can also be accessed using class name 
#print(Student.kind)