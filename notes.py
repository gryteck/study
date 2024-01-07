class Animal:
    __name: int

    def __init__(self, name):
        self.__name = name

    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        return print("Meoww")


class Dog(Animal):
    def speak(self):
        return print("Woof")


Vasya = Cat('Vasya')
Aktos = Dog('Aktos')
Cheburawka = Animal('Cheburawka')

for i in (Vasya, Aktos, Cheburawka):
    i.speak()
