# Recursion

print("=== RECURSION ===\n")


# Basic factorial function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Countdown function
def count_down(n):
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    count_down(n - 1)


# Sum of list recursively
def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


# Find maximum in list recursively
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return max(numbers[0], numbers[1])

    mid = len(numbers) // 2
    left_max = find_max(numbers[:mid])
    right_max = find_max(numbers[mid:])
    return max(left_max, right_max)


# Reverse string recursively
def reverse_string(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])


# Check if palindrome recursively
def is_palindrome_recursive(text):
    cleaned = text.lower().replace(" ", "")
    if len(cleaned) <= 1:
        return True
    if cleaned[0] != cleaned[-1]:
        return False
    return is_palindrome_recursive(cleaned[1:-1])


# Binary search recursively
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


# Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Generate all permutations recursively
def generate_permutations(items):
    if len(items) <= 1:
        return [items]

    permutations = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1 :]

        for perm in generate_permutations(remaining):
            permutations.append([current] + perm)

    return permutations


# Testing recursion
print("1. Factorial:")
for i in range(1, 6):
    result = factorial(i)
    print(f"Factorial of {i}: {result}")

print("\n2. Fibonacci sequence:")
for i in range(8):
    result = fibonacci(i)
    print(f"Fibonacci({i}): {result}")

print("\n3. Countdown:")
count_down(3)

print("\n4. Sum of list:")
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(f"Sum of {numbers}: {result}")

print("\n5. Find maximum:")
max_num = find_max(numbers)
print(f"Maximum in {numbers}: {max_num}")

print("\n6. Reverse string:")
text = "Python"
reversed_text = reverse_string(text)
print(f"'{text}' reversed: '{reversed_text}'")

print("\n7. Palindrome check:")
test_palindromes = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_palindromes:
    palindrome = is_palindrome_recursive(word)
    print(f"'{word}' is palindrome: {palindrome}")

print("\n8. Binary search:")
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(sorted_array, target)
print(f"Index of {target} in {sorted_array}: {index}")

print("\n9. Tower of Hanoi (3 disks):")
tower_of_hanoi(3, "A", "B", "C")

print("\n10. Generate permutations:")
test_items = [1, 2, 3]
permutations = generate_permutations(test_items)
print(f"Permutations of {test_items}: {permutations}")

print("\n=== END OF RECURSION ===")
