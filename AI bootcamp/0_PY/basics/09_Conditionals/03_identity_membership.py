# Identity and Membership

print("=== IDENTITY AND MEMBERSHIP ===\n")

# 3. Identity and Membership
print("3. Identity and Membership:")
# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}, y = {y}, z = x")
print(f"x is y: {x is y}")
print(f"x is z: {x is z}")
print(f"x == y: {x == y}")

# Membership operators
fruits = ["apple", "banana", "orange"]
print(f"\nfruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
print()

# Additional identity and membership examples
print("More identity and membership examples:")

# Identity with different types
a = 5
b = 5
c = a
print(f"a = {a}, b = {b}, c = a")
print(f"a is b: {a is b}")  # True (same object for small integers)
print(f"a is c: {a is c}")  # True
print(f"a == b: {a == b}")  # True

# Identity with strings
str1 = "hello"
str2 = "hello"
str3 = str1
print(f"\nstr1 = '{str1}', str2 = '{str2}', str3 = str1")
print(f"str1 is str2: {str1 is str2}")  # May be True (string interning)
print(f"str1 is str3: {str1 is str3}")  # True
print(f"str1 == str2: {str1 == str2}")  # True

# Membership with different containers
numbers = [1, 2, 3, 4, 5]
print(f"\nnumbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"6 not in numbers: {6 not in numbers}")

# Membership with strings
text = "Python programming"
print(f"\ntext = '{text}'")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# Membership with sets
my_set = {1, 2, 3, 4}
print(f"\nmy_set = {my_set}")
print(f"2 in my_set: {2 in my_set}")
print(f"5 not in my_set: {5 not in my_set}")

# Membership with dictionaries
person = {"name": "Alice", "age": 25}
print(f"\nperson = {person}")
print(f"'name' in person: {'name' in person}")
print(f"'city' not in person: {'city' not in person}")

print("\n=== END ===")
