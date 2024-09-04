"""
Define parent class animal:
Name, age
make_sound()
Define dog and cat subclasses 
Implement makesound for cat and dog
Test
Make 2 dog objects and a cat
Make a streetcat class that inherits from cat with different sound

"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}- {self.age}"

    def make_sound(self, sound):
        self.sound = sound


class Dog(Animal):

    def is_pure(self, is_pure):
        self.pure = is_pure
        if self.pure:
            print(f"dog: {self.name}, is pure race")
        else:
            print(f"dog: {self.name}, is not pure race")

    def make_sound(self, sound="woof"):
        self.sound = sound
        print(f"dog: {self.name}- {self.sound}")


class Cat(Animal):

    def is_ear_cat(self, is_ear_cat):
        self.is_ear_cat = is_ear_cat
        if self.is_ear_cat:
            print(f"cat: {self.name}, is ear cat")
        else:
            print(f"cat: {self.name}, is not ear cat")

    def make_sound(self, sound="Miaauuu"):
        self.sound = sound
        print(f"cat: {self.name}- {self.sound}")


class Street_cat(Cat):
    def make_sound(self, sound="Miahuhuhu"):
        self.sound = sound
        print(f"street cat: {self.name}- {self.sound}")
