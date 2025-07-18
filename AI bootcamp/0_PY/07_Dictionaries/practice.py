# Python Dictionaries Practice

print("=== PYTHON DICTIONARIES PRACTICE ===\n")

# 1. Dictionary Creation
print("1. Dictionary Creation:")
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Person dictionary: {person}")

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="Boston")
print(f"Person2 dictionary: {person2}")

# From list of tuples
items = [("name", "Charlie"), ("age", 35), ("city", "Chicago")]
person3 = dict(items)
print(f"Person3 dictionary: {person3}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares}")
print()

# 2. Accessing Dictionary Elements
print("2. Accessing Dictionary Elements:")
student = {"name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Physics"]}

# Using square brackets
name = student["name"]
print(f"Name: {name}")

# Using get() method
age = student.get("age")
grade = student.get("grade")
job = student.get("job")  # Returns None
job_safe = student.get("job", "Student")  # Returns default value

print(f"Age: {age}")
print(f"Grade: {grade}")
print(f"Job (not found): {job}")
print(f"Job with default: {job_safe}")

# Checking if key exists
print(f"'name' in student: {'name' in student}")
print(f"'job' in student: {'job' in student}")

# Getting all keys, values, and items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")
print()

# 3. Modifying Dictionaries
print("3. Modifying Dictionaries:")
person = {"name": "Alice", "age": 25}

# Adding new key-value pairs
person["city"] = "New York"
person["job"] = "Engineer"
print(f"After adding: {person}")

# Updating existing values
person["age"] = 26
print(f"After updating age: {person}")

# Using update() method
person.update({"city": "Boston", "salary": 75000})
print(f"After update(): {person}")

# Removing items
removed_age = person.pop("age")
print(f"Removed age: {removed_age}")
print(f"After pop(): {person}")

# Using del
del person["job"]
print(f"After del: {person}")

# clear() method
person.clear()
print(f"After clear(): {person}")
print()

# 4. Dictionary Methods
print("4. Dictionary Methods:")
person = {"name": "Alice", "age": 25}

# setdefault()
person.setdefault("city", "New York")
person.setdefault("name", "Bob")  # Won't change existing value
print(f"After setdefault(): {person}")

# popitem() - removes and returns last item
last_item = person.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem(): {person}")

# copy() method
original = {"name": "Alice", "scores": [85, 90, 78]}
shallow_copy = original.copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Modifying nested structure affects both
shallow_copy["scores"][0] = 100
print(f"After modifying nested: {original}")
print(f"Shallow copy: {shallow_copy}")
print()

# 5. Dictionary Operations
print("5. Dictionary Operations:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merging dictionaries
merged = dict1.copy()
merged.update(dict2)
print(f"Merged: {merged}")

# Dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
upper_person = {k.upper(): v for k, v in person.items()}
print(f"Upper keys: {upper_person}")
print()

# 6. Common Dictionary Patterns
print("6. Common Dictionary Patterns:")

# Counting items
words = ["apple", "banana", "apple", "cherry", "banana"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"Word counts: {counts}")

# Grouping data
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
]

grades = {}
for student in students:
    grade = student["grade"]
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(student["name"])

print(f"Students by grade: {grades}")

# Using defaultdict
from collections import defaultdict

grades_dd = defaultdict(list)
for student in students:
    grades_dd[student["grade"]].append(student["name"])
print(f"Using defaultdict: {dict(grades_dd)}")
print()

# 7. Built-in Functions with Dictionaries
print("7. Built-in Functions with Dictionaries:")
person = {"name": "Alice", "age": 25, "city": "New York"}

print(f"Length: {len(person)}")
print(f"Maximum key: {max(person)}")
print(f"Minimum key: {min(person)}")
print(f"Any key: {any(person)}")
print(f"All keys: {all(person)}")

# sorted() with dictionaries
print(f"Sorted keys: {sorted(person)}")
print(f"Sorted items: {sorted(person.items())}")
print(f"Sorted by values: {sorted(person.items(), key=lambda x: x[1])}")
print()

# 8. Dictionary Views
print("8. Dictionary Views:")
person = {"name": "Alice", "age": 25, "city": "New York"}

keys_view = person.keys()
values_view = person.values()
items_view = person.items()

print(f"Keys view: {keys_view}")
print(f"Values view: {values_view}")
print(f"Items view: {items_view}")

# Views are dynamic
person["job"] = "Engineer"
print(f"Keys view after adding job: {list(keys_view)}")
print()

# 9. Practice Problems
print("9. Practice Problems:")


# Problem 1: Count character frequencies
def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


text = "Hello World"
char_freq = count_characters(text)
print(f"Character frequencies in '{text}': {char_freq}")


# Problem 2: Find most common word
def most_common_word(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    if not word_count:
        return None

    return max(word_count.items(), key=lambda x: x[1])


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
most_common = most_common_word(words)
print(f"Most common word: {most_common}")


# Problem 3: Merge dictionaries with conflict resolution
def merge_dicts(dict1, dict2, conflict_strategy="first"):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            if conflict_strategy == "first":
                continue  # Keep first value
            elif conflict_strategy == "second":
                result[key] = value  # Use second value
            elif conflict_strategy == "combine":
                if isinstance(result[key], list) and isinstance(value, list):
                    result[key].extend(value)
                else:
                    result[key] = [result[key], value]
        else:
            result[key] = value

    return result


dict1 = {"a": 1, "b": 2, "c": [1, 2]}
dict2 = {"b": 3, "c": [3, 4], "d": 4}

merged_first = merge_dicts(dict1, dict2, "first")
merged_second = merge_dicts(dict1, dict2, "second")
merged_combine = merge_dicts(dict1, dict2, "combine")

print(f"Merge with 'first' strategy: {merged_first}")
print(f"Merge with 'second' strategy: {merged_second}")
print(f"Merge with 'combine' strategy: {merged_combine}")


# Problem 4: Invert dictionary
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted


original = {"a": 1, "b": 2, "c": 1, "d": 3}
inverted = invert_dict(original)
print(f"Original: {original}")
print(f"Inverted: {inverted}")


# Problem 5: Create a simple cache
class SimpleCache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            # Remove oldest item (simple FIFO)
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

    def size(self):
        return len(self.cache)


# Test cache
cache = SimpleCache(max_size=3)
cache.set("user1", {"name": "Alice", "age": 25})
cache.set("user2", {"name": "Bob", "age": 30})
cache.set("user3", {"name": "Charlie", "age": 35})
cache.set("user4", {"name": "Diana", "age": 28})  # This will evict user1

print(f"Cache size: {cache.size()}")
print(f"User1: {cache.get('user1')}")  # None (evicted)
print(f"User2: {cache.get('user2')}")  # Still there


# Problem 6: Flatten nested dictionary
def flatten_dict(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


nested = {
    "user": {"name": "Alice", "address": {"city": "New York", "zip": "10001"}},
    "settings": {"theme": "dark"},
}

flattened = flatten_dict(nested)
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")


# Problem 7: Dictionary-based configuration
class Config:
    def __init__(self, config_dict):
        self._config = config_dict

    def get(self, key, default=None):
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        keys = key.split(".")
        config = self._config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value


# Test configuration
config_dict = {"database": {"host": "localhost", "port": 5432}, "api": {"timeout": 30}}

config = Config(config_dict)
print(f"Database host: {config.get('database.host')}")
print(f"API timeout: {config.get('api.timeout')}")
print(f"Non-existent: {config.get('database.password', 'default')}")

config.set("database.password", "secret123")
print(f"After setting password: {config.get('database.password')}")

print("\n=== END OF PRACTICE ===")
