# Collections Module

print("=== COLLECTIONS MODULE ===\n")

from collections import defaultdict, Counter, namedtuple, deque, OrderedDict, ChainMap

print("1. DefaultDict:")
# DefaultDict with list as default factory
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)
print(f"DefaultDict with list: {dict(d)}")

# DefaultDict with int as default factory
word_count = defaultdict(int)
text = "hello world hello python"
for word in text.split():
    word_count[word] += 1
print(f"Word count with DefaultDict: {dict(word_count)}")

# DefaultDict with set as default factory
unique_letters = defaultdict(set)
words = ["hello", "world", "python"]
for word in words:
    for letter in word:
        unique_letters[letter].add(word)
print(f"Letters and their words: {dict(unique_letters)}")

print("\n2. Counter:")
# Basic Counter
text = "hello world"
char_count = Counter(text)
print(f"Character count: {dict(char_count)}")

# Counter with words
word_count = Counter(text.split())
print(f"Word count: {dict(word_count)}")

# Counter operations
c1 = Counter(["a", "b", "c", "a", "b", "b"])
c2 = Counter(["a", "b", "d"])
print(f"Counter 1: {dict(c1)}")
print(f"Counter 2: {dict(c2)}")
print(f"c1 + c2: {dict(c1 + c2)}")
print(f"c1 - c2: {dict(c1 - c2)}")
print(f"c1 & c2 (intersection): {dict(c1 & c2)}")
print(f"c1 | c2 (union): {dict(c1 | c2)}")

# Most common elements
print(f"Most common 2 elements: {c1.most_common(2)}")

print("\n3. NamedTuple:")
# Basic NamedTuple
Person = namedtuple("Person", ["name", "age", "city"])
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "London")
print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Person 1 name: {person1.name}")
print(f"Person 1 age: {person1.age}")

# NamedTuple with default values
Point = namedtuple("Point", ["x", "y"], defaults=[0, 0])
p1 = Point(1, 2)
p2 = Point()  # Uses defaults
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")

# NamedTuple with type hints (Python 3.6+)
from typing import NamedTuple


class Employee(NamedTuple):
    name: str
    id: int
    department: str


emp = Employee("John", 123, "IT")
print(f"Employee: {emp}")

print("\n4. Deque:")
# Basic deque operations
dq = deque([1, 2, 3])
print(f"Original deque: {dq}")

dq.append(4)
print(f"After append: {dq}")

dq.appendleft(0)
print(f"After appendleft: {dq}")

popped_right = dq.pop()
print(f"Popped from right: {popped_right}")
print(f"After pop: {dq}")

popped_left = dq.popleft()
print(f"Popped from left: {popped_left}")
print(f"After popleft: {dq}")

# Deque with maxlen
limited_dq = deque([1, 2, 3], maxlen=3)
limited_dq.append(4)
print(f"Limited deque after append: {limited_dq}")

# Deque rotation
rotating_dq = deque([1, 2, 3, 4, 5])
print(f"Original: {rotating_dq}")
rotating_dq.rotate(2)
print(f"After rotate(2): {rotating_dq}")
rotating_dq.rotate(-1)
print(f"After rotate(-1): {rotating_dq}")

print("\n5. OrderedDict:")
# OrderedDict maintains insertion order
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(f"OrderedDict: {dict(od)}")

# OrderedDict with move_to_end
od.move_to_end("a")
print(f"After move_to_end('a'): {dict(od)}")

# OrderedDict with popitem
last_item = od.popitem()
print(f"Popped last item: {last_item}")
print(f"After popitem: {dict(od)}")

print("\n6. ChainMap:")
# ChainMap for multiple dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

cm = ChainMap(dict1, dict2, dict3)
print(f"ChainMap: {dict(cm)}")
print(f"Value for 'a': {cm['a']}")
print(f"Value for 'b': {cm['b']}")  # Takes from first dict
print(f"Value for 'c': {cm['c']}")  # Takes from first dict

# ChainMap with new_child
new_cm = cm.new_child({"e": 7})
print(f"New ChainMap: {dict(new_cm)}")

print("\n7. Practical Examples:")

# Example 1: Word frequency analysis
text = "the quick brown fox jumps over the lazy dog"
words = text.split()
word_freq = Counter(words)
print(f"Word frequency: {dict(word_freq)}")

# Example 2: Grouping data
students = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 90),
    ("Alice", "Science", 88),
    ("Charlie", "Math", 92),
    ("Bob", "Science", 87),
]

# Group by student
student_scores = defaultdict(list)
for name, subject, score in students:
    student_scores[name].append((subject, score))

print("Student scores:")
for student, scores in student_scores.items():
    print(f"  {student}: {scores}")

# Example 3: Queue with deque
queue = deque()
queue.append("first")
queue.append("second")
queue.append("third")

print("Queue operations:")
while queue:
    item = queue.popleft()
    print(f"  Processed: {item}")

# Example 4: Configuration with OrderedDict
config = OrderedDict(
    [("host", "localhost"), ("port", 8080), ("debug", True), ("timeout", 30)]
)

print("Configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

print("\n=== END OF COLLECTIONS MODULE ===")
