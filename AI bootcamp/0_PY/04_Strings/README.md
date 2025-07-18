# Python Strings

## Overview
Strings in Python are sequences of characters enclosed in quotes. They are immutable (cannot be changed after creation).

## String Creation
```python
# Single quotes
name = 'John'

# Double quotes
message = "Hello, World!"

# Triple quotes (for multi-line strings)
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""

# Triple single quotes
code = '''
def hello():
    print("Hello, World!")
'''
```

## String Indexing and Slicing
```python
text = "Python Programming"

# Indexing (starts from 0)
first_char = text[0]      # 'P'
last_char = text[-1]      # 'g'
second_char = text[1]     # 'y'

# Slicing [start:end:step]
first_word = text[0:6]    # 'Python'
second_word = text[7:]    # 'Programming'
every_second = text[::2]  # 'Pto rgamn'
reverse = text[::-1]      # 'gnimmargorP nohtyP'
```

## String Methods

### Case Conversion
```python
text = "Hello World"

text.upper()      # 'HELLO WORLD'
text.lower()      # 'hello world'
text.title()      # 'Hello World'
text.capitalize() # 'Hello world'
text.swapcase()   # 'hELLO wORLD'
```

### Search and Replace
```python
text = "Python is awesome"

# Finding substrings
text.find("is")       # 7
text.find("Java")     # -1 (not found)
text.index("is")      # 7
text.count("o")       # 2

# Replacing
text.replace("awesome", "amazing")  # 'Python is amazing'
text.replace("o", "0")             # 'Pyth0n is awes0me'
```

### Splitting and Joining
```python
sentence = "Python,Java,JavaScript,C++"

# Splitting
languages = sentence.split(",")  # ['Python', 'Java', 'JavaScript', 'C++']
words = "Hello World".split()    # ['Hello', 'World']

# Joining
joined = "-".join(languages)     # 'Python-Java-JavaScript-C++'
```

### Stripping Whitespace
```python
text = "   Hello World   "

text.strip()    # 'Hello World'
text.lstrip()   # 'Hello World   '
text.rstrip()   # '   Hello World'
```

### Checking String Properties
```python
text = "Hello123"

text.isalpha()    # False (contains numbers)
text.isdigit()    # False (contains letters)
text.isalnum()    # True (alphanumeric)
text.isspace()    # False
text.startswith("Hello")  # True
text.endswith("123")      # True
```

## String Formatting

### f-strings (Python 3.6+)
```python
name = "Alice"
age = 25
height = 1.75

# Basic f-string
message = f"Hello, my name is {name}"

# With expressions
info = f"I am {age} years old and {height:.2f}m tall"

# With methods
greeting = f"Hello, {name.upper()}!"
```

### .format() method
```python
name = "Bob"
age = 30

# Positional arguments
message = "Hello, my name is {} and I am {} years old".format(name, age)

# Named arguments
message = "Hello, my name is {n} and I am {a} years old".format(n=name, a=age)

# Indexed arguments
message = "Hello, my name is {0} and I am {1} years old".format(name, age)
```

### % operator (old style)
```python
name = "Charlie"
age = 35

message = "Hello, my name is %s and I am %d years old" % (name, age)
```

## String Concatenation
```python
# Using + operator
first = "Hello"
second = "World"
result = first + " " + second  # "Hello World"

# Using join()
words = ["Hello", "World"]
result = " ".join(words)  # "Hello World"

# Using f-strings
result = f"{first} {second}"  # "Hello World"
```

## Escape Characters
```python
# Common escape characters
newline = "Line 1\nLine 2"
tab = "Column1\tColumn2"
quote = "He said \"Hello!\""
backslash = "C:\\Users\\Name"
raw_string = r"C:\Users\Name"  # Raw string, no escaping
```

## String Methods Summary
```python
# Case methods
.upper(), .lower(), .title(), .capitalize(), .swapcase()

# Search methods
.find(), .index(), .count(), .startswith(), .endswith()

# Replace methods
.replace()

# Split/Join methods
.split(), .join()

# Strip methods
.strip(), .lstrip(), .rstrip()

# Check methods
.isalpha(), .isdigit(), .isalnum(), .isspace()
```

## Common Use Cases
```python
# User input processing
user_input = "  john doe  "
clean_name = user_input.strip().title()  # "John Doe"

# URL building
base_url = "https://api.example.com"
endpoint = "/users"
url = base_url + endpoint

# File path handling
import os
path = os.path.join("folder", "file.txt")

# Data validation
email = "user@example.com"
is_valid = "@" in email and "." in email
```

## Course Structure

This Strings section is organized into individual practice files for focused learning:

### **Practice Files:**

1. **`01_string_creation.py`** - String creation and basic operations
   - Creating strings and basic indexing
   - String length and slicing

2. **`02_case_conversion.py`** - String case conversion
   - upper(), lower(), title(), capitalize()
   - Case manipulation methods

3. **`03_search_replace.py`** - String search and replace
   - find(), count(), replace() methods
   - String searching and substitution

4. **`04_split_join.py`** - String splitting and joining
   - split(), join() methods
   - Working with string lists

5. **`05_string_formatting.py`** - String formatting
   - f-strings, .format() method
   - Different formatting techniques

6. **`06_string_validation.py`** - String validation
   - isalpha(), isdigit(), startswith()
   - String validation methods

7. **`07_string_manipulation.py`** - String manipulation
   - strip(), center(), justify methods
   - String cleaning and formatting

8. **`08_practice_problems.py`** - Practice problems
   - 5 practical exercises
   - Real-world string processing

### **How to Use This Course:**

1. **Start with the README** - Read through the theory and concepts
2. **Run each file individually** - Execute `python filename.py` to see examples
3. **Experiment with code** - Modify strings and try different methods
4. **Complete practice problems** - Work through the exercises in `08_practice_problems.py`
5. **Move to next section** - Progress to Lists section

### **Running the Examples:**

```bash
# Run individual files
python 01_string_creation.py
python 02_case_conversion.py
python 03_search_replace.py
# ... and so on

# Or run all files in sequence
for file in *.py; do
    echo "=== Running $file ==="
    python "$file"
    echo
done
```

## Practice Examples
Each file contains hands-on exercises and examples. Start with `01_string_creation.py` and work your way through! 