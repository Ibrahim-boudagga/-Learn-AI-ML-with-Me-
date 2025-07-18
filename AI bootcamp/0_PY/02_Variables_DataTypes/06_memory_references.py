# Memory and References

print("=== MEMORY AND REFERENCES ===\n")

# Object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)
print(f"a == b: {a == b}")  # True (same values)

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print()

# 'is' checks object identity (same memory location)
# '==' checks value equality
# id() returns the memory address of an object
# Variables are references to objects in memory
