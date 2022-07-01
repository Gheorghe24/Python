from person import Person
from course_gpa import add_course_grade
from course_gpa import compute_gpa

class Student(Person):
    # init method or constructor
    def __init__(self, name):
        # you can reuse the method in the base class
        super().__init__(name) #superior class
        # this also works
        Person.__init__(self, name)
        # initialize instance attribute
        self.grade = None
        self.course_grades = []
 
    # sample method
    def change_grade(self, grade):
        # set instance attribute
        self.grade = grade
        
    #comment next 3 lines for task3
    def say_hi(self):
        super().say_hi()
        print('My grade is', self.grade)
    
    add_course_grade = add_course_grade
    compute_gpa = compute_gpa