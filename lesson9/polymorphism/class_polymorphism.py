class Dog:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound: Woof!")

class Cat:
    def __init__(self, name):
            self.name = name

    def sound(self):
            print(f"{self.name} makes the sound: meow!")



class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Chirp!")



dog = Dog("buddy")
cat = Cat("whiskers")
bird = Bird("Tweetie")


for animal in (dog,cat,bird):
    animal.sound()
