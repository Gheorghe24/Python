from person import Person
from student import Student

list1 = []
list1.append(Student('John'))
list1.append(Student('Ana'))
list1.append(Student('Irene'))
list1.append(Student('Serj'))
list1.append(Person('Serj'))
list1.append(Person('Vanya'))
list1.append(Person('Jack'))
list1.append(Person('GG'))

for obj in list1:
    # calling method 
    obj.say_hi()
