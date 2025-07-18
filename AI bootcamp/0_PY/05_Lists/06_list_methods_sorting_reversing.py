# List Methods - Sorting and Reversing

print("=== LIST METHODS - SORTING AND REVERSING ===\n")

# Sample data
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# sort() - sorts in place
numbers.sort()
print(f"After sort(): {numbers}")

# sort() with reverse=True
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# reverse() - reverses in place
numbers.reverse()
print(f"After reverse(): {numbers}")

# Using sorted() function - returns new list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"\nOriginal: {original}")
print(f"Sorted (new list): {sorted_list}")

# sorted() with reverse=True
reverse_sorted = sorted(original, reverse=True)
print(f"Reverse sorted: {reverse_sorted}")

# Sorting strings
fruits = ["banana", "apple", "cherry", "date"]
print(f"\nFruits: {fruits}")
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Sorting with key function
words = ["cat", "dog", "elephant", "ant"]
print(f"\nWords: {words}")
words.sort(key=len)  # Sort by length
print(f"Sorted by length: {words}")

# Custom sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(f"\nStudents: {students}")
students.sort(key=lambda x: x[1], reverse=True)  # Sort by grade
print(f"Sorted by grade: {students}")

print("\n=== END ===")
