# Practice Problems

print("=== PRACTICE PROBLEMS ===\n")


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

print("\n=== END OF PRACTICE PROBLEMS ===")
