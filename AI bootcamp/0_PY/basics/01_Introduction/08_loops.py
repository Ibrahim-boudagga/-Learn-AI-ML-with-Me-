# Loops

print("=== LOOPS ===\n")

print("For loop (range 5):")
for i in range(5):
    print(f"  Count: {i}")

print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  While count: {count}")
    count += 1

print("\nFor loop with list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")
print()

# for loops iterate over sequences (lists, strings, range)
# while loops repeat while condition is True
# range() creates a sequence of numbers
