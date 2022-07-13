
# Method = function that goes inside of a class
class Dog:

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

d = Dog("Tim", 34)  
d2 = Dog("Bill", 12)

print(d.get_name())
print(d2.name)
