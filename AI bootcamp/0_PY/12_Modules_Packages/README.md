# Python Modules and Packages

## Overview
Modules and packages are ways to organize and reuse Python code. A module is a single Python file, while a package is a directory containing multiple modules and an `__init__.py` file.

## Modules

### Creating a Simple Module
```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

PI = 3.14159
E = 2.71828
```

### Importing Modules
```python
# Import entire module
import math_utils

result = math_utils.add(5, 3)
print(result)  # 8

# Import specific functions
from math_utils import add, subtract

result = add(10, 5)
print(result)  # 15

# Import with alias
import math_utils as mu

result = mu.multiply(4, 6)
print(result)  # 24

# Import all (not recommended)
from math_utils import *

result = divide(10, 2)
print(result)  # 5.0
```

### Built-in Modules
```python
# Math module
import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

# Random module
import random
print(random.randint(1, 10))  # Random number between 1 and 10
print(random.choice(['apple', 'banana', 'orange']))

# Datetime module
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# OS module
import os
print(os.getcwd())  # Current working directory
print(os.listdir()) # List files in current directory
```

## Package Structure

### Basic Package
```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
```

### Creating a Package
```python
# my_package/__init__.py
from .module1 import function1
from .module2 import function2

__version__ = "1.0.0"
__author__ = "Your Name"

# This makes the package importable
```

```python
# my_package/module1.py
def function1():
    return "Hello from module1"

def internal_function():
    return "This is internal"
```

```python
# my_package/module2.py
def function2():
    return "Hello from module2"

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
```

### Importing from Packages
```python
# Import from package
import my_package

result = my_package.function1()
print(result)

# Import specific module from package
from my_package import module1

result = module1.function1()
print(result)

# Import specific function
from my_package.module1 import function1

result = function1()
print(result)

# Import class
from my_package.module2 import MyClass

obj = MyClass("test")
print(obj.get_value())
```

## Advanced Import Techniques

### Relative Imports
```python
# Inside a package, you can use relative imports
# my_package/subpackage/submodule.py

# Import from parent package
from ..module1 import function1

# Import from sibling module
from ..module2 import MyClass

# Import from same level
from .other_submodule import some_function
```

### Conditional Imports
```python
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy not available")

def process_data(data):
    if HAS_NUMPY:
        return np.array(data)
    else:
        return list(data)
```

### Dynamic Imports
```python
import importlib

# Import module dynamically
module_name = "math"
math_module = importlib.import_module(module_name)
print(math_module.pi)

# Import function dynamically
def import_function(module_name, function_name):
    module = importlib.import_module(module_name)
    return getattr(module, function_name)

sqrt_func = import_function("math", "sqrt")
print(sqrt_func(16))
```

## Module Attributes

### Special Module Attributes
```python
# __name__ - module name
print(__name__)  # "__main__" if run directly, module name if imported

# __file__ - module file path
print(__file__)

# __doc__ - module documentation
print(__doc__)

# __all__ - defines what gets imported with "from module import *"
__all__ = ['public_function', 'PublicClass']

def public_function():
    return "This is public"

def _private_function():
    return "This is private"

class PublicClass:
    pass
```

### Module Documentation
```python
"""
This is a module for mathematical operations.

This module provides basic arithmetic functions and mathematical constants.
It can be used for simple calculations and educational purposes.

Author: Your Name
Version: 1.0.0
"""

def add(a, b):
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b
```

## Package Management

### Creating a Setup File
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.19.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
```

### Installing Packages
```bash
# Install in development mode
pip install -e .

# Install from PyPI
pip install package_name

# Install specific version
pip install package_name==1.0.0

# Install with requirements
pip install -r requirements.txt
```

## Common Module Patterns

### Singleton Pattern
```python
# singleton.py
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = []
            self.initialized = True
    
    def add_data(self, item):
        self.data.append(item)
    
    def get_data(self):
        return self.data.copy()
```

### Factory Pattern
```python
# factory.py
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def create_animal(animal_type):
    animals = {
        "dog": Dog,
        "cat": Cat,
    }
    
    if animal_type in animals:
        return animals[animal_type]()
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")
```

### Configuration Module
```python
# config.py
import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    
    @classmethod
    def get_database_url(cls):
        return cls.DATABASE_URL
    
    @classmethod
    def is_debug(cls):
        return cls.DEBUG
```

## Testing Modules

### Unit Testing
```python
# test_math_utils.py
import unittest
from math_utils import add, subtract, multiply, divide

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
    
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
```

## Best Practices

### Module Organization
```python
# Good structure
"""
Module documentation
"""

# Standard library imports
import os
import sys
from datetime import datetime

# Third-party imports
import requests
import numpy as np

# Local imports
from .utils import helper_function
from .config import Config

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Classes
class MyClass:
    pass

# Functions
def main():
    pass

if __name__ == "__main__":
    main()
```

### Import Organization
```python
# 1. Standard library imports
import os
import sys
from datetime import datetime

# 2. Third-party imports
import requests
import numpy as np

# 3. Local application imports
from my_package import my_module
from my_package.subpackage import submodule
```

### Avoiding Circular Imports
```python
# Bad - circular import
# module1.py
from module2 import function2

def function1():
    return function2()

# module2.py
from module1 import function1

def function2():
    return function1()

# Good - use lazy imports
# module1.py
def function1():
    from module2 import function2
    return function2()

# module2.py
def function2():
    from module1 import function1
    return function1()
```

## Common Built-in Modules

### Collections
```python
from collections import defaultdict, Counter, namedtuple

# DefaultDict
d = defaultdict(list)
d['a'].append(1)  # No KeyError

# Counter
c = Counter(['a', 'b', 'a', 'c'])
print(c)  # Counter({'a': 2, 'b': 1, 'c': 1})

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
```

### JSON
```python
import json

# Serialize
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)

# Deserialize
parsed_data = json.loads(json_string)
print(parsed_data["name"])
```

### Pickle
```python
import pickle

# Serialize object
data = {"name": "Alice", "age": 25}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Deserialize object
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print(loaded_data)
```

## Practice Examples
See `practice.py` for hands-on exercises with modules and packages! 