def add_course_grade(self, course_grade):
    # course_grade is an object attached by composition 
    self.course_grades.append(course_grade)
 
def compute_gpa(self):
    self.grade = sum([course_grade.grade for course_grade in self.course_grades])/len(self.course_grades)