# Nested Loops

print("=== NESTED LOOPS ===\n")

# Multiplication table
print("1. Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")
    print()  # Empty line between tables

# Pattern printing
print("2. Pattern printing:")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line

# Number pyramid
print("\n3. Number pyramid:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Matrix creation
print("\n4. Matrix creation:")
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i + j)
    matrix.append(row)
print(f"  Matrix: {matrix}")

# Nested loops with conditions
print("\n5. Nested loops with conditions:")
for i in range(5):
    for j in range(5):
        if i == j:
            print("X", end=" ")
        else:
            print(".", end=" ")
    print()

# Triangular pattern
print("\n6. Triangular pattern:")
for i in range(5):
    for j in range(5 - i):
        print("*", end=" ")
    print()

# Number triangle
print("\n7. Number triangle:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# Checkerboard pattern
print("\n8. Checkerboard pattern:")
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

# Nested loops with break
print("\n9. Nested loops with break:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # Breaks inner loop only
        print(f"  ({i}, {j})")

# Nested loops with continue
print("\n10. Nested loops with continue:")
for i in range(3):
    for j in range(3):
        if i == j:
            continue  # Skip diagonal elements
        print(f"  ({i}, {j})")

print("\n=== END OF NESTED LOOPS ===")
