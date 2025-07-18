# Python Loops Practice

print("=== PYTHON LOOPS PRACTICE ===\n")

# 1. Basic For Loops
print("1. Basic For Loops:")
# Iterating over a range
for i in range(5):
    print(f"Count: {i}")

# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Iterating over a string
for char in "Python":
    print(f"Character: {char}")
print()

# 2. Range Function
print("2. Range Function:")
# range(stop)
print("range(5):")
for i in range(5):
    print(f"  {i}")

# range(start, stop)
print("\nrange(1, 6):")
for i in range(1, 6):
    print(f"  {i}")

# range(start, stop, step)
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}")

# Negative step
print("\nrange(5, 0, -1):")
for i in range(5, 0, -1):
    print(f"  {i}")
print()

# 3. Iterating Over Different Data Types
print("3. Iterating Over Different Data Types:")
# Lists
numbers = [1, 2, 3, 4, 5]
print("Doubling numbers:")
for num in numbers:
    print(f"  {num} * 2 = {num * 2}")

# Tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
print("\nCoordinates:")
for x, y in coordinates:
    print(f"  Point: ({x}, {y})")

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print("\nPerson details:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nPerson details (items):")
for key, value in person.items():
    print(f"  {key}: {value}")

# Sets
unique_numbers = {1, 2, 3, 4, 5}
print("\nUnique numbers:")
for num in unique_numbers:
    print(f"  {num}")
print()

# 4. While Loops
print("4. While Loops:")
# Simple counter
count = 0
print("Counting up:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# User input simulation
print("\nPassword check (simulated):")
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    if attempts == 2:  # Simulate correct password on second attempt
        print("  Access granted!")
        break
    else:
        print(f"  Wrong password. {max_attempts - attempts} attempts left")
print()

# 5. Loop Control Statements
print("5. Loop Control Statements:")
# Break statement
print("Break example:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

# Continue statement
print("\nContinue example (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# Pass statement
print("\nPass example:")
for i in range(5):
    if i < 3:
        pass  # Do nothing for now
    else:
        print(f"  Processing: {i}")
print()

# 6. Enumerate Function
print("6. Enumerate Function:")
fruits = ["apple", "banana", "orange"]
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nFruits with index starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")
print()

# 7. Zip Function
print("7. Zip Function:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

print("Combined data:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old from {city}")

# Different length lists
print("\nDifferent length lists:")
list1 = [1, 2, 3]
list2 = ["a", "b"]
for item1, item2 in zip(list1, list2):
    print(f"  {item1} - {item2}")
print()

# 8. List Comprehension
print("8. List Comprehension:")
# Basic list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
print(f"Word lengths: {word_lengths}")
print()

# 9. Common Loop Patterns
print("9. Common Loop Patterns:")

# Accumulator pattern
print("Accumulator - Sum numbers:")
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(f"  Total: {total}")

# Counter pattern
print("\nCounter - Count characters:")
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"  Character count: {char_count}")

# Filter pattern
print("\nFilter - Even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"  Even numbers: {even_numbers}")

# Map pattern
print("\nMap - Double numbers:")
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(f"  Doubled: {doubled}")
print()

# 10. Nested Loops
print("10. Nested Loops:")
# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")
    print()  # Empty line between tables

# Pattern printing
print("Pattern printing:")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line
print()

# 11. Practice Problems
print("11. Practice Problems:")


# Problem 1: Find the sum of all numbers from 1 to n
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = 10
result = sum_to_n(n)
print(f"Sum of numbers from 1 to {n}: {result}")


# Problem 2: Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


test_text = "Hello World Python"
vowel_count = count_vowels(test_text)
print(f"Vowels in '{test_text}': {vowel_count}")


# Problem 3: Find the largest number in a list
def find_max(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


test_numbers = [3, 7, 2, 9, 1, 8, 5]
max_number = find_max(test_numbers)
print(f"Maximum in {test_numbers}: {max_number}")


# Problem 4: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


test_primes = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_primes:
    prime = is_prime(num)
    print(f"{num} is prime: {prime}")


# Problem 5: Generate Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


fib_sequence = fibonacci(10)
print(f"Fibonacci sequence (first 10): {fib_sequence}")


# Problem 6: Reverse a string
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


test_string = "Python"
reversed_string = reverse_string(test_string)
print(f"'{test_string}' reversed: '{reversed_string}'")


# Problem 7: Find common elements between two lists
def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common_elements = find_common(list_a, list_b)
print(f"Common elements between {list_a} and {list_b}: {common_elements}")


# Problem 8: Check if a string is palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[-(i + 1)]:
            return False
    return True


test_palindromes = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_palindromes:
    palindrome = is_palindrome(word)
    print(f"'{word}' is palindrome: {palindrome}")


# Problem 9: Generate multiplication table
def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:3}", end="")
        print()  # New line


print("Multiplication table (5x5):")
print_multiplication_table(5)


# Problem 10: Find factors of a number
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


test_number = 12
factors = find_factors(test_number)
print(f"Factors of {test_number}: {factors}")


# Problem 11: Check if a number is perfect
def is_perfect(n):
    if n <= 1:
        return False

    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return sum(factors) == n


test_perfect = [6, 28, 12, 496]
for num in test_perfect:
    perfect = is_perfect(num)
    print(f"{num} is perfect: {perfect}")


# Problem 12: Generate prime numbers up to n
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


limit = 20
prime_numbers = generate_primes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")


# Problem 13: Find the longest word in a sentence
def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""

    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest


test_sentence = "Python is a great programming language"
longest_word = find_longest_word(test_sentence)
print(f"Longest word in '{test_sentence}': '{longest_word}'")


# Problem 14: Count word frequency
def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:")
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


test_text = "Python is great. Python is fun. Python is powerful."
word_frequency = count_words(test_text)
print(f"Word frequency in '{test_text}': {word_frequency}")


# Problem 15: Check if a number is armstrong number
def is_armstrong(n):
    if n < 0:
        return False

    # Convert to string to count digits
    num_str = str(n)
    num_digits = len(num_str)

    # Calculate sum of digits raised to power of number of digits
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits

    return total == n


test_armstrong = [153, 370, 371, 407, 123]
for num in test_armstrong:
    armstrong = is_armstrong(num)
    print(f"{num} is Armstrong number: {armstrong}")

print("\n=== END OF PRACTICE ===")
