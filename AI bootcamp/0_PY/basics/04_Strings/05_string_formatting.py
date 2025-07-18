# String Formatting

print("=== STRING FORMATTING ===\n")

name = "Alice"
age = 25
height = 1.75

# f-strings
print(f"f-string: Hello, my name is {name} and I am {age} years old")
print(f"f-string with formatting: I am {height:.2f}m tall")

# .format() method
message = "Hello, my name is {} and I am {} years old".format(name, age)
print(f".format(): {message}")

# Named placeholders
message = "Hello, my name is {n} and I am {a} years old".format(n=name, a=age)
print(f"Named placeholders: {message}")
print()

# String formatting methods:
# f-strings (Python 3.6+) : Most readable and efficient
# .format() : Flexible formatting with placeholders
# % operator : Old-style formatting (C-style)
# str() : Convert objects to string representation
