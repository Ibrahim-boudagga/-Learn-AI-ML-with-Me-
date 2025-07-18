# Python Modules and Packages Practice

print("=== PYTHON MODULES AND PACKAGES PRACTICE ===\n")

# 1. Creating and Using Simple Modules
print("1. Creating and Using Simple Modules:")


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


# Using the module
print(f"Add: {MathUtils.add(5, 3)}")
print(f"Subtract: {MathUtils.subtract(10, 4)}")
print(f"Multiply: {MathUtils.multiply(6, 7)}")
print(f"Divide: {MathUtils.divide(15, 3)}")
print(f"PI: {MathUtils.PI}")
print()

# 2. Built-in Modules
print("2. Built-in Modules:")

import math
import random
import datetime
import os

# Math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"PI: {math.pi}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")

# Random module
print(f"Random number (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")
print(f"Random float: {random.random():.3f}")

# Datetime module
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# OS module
print(f"Current directory: {os.getcwd()}")
print(f"Platform: {os.name}")
print()

# 3. Import Techniques
print("3. Import Techniques:")

# Import with alias
import math as m

print(f"Using alias - PI: {m.pi}")

# Import specific functions
from math import sqrt, pi

print(f"Direct import - sqrt(25): {sqrt(25)}")
print(f"Direct import - pi: {pi}")

# Import with conditional
try:
    import numpy as np

    print("NumPy is available")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr}")
except ImportError:
    print("NumPy is not available")
    arr = [1, 2, 3, 4, 5]
    print(f"Regular list: {arr}")
print()

# 4. Collections Module
print("4. Collections Module:")

from collections import defaultdict, Counter, namedtuple

# DefaultDict
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)
print(f"DefaultDict: {dict(d)}")

# Counter
text = "hello world"
char_count = Counter(text)
print(f"Character count: {dict(char_count)}")

word_count = Counter(text.split())
print(f"Word count: {dict(word_count)}")

# NamedTuple
Person = namedtuple("Person", ["name", "age", "city"])
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "London")
print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Person 1 name: {person1.name}")
print()

# 5. JSON Module
print("5. JSON Module:")

import json

# Python object to JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming"],
    "active": True,
}

json_string = json.dumps(data, indent=2)
print("Python to JSON:")
print(json_string)

# JSON to Python object
parsed_data = json.loads(json_string)
print(f"\nJSON to Python - name: {parsed_data['name']}")
print(f"JSON to Python - age: {parsed_data['age']}")

# Working with JSON files
sample_data = {"users": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]}

# Write to JSON file (simulated)
print(f"\nData to write to file: {sample_data}")

# Read from JSON file (simulated)
print(f"Data read from file: {sample_data}")
print()

# 6. Pickle Module
print("6. Pickle Module:")

import pickle

# Python object to pickle
data_to_pickle = {
    "name": "Alice",
    "scores": [85, 92, 78],
    "grades": {"math": "A", "science": "B"},
}

# Simulate pickling
pickled_data = pickle.dumps(data_to_pickle)
print(f"Pickled data size: {len(pickled_data)} bytes")

# Simulate unpickling
unpickled_data = pickle.loads(pickled_data)
print(f"Unpickled data: {unpickled_data}")
print()

# 7. Creating Package Structure
print("7. Creating Package Structure:")


# Simulating a package structure
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def get_history(self):
        return self.history


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


# Using the package
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"History: {calc.get_history()}")

text = "Hello World"
print(f"Reversed '{text}': '{StringUtils.reverse(text)}'")
print(f"Vowels in '{text}': {StringUtils.count_vowels(text)}")
print(f"'{text}' is palindrome: {StringUtils.is_palindrome(text)}")
print()

# 8. Module Attributes
print("8. Module Attributes:")

# Simulating module attributes
module_name = "__main__"
module_file = "practice.py"
module_doc = "This is a practice module for Python modules and packages"

print(f"Module name: {module_name}")
print(f"Module file: {module_file}")
print(f"Module doc: {module_doc}")

# Simulating __all__
__all__ = ["Calculator", "StringUtils", "MathUtils"]

print(f"All exports: {__all__}")
print()

# 9. Dynamic Imports
print("9. Dynamic Imports:")

import importlib

# Dynamic module import
module_name = "math"
math_module = importlib.import_module(module_name)
print(f"Imported module: {math_module}")
print(f"Module PI: {math_module.pi}")


# Dynamic function import
def import_function(module_name, function_name):
    module = importlib.import_module(module_name)
    return getattr(module, function_name)


sqrt_func = import_function("math", "sqrt")
print(f"Dynamic sqrt function: {sqrt_func(16)}")
print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Create a configuration module
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


print(f"Database URL: {Config.get_database_url()}")
print(f"Debug mode: {Config.is_debug()}")
print(f"Max connections: {Config.get_max_connections()}")


# Problem 2: Create a singleton logger
class Logger:
    _instance = None
    logs = []  # Class attribute to satisfy linter

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self):
        return self.logs.copy()


# Test singleton logger
logger1 = Logger()
logger2 = Logger()
print(f"Same logger instance: {logger1 is logger2}")

logger1.log("Application started")
logger2.log("User logged in", "INFO")
logger1.log("Error occurred", "ERROR")

print(f"All logs: {logger1.get_logs()}")


# Problem 3: Create a factory for different data formats
class DataFormatter:
    def format_data(self, data):
        pass


class JSONFormatter(DataFormatter):
    def format_data(self, data):
        return json.dumps(data, indent=2)


class XMLFormatter(DataFormatter):
    def format_data(self, data):
        # Simplified XML formatting
        xml = "<data>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</data>"
        return xml


class CSVFormatter(DataFormatter):
    def format_data(self, data):
        if not data:
            return ""
        headers = list(data[0].keys())
        csv = ",".join(headers) + "\n"
        for row in data:
            csv += ",".join(str(row[header]) for header in headers) + "\n"
        return csv


def create_formatter(format_type):
    formatters = {"json": JSONFormatter, "xml": XMLFormatter, "csv": CSVFormatter}

    if format_type in formatters:
        return formatters[format_type]()
    else:
        raise ValueError(f"Unknown format: {format_type}")


# Test formatters
test_data = {"name": "Alice", "age": 25, "city": "New York"}
test_list_data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]

for format_type in ["json", "xml", "csv"]:
    try:
        formatter = create_formatter(format_type)
        if format_type == "csv":
            result = formatter.format_data(test_list_data)
        else:
            result = formatter.format_data(test_data)
        print(f"{format_type.upper()} format:")
        print(result)
        print()
    except Exception as e:
        print(f"Error with {format_type}: {e}")


# Problem 4: Create a plugin system
class Plugin:
    def execute(self, data):
        pass


class UppercasePlugin(Plugin):
    def execute(self, data):
        if isinstance(data, str):
            return data.upper()
        return data


class ReversePlugin(Plugin):
    def execute(self, data):
        if isinstance(data, str):
            return data[::-1]
        return data


class NumberPlugin(Plugin):
    def execute(self, data):
        if isinstance(data, (int, float)):
            return data * 2
        return data


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def execute_plugin(self, name, data):
        if name in self.plugins:
            return self.plugins[name].execute(data)
        else:
            raise ValueError(f"Plugin '{name}' not found")

    def list_plugins(self):
        return list(self.plugins.keys())


# Test plugin system
manager = PluginManager()
manager.register_plugin("uppercase", UppercasePlugin())
manager.register_plugin("reverse", ReversePlugin())
manager.register_plugin("number", NumberPlugin())

test_string = "hello world"
test_number = 42

print(f"Original string: {test_string}")
print(f"Uppercase: {manager.execute_plugin('uppercase', test_string)}")
print(f"Reverse: {manager.execute_plugin('reverse', test_string)}")

print(f"Original number: {test_number}")
print(f"Doubled: {manager.execute_plugin('number', test_number)}")

print(f"Available plugins: {manager.list_plugins()}")


# Problem 5: Create a module for file operations
class FileManager:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    def write_file(filename, content):
        try:
            with open(filename, "w") as f:
                f.write(content)
            return f"Successfully wrote to '{filename}'"
        except Exception as e:
            return f"Error writing file: {e}"

    @staticmethod
    def append_file(filename, content):
        try:
            with open(filename, "a") as f:
                f.write(content)
            return f"Successfully appended to '{filename}'"
        except Exception as e:
            return f"Error appending to file: {e}"

    @staticmethod
    def file_exists(filename):
        import os

        return os.path.exists(filename)


# Test file manager (simulated)
print("File operations (simulated):")
print(FileManager.file_exists("test.txt"))
print(FileManager.write_file("test.txt", "Hello, World!"))
print(FileManager.read_file("test.txt"))
print(FileManager.append_file("test.txt", "\nNew line"))


# Problem 6: Create a module for data validation
class DataValidator:
    @staticmethod
    def validate_email(email):
        import re

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone):
        import re

        # Remove all non-digit characters
        digits = re.sub(r"\D", "", phone)
        return len(digits) >= 10

    @staticmethod
    def validate_age(age):
        return isinstance(age, int) and 0 <= age <= 150

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False, "Password must be at least 8 characters"

        if not any(c.isupper() for c in password):
            return False, "Password must contain uppercase letter"

        if not any(c.islower() for c in password):
            return False, "Password must contain lowercase letter"

        if not any(c.isdigit() for c in password):
            return False, "Password must contain digit"

        return True, "Password is valid"


# Test data validation
test_emails = ["user@example.com", "invalid-email", "test@domain"]
test_phones = ["123-456-7890", "1234567890", "123"]
test_ages = [25, -5, 200, "twenty"]
test_passwords = ["weak", "StrongPass1", "nouppercase1", "NOLOWERCASE1"]

print("Email validation:")
for email in test_emails:
    valid = DataValidator.validate_email(email)
    print(f"  {email}: {valid}")

print("Phone validation:")
for phone in test_phones:
    valid = DataValidator.validate_phone(phone)
    print(f"  {phone}: {valid}")

print("Age validation:")
for age in test_ages:
    valid = DataValidator.validate_age(age)
    print(f"  {age}: {valid}")

print("Password validation:")
for password in test_passwords:
    valid, message = DataValidator.validate_password(password)
    print(f"  {password}: {message}")

print("\n=== END OF PRACTICE ===")
