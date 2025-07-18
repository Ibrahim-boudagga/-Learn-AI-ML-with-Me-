# Practice Problems - Part 2

print("=== PRACTICE PROBLEMS - PART 2 ===\n")


# Problem 8: Check if a string is palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[-(i + 1)]:
            return False
    return True


test_palindromes = ["racecar", "hello", "A man a plan a canal Panama"]
print("8. Palindrome check:")
for word in test_palindromes:
    palindrome = is_palindrome(word)
    print(f"  '{word}' is palindrome: {palindrome}")


# Problem 9: Generate multiplication table
def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:3}", end="")
        print()  # New line


print("\n9. Multiplication table (5x5):")
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
print(f"\n10. Factors of {test_number}: {factors}")


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
print("\n11. Perfect number check:")
for num in test_perfect:
    perfect = is_perfect(num)
    print(f"  {num} is perfect: {perfect}")


# Problem 12: Generate prime numbers up to n
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):  # Using is_prime from previous file
            primes.append(num)
    return primes


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


limit = 20
prime_numbers = generate_primes(limit)
print(f"\n12. Prime numbers up to {limit}: {prime_numbers}")


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
print(f"\n13. Longest word in '{test_sentence}': '{longest_word}'")


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
print(f"\n14. Word frequency in '{test_text}': {word_frequency}")


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
print("\n15. Armstrong number check:")
for num in test_armstrong:
    armstrong = is_armstrong(num)
    print(f"  {num} is Armstrong number: {armstrong}")

print("\n=== END OF PRACTICE PROBLEMS - PART 2 ===")
