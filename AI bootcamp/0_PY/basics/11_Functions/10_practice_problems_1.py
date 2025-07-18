# Practice Problems - Part 1

print("=== PRACTICE PROBLEMS - PART 1 ===\n")


# Problem 1: Calculate area of different shapes
def calculate_area(shape, *args):
    if shape == "rectangle":
        length, width = args
        return length * width
    elif shape == "circle":
        radius = args[0]
        import math

        return math.pi * radius**2
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height
    else:
        return "Unknown shape"


print("1. Calculate area of different shapes:")
print(f"Rectangle area (5x3): {calculate_area('rectangle', 5, 3)}")
print(f"Circle area (radius 4): {calculate_area('circle', 4):.2f}")
print(f"Triangle area (base 6, height 4): {calculate_area('triangle', 6, 4)}")


# Problem 2: Check if number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


test_primes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("\n2. Prime number check:")
for num in test_primes:
    prime = is_prime(num)
    print(f"{num} is prime: {prime}")


# Problem 3: Find GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


test_gcd = [(48, 18), (54, 24), (7, 13)]
print("\n3. GCD calculation:")
for a, b in test_gcd:
    result1 = gcd(a, b)
    result2 = gcd_recursive(a, b)
    print(f"GCD of {a} and {b}: {result1} (iterative), {result2} (recursive)")


# Problem 4: Convert decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary


def decimal_to_binary_recursive(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2)


test_decimals = [5, 10, 15, 255]
print("\n4. Decimal to binary conversion:")
for num in test_decimals:
    binary1 = decimal_to_binary(num)
    binary2 = decimal_to_binary_recursive(num)
    print(f"{num} in binary: {binary1} (iterative), {binary2} (recursive)")


# Problem 5: Check if string is palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def is_palindrome_recursive(text):
    cleaned = text.lower().replace(" ", "")
    if len(cleaned) <= 1:
        return True
    if cleaned[0] != cleaned[-1]:
        return False
    return is_palindrome_recursive(cleaned[1:-1])


test_palindromes = ["racecar", "hello", "A man a plan a canal Panama", "level"]
print("\n5. Palindrome check:")
for word in test_palindromes:
    palindrome1 = is_palindrome(word)
    palindrome2 = is_palindrome_recursive(word)
    print(
        f"'{word}' is palindrome: {palindrome1} (iterative), {palindrome2} (recursive)"
    )

print("\n=== END OF PRACTICE PROBLEMS - PART 1 ===")
