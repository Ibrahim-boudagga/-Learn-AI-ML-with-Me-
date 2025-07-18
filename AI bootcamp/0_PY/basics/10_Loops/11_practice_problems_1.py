# Practice Problems - Part 1

print("=== PRACTICE PROBLEMS - PART 1 ===\n")


# Problem 1: Find the sum of all numbers from 1 to n
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


n = 10
result = sum_to_n(n)
print(f"1. Sum of numbers from 1 to {n}: {result}")


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
print(f"\n2. Vowels in '{test_text}': {vowel_count}")


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
print(f"\n3. Maximum in {test_numbers}: {max_number}")


# Problem 4: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


test_primes = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n4. Prime number check:")
for num in test_primes:
    prime = is_prime(num)
    print(f"  {num} is prime: {prime}")


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
print(f"\n5. Fibonacci sequence (first 10): {fib_sequence}")


# Problem 6: Reverse a string
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


test_string = "Python"
reversed_string = reverse_string(test_string)
print(f"\n6. '{test_string}' reversed: '{reversed_string}'")


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
print(f"\n7. Common elements between {list_a} and {list_b}: {common_elements}")

print("\n=== END OF PRACTICE PROBLEMS - PART 1 ===")
