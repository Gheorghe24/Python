class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old" )

    def speak(self) :
        print("I don't know what to say")

class Cat(Pet):
    
    def speak(self):
        print("meow")

class Dog(Pet):

    def speak(self):
        print("bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()
d = Cat("Jill", 14)
d.show()
d.speak()