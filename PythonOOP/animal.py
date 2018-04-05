class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayhealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def displayhealth(self):
        super(Dragon, self).displayhealth()
        print "I am a Dragon"
    def fly(self):
        self.health -= 10
        return self

myAnimal = Animal ("Rupert", 50)
myAnimal.displayhealth()
myAnimal.pet()
myAnimal.fly()

myDog = Dog("Doggo", 30)
myDog.fly()