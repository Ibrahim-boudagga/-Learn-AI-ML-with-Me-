# Creating and Using Simple Modules

print("=== CREATING AND USING SIMPLE MODULES ===\n")


# Simulating a math_utils module
class MathUtils:
    PI = 3.14159
    E = 2.71828

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(base, exponent):
        return base**exponent

    @staticmethod
    def square_root(number):
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number**0.5


# Using the module
print("1. Basic math operations:")
print(f"Add: {MathUtils.add(5, 3)}")
print(f"Subtract: {MathUtils.subtract(10, 4)}")
print(f"Multiply: {MathUtils.multiply(6, 7)}")
print(f"Divide: {MathUtils.divide(15, 3)}")

print("\n2. Constants:")
print(f"PI: {MathUtils.PI}")
print(f"E: {MathUtils.E}")

print("\n3. Advanced operations:")
print(f"Power: {MathUtils.power(2, 8)}")
print(f"Square root: {MathUtils.square_root(16)}")

print("\n4. Error handling:")
try:
    result = MathUtils.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

try:
    result = MathUtils.square_root(-4)
except ValueError as e:
    print(f"Error: {e}")

print("\n5. Module-like class with more functionality:")


class StringUtils:
    @staticmethod
    def reverse(text):
        return text[::-1]

    @staticmethod
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)

    @staticmethod
    def is_palindrome(text):
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

    @staticmethod
    def capitalize_words(text):
        return " ".join(word.capitalize() for word in text.split())

    @staticmethod
    def remove_duplicates(text):
        seen = set()
        result = ""
        for char in text:
            if char not in seen:
                result += char
                seen.add(char)
        return result


# Using StringUtils module
test_text = "hello world"
print(f"Original text: '{test_text}'")
print(f"Reversed: '{StringUtils.reverse(test_text)}'")
print(f"Vowel count: {StringUtils.count_vowels(test_text)}")
print(f"Is palindrome: {StringUtils.is_palindrome(test_text)}")
print(f"Capitalized: '{StringUtils.capitalize_words(test_text)}'")
print(f"No duplicates: '{StringUtils.remove_duplicates(test_text)}'")

print("\n6. Module with configuration:")


class Config:
    DEBUG = True
    DATABASE_URL = "sqlite:///app.db"
    SECRET_KEY = "my-secret-key"
    MAX_CONNECTIONS = 100

    @classmethod
    def get_database_url(cls):
        return cls.DATABASE_URL

    @classmethod
    def is_debug(cls):
        return cls.DEBUG

    @classmethod
    def get_max_connections(cls):
        return cls.MAX_CONNECTIONS

    @classmethod
    def set_debug(cls, value):
        cls.DEBUG = value


print(f"Database URL: {Config.get_database_url()}")
print(f"Debug mode: {Config.is_debug()}")
print(f"Max connections: {Config.get_max_connections()}")

Config.set_debug(False)
print(f"Debug mode after change: {Config.is_debug()}")

print("\n=== END OF CREATING SIMPLE MODULES ===")
