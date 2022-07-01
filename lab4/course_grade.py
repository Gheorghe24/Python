# import this module
import datetime
from student import Student
 
# define a new class to contain the grade for a course
class CourseGrade():
    # init method or constructor
    def __init__(self, course_id, grade, date):
        self.course_id = course_id
        self.grade = grade
        self.date = date
        self.date_changed = date
 
    # sample method
    def change_grade(self, grade, date):
        print("grade changed from: ", self.grade, " to: ", grade, " at: ", date)
        self.grade = grade
        self.date_changed = date
 
student = Student('John')

course_grade = CourseGrade('EWIS', 9, datetime.date(2022, 3, 30))
student.add_course_grade(course_grade)
course_grade.change_grade(10, datetime.date(2022, 3, 31))

course_grade = CourseGrade('EWIS', 8, datetime.date(2021, 3, 30))
student.add_course_grade(course_grade)
course_grade.change_grade(8, datetime.date(2022, 3, 31))

student.say_hi()
student.compute_gpa()
student.say_hi()
