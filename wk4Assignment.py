class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(
            "I am called {self.name} , a {self.gender} of {self.age} years old.")


mtu1 = Person("Jane", 10, "Female")
mtu1.introduce()
