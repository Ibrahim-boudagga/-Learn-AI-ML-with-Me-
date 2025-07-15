# 🎯 Regular Expressions (Regex)

> **Mastering Pattern Matching in Text Processing** 🔍

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)](https://python.org)
[![Regex](https://img.shields.io/badge/Regex-Pattern_Matching-green?style=flat)](https://docs.python.org/3/library/re.html)
[![NLP](https://img.shields.io/badge/NLP-Text_Processing-orange?style=flat)](https://nltk.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)](https://jupyter.org)

---

## 📖 **What are Regular Expressions?**

Regular expressions (regex) are powerful pattern-matching tools used to search, extract, and manipulate text based on specific patterns. They're essential for:

- **🔍 Text Search**: Finding specific patterns in large datasets
- **🔄 Text Replacement**: Automatically replacing text patterns
- **📊 Data Extraction**: Extracting structured information from unstructured text
- **🧹 Data Cleaning**: Removing unwanted patterns or formatting
- **✅ Validation**: Checking if text matches expected formats

---

## 🚀 **Current Implementation**

This module includes practical examples with professional colored logging:

### **📁 Files Included**
- **`regx.py`** - Python script with regex examples and colored logging
- **`2.4 Regular Expressions.ipynb`** - Jupyter notebook for interactive learning
- **`README.md`** - Comprehensive regex guide (this file)

### **🎯 Key Features Demonstrated**
- **Pattern matching** with `re.search()` and `re.findall()`
- **Text substitution** with `re.sub()`
- **Raw string handling** for Windows paths
- **Professional logging** with ColoredLogs
- **Real-world examples** for NLP applications

---

## 🎯 **When to Use Regular Expressions**

### **✅ Perfect For:**
- **Email validation**: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- **Phone number extraction**: `\b\d{3}[-.]?\d{3}[-.]?\d{4}\b`
- **URL parsing**: `https?://[^\s]+`
- **Date pattern matching**: `\d{1,2}[/-]\d{1,2}[/-]\d{2,4}`
- **Credit card validation**: `\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b`
- **Text preprocessing**: Removing special characters, extracting words

### **❌ Avoid For:**
- **Simple string operations**: Use `str.replace()`, `str.find()` instead
- **HTML/XML parsing**: Use dedicated parsers (BeautifulSoup, lxml)
- **Complex nested structures**: Consider JSON/XML parsers
- **Performance-critical applications**: Regex can be slower than string methods

---

## 🛠️ **Core Regex Functions**

### **1. re.search() - Find First Match**
```python
import re

text = "The quick brown fox jumps over the lazy dog"
result = re.search(r"fox", text)

if result:
    print(f"Found: {result.group()}")  # 'fox'
    print(f"Position: {result.span()}")  # (16, 19)
else:
    print("No match found")
```

### **2. re.findall() - Find All Matches**
```python
text = "The quick brown fox jumps over the lazy dog"
words_starting_with_t = re.findall(r'\bt\w+', text)
print(words_starting_with_t)  # ['The', 'the']
```

### **3. re.sub() - Replace Patterns**
```python
text = "sara was able to help me find the items i needed quickly"
corrected = re.sub(r"sara", "sarah", text)
print(corrected)  # "sarah was able to help me find the items i needed quickly"
```

### **4. re.match() - Match at Start**
```python
text = "Hello World"
if re.match(r"^Hello", text):
    print("Starts with 'Hello'")
```

---

## 📚 **Essential Regex Patterns**

### **🔤 Character Classes**
```python
# Word characters
r'\w+'          # One or more word characters
r'\b\w+\b'      # Complete words only

# Digits
r'\d+'          # One or more digits
r'\d{3,4}'      # 3 to 4 digits

# Whitespace
r'\s+'          # One or more whitespace characters
r'\S+'          # One or more non-whitespace characters
```

### **📍 Anchors**
```python
r'^start'       # String starts with 'start'
r'end$'         # String ends with 'end'
r'\bword\b'     # Word boundary
```

### **🔄 Quantifiers**
```python
r'a*'           # Zero or more 'a's
r'a+'           # One or more 'a's
r'a?'           # Zero or one 'a'
r'a{3}'         # Exactly 3 'a's
r'a{2,4}'       # 2 to 4 'a's
```

### **📝 Groups and Capturing**
```python
r'(\w+)@(\w+)\.(\w+)'  # Email with groups
r'(?P<name>\w+)'       # Named group
```

---

## 💻 **Practical Examples**

### **📧 Email Validation**
```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Test
emails = [
    "user@example.com",
    "invalid.email",
    "user@domain.co.uk"
]

for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
```

### **📱 Phone Number Extraction**
```python
import re

text = "Contact us at 555-123-4567 or 555.987.6543"
phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
phones = re.findall(phone_pattern, text)
print(f"Found phones: {phones}")
```

### **🔤 Word Frequency Analysis**
```python
import re
from collections import Counter

text = "The quick brown fox jumps over the lazy dog. The fox is quick."
words = re.findall(r'\b\w+\b', text.lower())
word_freq = Counter(words)
print(word_freq.most_common(3))
```

---

## ⚡ **Performance Best Practices**

### **🚀 Optimization Tips**
```python
# 1. Compile patterns for reuse
pattern = re.compile(r'\b\w+\b')
words = pattern.findall(text)

# 2. Use raw strings (r'') for patterns
pattern = r'\d+'  # Good
pattern = '\\d+'  # Avoid

# 3. Use appropriate quantifiers
r'\w+'           # Good - non-greedy
r'\w*'           # Avoid - can be greedy

# 4. Use word boundaries for precision
r'\bword\b'      # Good - exact word match
r'word'          # Avoid - matches substrings
```

### **🎯 Common Mistakes to Avoid**
```python
# ❌ Don't: Overly complex patterns
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# ✅ Do: Break into readable parts
local_part = r'[a-zA-Z0-9._%+-]+'
domain = r'[a-zA-Z0-9.-]+'
tld = r'[a-zA-Z]{2,}'
pattern = f'^{local_part}@{domain}\\.{tld}$'
```

---

## 🧪 **Testing and Debugging**

### **🔍 Regex Testing Tools**
```python
import re

def test_regex(pattern, test_strings):
    """Test regex pattern against multiple strings"""
    compiled = re.compile(pattern)
    
    for test_str in test_strings:
        match = compiled.search(test_str)
        status = "✅ Match" if match else "❌ No match"
        print(f"{test_str}: {status}")
        if match:
            print(f"  Matched: '{match.group()}' at {match.span()}")

# Example usage
pattern = r'\b\w+@\w+\.\w+\b'
test_strings = [
    "user@example.com",
    "invalid.email",
    "test@domain.co.uk"
]
test_regex(pattern, test_strings)
```

### **🐛 Debugging Tips**
```python
# 1. Use re.DEBUG flag for complex patterns
pattern = re.compile(r'\b\w+@\w+\.\w+\b', re.DEBUG)

# 2. Test with simple examples first
simple_pattern = r'fox'
result = re.search(simple_pattern, "The fox is quick")

# 3. Use online regex testers for validation
# - regex101.com
# - regexr.com
# - debuggex.com
```

---

## 📊 **Real-World Applications**

### **📈 Data Analysis**
```python
import re
import pandas as pd
from ColoredLogs import Debugger

Debugger.info("Starting data analysis with regex...")

# Extract patterns from text data
text_data = ["user@example.com", "invalid.email", "test@domain.co.uk"]
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

valid_emails = [email for email in text_data if re.match(email_pattern, email)]
Debugger.success(f"Found {len(valid_emails)} valid emails: {valid_emails}")
```

# Extract dates from text
text_data = [
    "Meeting on 2023-12-25",
    "Deadline: 12/31/2023",
    "Event: 25-12-2023"
]

date_pattern = r'\d{4}[-/]\d{1,2}[-/]\d{1,2}'
dates = [re.findall(date_pattern, text) for text in text_data]
print(f"Extracted dates: {dates}")
```

### **🔧 Log Processing**
```python
import re

log_line = "2023-12-25 10:30:45 [ERROR] User authentication failed for user_id=12345"

# Extract components
timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
level_pattern = r'\[(INFO|ERROR|WARN)\]'
user_pattern = r'user_id=(\d+)'

timestamp = re.search(timestamp_pattern, log_line)
level = re.search(level_pattern, log_line)
user_id = re.search(user_pattern, log_line)

print(f"Timestamp: {timestamp.group() if timestamp else 'N/A'}")
print(f"Level: {level.group(1) if level else 'N/A'}")
print(f"User ID: {user_id.group(1) if user_id else 'N/A'}")
```

---

## 🎓 **Learning Resources**

### **📚 Recommended Reading**
- [Python re Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expressions Cookbook](https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/)
- [Regex101](https://regex101.com/) - Online regex tester

### **🎯 Practice Exercises**
1. **Email Validation**: Create a robust email validator
2. **Phone Number Parser**: Extract phone numbers from various formats
3. **Date Extractor**: Parse dates in different formats
4. **URL Parser**: Extract domains and paths from URLs
5. **Text Cleaner**: Remove special characters and normalize text

---

## 🚀 **Advanced Techniques**

### **🔧 Named Groups**
```python
import re

# Extract structured data
text = "Name: John Doe, Age: 30, Email: john@example.com"

pattern = r'Name:\s*(?P<name>\w+\s+\w+),\s*Age:\s*(?P<age>\d+),\s*Email:\s*(?P<email>\S+)'
match = re.search(pattern, text)

if match:
    data = match.groupdict()
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"Email: {data['email']}")
```

### **🔄 Lookahead and Lookbehind**
```python
import re

# Positive lookahead
text = "password123 secret456 key789"
# Find words followed by numbers
pattern = r'\w+(?=\d)'
matches = re.findall(pattern, text)
print(f"Words before numbers: {matches}")

# Negative lookbehind
text = "price: $100, cost: $50, value: $200"
# Find dollar amounts not preceded by 'cost'
pattern = r'(?<!cost: )\$(\d+)'
matches = re.findall(pattern, text)
print(f"Non-cost amounts: {matches}")
```

---

## 📈 **Performance Comparison**

### **⚡ Speed Benchmarks**
```python
import re
import time

text = "The quick brown fox jumps over the lazy dog " * 1000

# Method 1: re.search()
start = time.time()
result = re.search(r'fox', text)
time1 = time.time() - start

# Method 2: str.find()
start = time.time()
result = text.find('fox')
time2 = time.time() - start

print(f"Regex search: {time1:.6f}s")
print(f"String find: {time2:.6f}s")
print(f"Regex is {time1/time2:.1f}x slower")
```

---

## 🎯 **Best Practices Summary**

### **✅ Do's**
- **Use raw strings** (`r''`) for patterns
- **Compile patterns** for reuse
- **Test thoroughly** with edge cases
- **Use word boundaries** for precise matching
- **Keep patterns simple** and readable
- **Document complex patterns** with comments

### **❌ Don'ts**
- **Don't over-engineer** simple string operations
- **Avoid overly complex** patterns
- **Don't forget to handle** None results
- **Avoid greedy quantifiers** when not needed
- **Don't use regex** for HTML/XML parsing

---

## 🔗 **Related Topics**

- **📝 [Text Preprocessing](./../README.md)** - Complete NLP pipeline
- **🔤 [Lowercasing](./../1_Lowercasing/README.md)** - Text normalization
- **🚫 [Stopwords Removal](./../2_StopWords/README.md)** - Filtering common words
- **📊 [Data Analysis](../README.md)** - Statistical text analysis

---

*Master regex patterns to unlock powerful text processing capabilities!* 🎯

---

*Made with ❤️ for the AI/ML community*
