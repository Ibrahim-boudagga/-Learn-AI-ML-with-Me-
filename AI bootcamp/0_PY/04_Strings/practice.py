# Python Strings Practice

print("=== PYTHON STRINGS PRACTICE ===\n")

# 1. String Creation and Basic Operations
print("1. String Creation and Basic Operations:")
name = "Python Programming"
print(f"Original string: '{name}'")
print(f"Length: {len(name)}")
print(f"First character: '{name[0]}'")
print(f"Last character: '{name[-1]}'")
print(f"Characters 7-10: '{name[7:10]}'")
print()

# 2. String Methods - Case Conversion
print("2. String Methods - Case Conversion:")
text = "Hello World Python"
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Swap case: '{text.swapcase()}'")
print()

# 3. String Search and Replace
print("3. String Search and Replace:")
sentence = "Python is awesome and Python is powerful"
print(f"Original: '{sentence}'")
print(f"Find 'Python': {sentence.find('Python')}")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Replace 'Python' with 'Java': '{sentence.replace('Python', 'Java')}'")
print(f"Replace first 'Python' only: '{sentence.replace('Python', 'Java', 1)}'")
print()

# 4. String Splitting and Joining
print("4. String Splitting and Joining:")
csv_data = "apple,banana,orange,grape"
print(f"CSV data: '{csv_data}'")
fruits = csv_data.split(",")
print(f"Split fruits: {fruits}")

words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"Joined words: '{joined}'")

# Split by multiple delimiters
text_with_spaces = "apple, banana; orange. grape"
import re

cleaned = re.split(r"[,;\s.]+", text_with_spaces)
print(f"Split by multiple delimiters: {cleaned}")
print()

# 5. String Formatting
print("5. String Formatting:")
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

# 6. String Validation
print("6. String Validation:")
test_strings = ["Hello123", "Hello", "123", "   ", "Hello World", "hello"]

for s in test_strings:
    print(f"'{s}':")
    print(f"  isalpha(): {s.isalpha()}")
    print(f"  isdigit(): {s.isdigit()}")
    print(f"  isalnum(): {s.isalnum()}")
    print(f"  isspace(): {s.isspace()}")
    print(f"  startswith('Hello'): {s.startswith('Hello')}")
    print(f"  endswith('World'): {s.endswith('World')}")
    print()

# 7. String Manipulation
print("7. String Manipulation:")
text = "   Python Programming   "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lstrip: '{text.lstrip()}'")
print(f"Rstrip: '{text.rstrip()}'")

# Padding
name = "John"
print(f"Original: '{name}'")
print(f"Center (10): '{name.center(10)}'")
print(f"Left justify (10): '{name.ljust(10)}'")
print(f"Right justify (10): '{name.rjust(10)}'")
print()

# 8. Practice Problems
print("8. Practice Problems:")


# Problem 1: Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


text = "Hello World Python"
vowel_count = count_vowels(text)
print(f"Vowels in '{text}': {vowel_count}")


# Problem 2: Reverse words in a sentence
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


sentence = "Python is awesome"
reversed_sentence = reverse_words(sentence)
print(f"Original: '{sentence}'")
print(f"Reversed words: '{reversed_sentence}'")


# Problem 3: Check if string is palindrome
def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


test_palindromes = ["racecar", "A man a plan a canal Panama", "hello", "Madam"]
for word in test_palindromes:
    result = is_palindrome(word)
    print(f"'{word}' is palindrome: {result}")


# Problem 4: Extract domain from email
def extract_domain(email):
    if "@" in email:
        return email.split("@")[1]
    return None


emails = ["user@example.com", "admin@company.org", "invalid-email"]
for email in emails:
    domain = extract_domain(email)
    print(f"Email: {email} -> Domain: {domain}")


# Problem 5: Format phone number
def format_phone_number(phone):
    # Remove all non-digits
    digits = "".join(char for char in phone if char.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone


phone_numbers = ["1234567890", "123-456-7890", "(123) 456-7890"]
for phone in phone_numbers:
    formatted = format_phone_number(phone)
    print(f"Original: {phone} -> Formatted: {formatted}")

print("\n=== END OF PRACTICE ===")
