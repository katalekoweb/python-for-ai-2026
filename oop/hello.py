class Dog:
    def __init__(self, name, breed="None"):
        self.name = name
        self.breed = breed
        
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
jerry = Dog(name='Jerry', breed='Labrador')
print(jerry.name)

dog = Dog(name="Tim")
print(dog.name)