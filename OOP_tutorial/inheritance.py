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
    def __init__(self, name, age, color) -> None:
        self.color = color
        super().__init__(name, age)

    def speak(self):
        print("bark")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}" )

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()
d = Dog("Jill", 14, "brown")
d.show()
d.speak()