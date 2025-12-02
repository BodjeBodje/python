"""
Quiz: OOP Basics & Inheritance (Python)

Section A: Short Questions 
1. Define a class in your own words.
	A class is a blueprint or a template for creating objects.
	
2. What is an object? 
	An object is an instance of a class. It is a concrete entity created from the class blueprint, with its own unique set of data (attribute values) while still adhering to the structure defined by its class.
	
3. What is the purpose of the __init__ method in Python classes?
	The __init__ method is a special method in Python classes, also known as the constructor.
	
4. Explain the difference between a method and an attribute. 
	Attribute: An attribute is a variable associated with a class or an object that stores data. It represents a characteristic or a property of the object. For example, in a Dog class, name and age could be attributes.
	Method: A method is a function defined within a class that performs an action or defines a behavior for objects of that class. It operates on the object's attributes. For example, in a Dog class, bark() or eat() could be methods.
	
5. What does inheritance mean in object-oriented programming? 
Inheritance is a fundamental concept in object-oriented programming that allows a new class (the "child" or "derived" class) to inherit attributes and methods from an existing class (the "parent" or "base" class).

Section B: True or False
6. A class is an instance of an object.
    False
7. A child class can access methods defined in the parent class.
    True
8. Every class must have a constructor (__init__).
    False
9. Inheritance helps reduce code duplication.
    True
10. In Python, a subclass can override a method from its parent class.
    True
    
"""
# Section C: Code-Based Questions
# 11. What will the following code print?
class A:
    def greet(self):
        return "Hello from A"
class B(A):
    pass
        
obj = B()
print(obj.greet())#It's have print "Hello from A"

# Write a class called Car with:
# ● a constructor that takes brand and year
# ● a method info() that returns a string: "Toyota 2020" (as an example)
class Car:
    def __init__(self,brand, year):
        self.brand=brand
        self.year=year
    def info(self):
        print("Toyota 2020")

car1=Car(brand="Toyota", year="2020")
car1.info()

# 13. Consider this code:
#     What concept does the sound() method in Cat demonstrate?
class Animal:
    def sound(self):
        return "Some sound"
class Cat(Animal):
    def sound(self):
        return "Meow"
cat=Cat()
print(cat.sound())
# print(cat.sound1())

# 14. What is the output?
class Parent:
    x = 100
class Child(Parent): #What is Child(Parent) important in this inheriter
    x = 200
print(Parent.x)
print(Child.x)

# 15. Create a parent class Shape with a method area() that returns "Area not defined".
# Create two child classes:
# ● Circle that overrides area()
# ● Square that overrides area()
#You don’t need to calculate real areas—just return simple text like "Circle area".
class Shape:
    def area():
        return "Area not defined"
class Circle(Shape):
    def area(self):
        return "Circle area"
class Square(Shape):
    def area(self):
        return "Circle square"
child_class=Square()
print(child_class.area())
child_class=Circle()
print(child_class.area())

# Section D: Short Program
# 16. Write a short program that demonstrates:
# ● A base class Person
# ● Two subclasses Student and Teacher
# ● Each subclass overrides a method called role()
# The program should create one Student object and one Teacher object and print their roles.
class Person:
    def __init__(self, name: str,age:int):
        self.name=name
        self.age=age
    def person(self):
        print("{self.name} {self.age}")       

class Student(Person):
    def __init__(self,name:str,age:int,student_id:str,major:str):
        super().__init__(name, age)
        self.student_id=student_id
        self.major=major
    def student(self):
        return f"{self.name} {self.student_id} {self.major}"

class Teacher(Person):
    def __init__(self,name:str, age: int,employee_id:str,subject:str):
        super().__init__(name, age)
        self.employee_id=employee_id
        self.subject=subject
    def teacher(self):
        return (f"{self.name} {self.employee_id} {self.subject}")

student1=Student("Amadou", 20, "M0122", "business")
print(student1.student())
teacher1=Teacher("Aly", 20, "S0123","Math")
print(teacher1.teacher())