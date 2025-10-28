class Dog:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof! Woof!")
    
    def celebrateBirthday(self):  
        self.age += 1
        print(f"Happy Birthday! {self.name} is now {self.age} years old.")
    
    def getInfo(self):  
        return f"Dog Name: {self.name}, Age: {self.age}"


name = input("Enter the dog's name: ")
age = int(input("Enter the dog's age: "))
dog = Dog(name, age)  

dog.bark()
dog.celebrateBirthday()
print(dog.getInfo())