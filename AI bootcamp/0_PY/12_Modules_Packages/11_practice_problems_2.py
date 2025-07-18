# Practice Problems - Part 2

print("=== PRACTICE PROBLEMS - PART 2 ===\n")

print("Problem 5: Create a module for file operations")

import os


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
        return os.path.exists(filename)

    @staticmethod
    def get_file_size(filename):
        try:
            return os.path.getsize(filename)
        except OSError:
            return -1

    @staticmethod
    def delete_file(filename):
        try:
            os.remove(filename)
            return f"Successfully deleted '{filename}'"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except Exception as e:
            return f"Error deleting file: {e}"

    @staticmethod
    def list_directory(path="."):
        try:
            return os.listdir(path)
        except Exception as e:
            return f"Error listing directory: {e}"

    @staticmethod
    def create_directory(dirname):
        try:
            os.makedirs(dirname, exist_ok=True)
            return f"Successfully created directory '{dirname}'"
        except Exception as e:
            return f"Error creating directory: {e}"


# Test file manager (simulated)
print("File operations (simulated):")
print(f"File exists: {FileManager.file_exists('test.txt')}")
print(FileManager.write_file("test.txt", "Hello, World!"))
print(FileManager.read_file("test.txt"))
print(FileManager.append_file("test.txt", "\nNew line"))
print(f"File size: {FileManager.get_file_size('test.txt')} bytes")
print(f"Directory contents: {FileManager.list_directory()[:5]}")  # Show first 5
print(FileManager.create_directory("test_dir"))
print(FileManager.delete_file("test.txt"))

print("\nProblem 6: Create a module for data validation")

import re


class DataValidator:
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone):
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

    @staticmethod
    def validate_url(url):
        pattern = r"^https?://[^\s/$.?#].[^\s]*$"
        return bool(re.match(pattern, url))

    @staticmethod
    def validate_credit_card(card_number):
        # Remove spaces and dashes
        clean_number = re.sub(r"\D", "", card_number)
        return len(clean_number) >= 13 and len(clean_number) <= 19

    @staticmethod
    def validate_postal_code(postal_code):
        # US postal code pattern
        pattern = r"^\d{5}(-\d{4})?$"
        return bool(re.match(pattern, postal_code))

    @staticmethod
    def validate_date(date_string):
        # Simple date validation (YYYY-MM-DD)
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(pattern, date_string):
            return False

        try:
            import datetime

            datetime.datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False


# Test data validation
test_emails = [
    "user@example.com",
    "invalid-email",
    "test@domain",
    "user.name@company.co.uk",
]
test_phones = ["123-456-7890", "1234567890", "123", "+1-555-123-4567"]
test_ages = [25, -5, 200, "twenty", 0, 150]
test_passwords = [
    "weak",
    "StrongPass1",
    "nouppercase1",
    "NOLOWERCASE1",
    "NoNumbers",
    "PerfectPass123",
]
test_urls = [
    "https://www.example.com",
    "http://localhost:8080",
    "invalid-url",
    "ftp://files.com",
]
test_cards = ["1234-5678-9012-3456", "123456789012345", "1234-5678-9012"]
test_postal_codes = ["12345", "12345-6789", "1234", "123456"]
test_dates = ["2023-01-01", "2023-13-01", "2023-01-32", "2023/01/01"]

print("Email validation:")
for email in test_emails:
    valid = DataValidator.validate_email(email)
    print(f"  {email}: {valid}")

print("\nPhone validation:")
for phone in test_phones:
    valid = DataValidator.validate_phone(phone)
    print(f"  {phone}: {valid}")

print("\nAge validation:")
for age in test_ages:
    valid = DataValidator.validate_age(age)
    print(f"  {age}: {valid}")

print("\nPassword validation:")
for password in test_passwords:
    valid, message = DataValidator.validate_password(password)
    print(f"  {password}: {message}")

print("\nURL validation:")
for url in test_urls:
    valid = DataValidator.validate_url(url)
    print(f"  {url}: {valid}")

print("\nCredit card validation:")
for card in test_cards:
    valid = DataValidator.validate_credit_card(card)
    print(f"  {card}: {valid}")

print("\nPostal code validation:")
for code in test_postal_codes:
    valid = DataValidator.validate_postal_code(code)
    print(f"  {code}: {valid}")

print("\nDate validation:")
for date in test_dates:
    valid = DataValidator.validate_date(date)
    print(f"  {date}: {valid}")

print("\nProblem 7: Create a module for caching")

import time
from collections import OrderedDict


class Cache:
    def __init__(self, max_size=100, ttl=300):  # 5 minutes default TTL
        self.max_size = max_size
        self.ttl = ttl
        self.cache = OrderedDict()
        self.timestamps = {}

    def get(self, key):
        if key in self.cache:
            # Check if item has expired
            if time.time() - self.timestamps[key] > self.ttl:
                self.delete(key)
                return None
            else:
                # Move to end (most recently used)
                self.cache.move_to_end(key)
                return self.cache[key]
        return None

    def set(self, key, value):
        if key in self.cache:
            # Update existing item
            self.cache.move_to_end(key)
        else:
            # Check if cache is full
            if len(self.cache) >= self.max_size:
                # Remove least recently used item
                oldest_key = next(iter(self.cache))
                self.delete(oldest_key)

        self.cache[key] = value
        self.timestamps[key] = time.time()

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.timestamps[key]

    def clear(self):
        self.cache.clear()
        self.timestamps.clear()

    def size(self):
        return len(self.cache)

    def keys(self):
        return list(self.cache.keys())

    def get_stats(self):
        return {
            "size": len(self.cache),
            "max_size": self.max_size,
            "ttl": self.ttl,
            "keys": list(self.cache.keys()),
        }


# Test cache
print("Testing cache functionality:")
cache = Cache(max_size=3, ttl=10)  # 10 seconds TTL

cache.set("user:1", {"name": "Alice", "age": 25})
cache.set("user:2", {"name": "Bob", "age": 30})
cache.set("user:3", {"name": "Charlie", "age": 35})

print(f"Cache size: {cache.size()}")
print(f"User 1: {cache.get('user:1')}")

# This will evict the oldest item
cache.set("user:4", {"name": "David", "age": 40})
print(f"Cache size after adding user 4: {cache.size()}")
print(f"User 1 (should be None): {cache.get('user:1')}")
print(f"User 2: {cache.get('user:2')}")

print(f"Cache stats: {cache.get_stats()}")

print("\nProblem 8: Create a module for rate limiting")

import time
from collections import defaultdict


class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)

    def is_allowed(self, identifier):
        now = time.time()
        user_requests = self.requests[identifier]

        # Remove old requests outside the time window
        user_requests[:] = [
            req_time for req_time in user_requests if now - req_time < self.time_window
        ]

        # Check if user has exceeded the limit
        if len(user_requests) >= self.max_requests:
            return False

        # Add current request
        user_requests.append(now)
        return True

    def get_remaining_requests(self, identifier):
        now = time.time()
        user_requests = self.requests[identifier]

        # Remove old requests
        user_requests[:] = [
            req_time for req_time in user_requests if now - req_time < self.time_window
        ]

        return max(0, self.max_requests - len(user_requests))

    def reset(self, identifier):
        if identifier in self.requests:
            del self.requests[identifier]

    def get_stats(self):
        return {
            "max_requests": self.max_requests,
            "time_window": self.time_window,
            "active_users": len(self.requests),
        }


# Test rate limiter
print("Testing rate limiter:")
limiter = RateLimiter(max_requests=3, time_window=10)  # 3 requests per 10 seconds

user_id = "user123"

for i in range(5):
    allowed = limiter.is_allowed(user_id)
    remaining = limiter.get_remaining_requests(user_id)
    print(f"Request {i+1}: Allowed={allowed}, Remaining={remaining}")
    time.sleep(0.1)  # Small delay

print(f"Rate limiter stats: {limiter.get_stats()}")

print("\n=== END OF PRACTICE PROBLEMS - PART 2 ===")
