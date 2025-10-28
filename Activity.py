class Dog:
    def __init__(dog, name, age):  
        dog.name = name
        dog.age = age
    
    def bark(dog):
        print("Woof! Woof!")
    
    def celebrateBirthday(dog):  
        dog.age += 1
        print(f"Happy Birthday! {dog.name} is now {dog.age} years old.")

    def getInfo(dog):  
        return f"Dog Name: {dog.name}, Age: {dog.age}"


name = input("Enter the dog's name: ")
age = int(input("Enter the dog's age: "))
dog = Dog(name, age)  

dog.bark()
dog.celebrateBirthday()
print(dog.getInfo())