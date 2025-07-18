# Named Tuples

print("=== NAMED TUPLES ===\n")

# 7. Named Tuples
print("7. Named Tuples:")
from collections import namedtuple

# Creating a named tuple
Person = namedtuple("Person", ["name", "age", "city"])

# Creating instances
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "London")

print(f"Person 1: {person1.name} is {person1.age} years old from {person1.city}")
print(f"Person 2: {person2.name} is {person2.age} years old from {person2.city}")

# Accessing by index
print(f"Person 1 by index: {person1[0]} is {person1[1]} years old from {person1[2]}")

# Converting to dictionary
person_dict = person1._asdict()
print(f"Person 1 as dictionary: {person_dict}")
print()

# Additional named tuple examples
print("More named tuple examples:")

# Point named tuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)
p2 = Point(0, 0)
print(f"Point 1: ({p1.x}, {p1.y})")
print(f"Point 2: ({p2.x}, {p2.y})")

# RGB Color named tuple
Color = namedtuple("Color", ["red", "green", "blue"])
white = Color(255, 255, 255)
black = Color(0, 0, 0)
red = Color(255, 0, 0)
print(f"White: RGB({white.red}, {white.green}, {white.blue})")
print(f"Black: RGB({black.red}, {black.green}, {black.blue})")
print(f"Red: RGB({red.red}, {red.green}, {red.blue})")

# Student named tuple
Student = namedtuple("Student", ["name", "grade", "gpa"])
student1 = Student("John", "A", 3.8)
student2 = Student("Jane", "B", 3.2)
print(f"Student 1: {student1.name}, Grade: {student1.grade}, GPA: {student1.gpa}")
print(f"Student 2: {student2.name}, Grade: {student2.grade}, GPA: {student2.gpa}")

# Creating from iterable
values = ["Charlie", 35, "Paris"]
person3 = Person._make(values)
print(
    f"Person 3 from iterable: {person3.name} is {person3.age} years old from {person3.city}"
)

# Replacing fields
person4 = person1._replace(age=26, city="Boston")
print(
    f"Updated Person 1: {person4.name} is {person4.age} years old from {person4.city}"
)

print("\n=== END ===")
