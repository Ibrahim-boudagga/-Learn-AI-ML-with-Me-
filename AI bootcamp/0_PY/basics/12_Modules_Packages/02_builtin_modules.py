# Built-in Modules

print("=== BUILT-IN MODULES ===\n")

# Math module
import math

print("1. Math Module:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"PI: {math.pi}")
print(f"E: {math.e}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Absolute value of -5: {math.fabs(-5)}")
print(f"Power 2^8: {math.pow(2, 8)}")
print(f"Logarithm base 10 of 100: {math.log10(100)}")
print(f"Sine of 90 degrees: {math.sin(math.radians(90))}")

# Random module
import random

print("\n2. Random Module:")
print(f"Random number (1-10): {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random():.3f}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")
print(f"Random sample: {random.sample(range(1, 50), 6)}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Datetime module
import datetime

print("\n3. Datetime Module:")
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

# Date arithmetic
tomorrow = now + datetime.timedelta(days=1)
yesterday = now - datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")

# OS module
import os

print("\n4. OS Module:")
print(f"Current directory: {os.getcwd()}")
print(f"Platform: {os.name}")

# Show some environment variables
env_vars = dict(os.environ)
env_sample = {k: v for i, (k, v) in enumerate(env_vars.items()) if i < 3}
print(f"Environment variables sample: {env_sample}")

# List directory contents
dir_contents = os.listdir(".")
print(f"Current directory contents (first 5): {dir_contents[:5]}")

# Sys module
import sys

print("\n5. Sys Module:")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")
print(f"Path (first 3): {sys.path[:3]}")

# Collections module
from collections import defaultdict, Counter, namedtuple, deque

print("\n6. Collections Module:")

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

# Deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(f"Deque: {dq}")

# Re module
import re

print("\n7. Re Module (Regular Expressions):")
text = "Hello World 123"
print(f"Original text: {text}")

# Find all digits
digits = re.findall(r"\d+", text)
print(f"Digits found: {digits}")

# Find all words
words = re.findall(r"\b\w+\b", text)
print(f"Words found: {words}")

# Replace
replaced = re.sub(r"\d+", "XXX", text)
print(f"After replacement: {replaced}")

# Match pattern
email = "user@example.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
is_valid_email = bool(re.match(pattern, email))
print(f"Valid email: {is_valid_email}")

# JSON module
import json

print("\n8. JSON Module:")
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming"],
    "active": True,
}

# Python object to JSON
json_string = json.dumps(data, indent=2)
print("Python to JSON:")
print(json_string)

# JSON to Python object
parsed_data = json.loads(json_string)
print(f"\nJSON to Python - name: {parsed_data['name']}")
print(f"JSON to Python - age: {parsed_data['age']}")

# Pickle module
import pickle

print("\n9. Pickle Module:")
data_to_pickle = {
    "name": "Alice",
    "scores": [85, 92, 78],
    "grades": {"math": "A", "science": "B"},
}

# Python object to pickle
pickled_data = pickle.dumps(data_to_pickle)
print(f"Pickled data size: {len(pickled_data)} bytes")

# Pickle to Python object
unpickled_data = pickle.loads(pickled_data)
print(f"Unpickled data: {unpickled_data}")

# Urllib module
import urllib.parse

print("\n10. Urllib Module:")
url = "https://www.example.com/path?name=Alice&age=25"
parsed = urllib.parse.urlparse(url)
print(f"Scheme: {parsed.scheme}")
print(f"Netloc: {parsed.netloc}")
print(f"Path: {parsed.path}")
print(f"Query: {parsed.query}")

# Parse query parameters
params = urllib.parse.parse_qs(parsed.query)
print(f"Query parameters: {params}")

print("\n=== END OF BUILT-IN MODULES ===")
