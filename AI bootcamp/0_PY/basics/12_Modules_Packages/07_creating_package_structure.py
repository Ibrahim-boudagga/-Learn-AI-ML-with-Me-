# Creating Package Structure

print("=== CREATING PACKAGE STRUCTURE ===\n")

print("1. Basic Package Structure:")


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

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history.copy()

    def clear_history(self):
        self.history.clear()


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


# Using the package
print("2. Using Calculator Package:")
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"History: {calc.get_history()}")

print("\n3. Using StringUtils Package:")
text = "Hello World"
print(f"Original text: '{text}'")
print(f"Reversed: '{StringUtils.reverse(text)}'")
print(f"Vowel count: {StringUtils.count_vowels(text)}")
print(f"Is palindrome: {StringUtils.is_palindrome(text)}")
print(f"Capitalized: '{StringUtils.capitalize_words(text)}'")
print(f"No duplicates: '{StringUtils.remove_duplicates(text)}'")

print("\n4. Package with Configuration:")


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

print("\n5. Package with Logger:")


class Logger:
    _instance = None
    logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message, level="INFO"):
        import datetime

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self):
        return self.logs.copy()

    def clear_logs(self):
        self.logs.clear()


# Test singleton logger
logger1 = Logger()
logger2 = Logger()
print(f"Same logger instance: {logger1 is logger2}")

logger1.log("Application started")
logger2.log("User logged in", "INFO")
logger1.log("Error occurred", "ERROR")

print(f"All logs: {logger1.get_logs()}")

print("\n6. Package with Data Formatters:")


class DataFormatter:
    def format_data(self, data):
        pass


class JSONFormatter(DataFormatter):
    def format_data(self, data):
        import json

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

print("\n7. Package with Plugin System:")


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

    def remove_plugin(self, name):
        if name in self.plugins:
            del self.plugins[name]


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

print("\n8. Package with File Manager:")


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

print("\n9. Package with Data Validator:")


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

print("\n=== END OF CREATING PACKAGE STRUCTURE ===")
