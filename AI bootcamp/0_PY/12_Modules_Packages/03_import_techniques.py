# Import Techniques

print("=== IMPORT TECHNIQUES ===\n")

# Import with alias
import math as m

print("1. Import with alias:")
print(f"Using alias - PI: {m.pi}")
print(f"Using alias - sqrt(25): {m.sqrt(25)}")

# Import specific functions
from math import sqrt, pi, ceil, floor

print("\n2. Import specific functions:")
print(f"Direct import - sqrt(25): {sqrt(25)}")
print(f"Direct import - pi: {pi}")
print(f"Direct import - ceil(4.3): {ceil(4.3)}")
print(f"Direct import - floor(4.7): {floor(4.7)}")

# Import with conditional
print("\n3. Conditional imports:")
try:
    import numpy as np

    print("NumPy is available")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr}")
except ImportError:
    print("NumPy is not available")
    arr = [1, 2, 3, 4, 5]
    print(f"Regular list: {arr}")

# Import with relative paths (simulated)
print("\n4. Relative imports (simulated):")
# In a real package structure, you might have:
# from . import my_module
# from .. import parent_module
# from .my_module import my_function

# Import from submodules
import datetime
from datetime import datetime as dt

print("\n5. Import from submodules:")
now = dt.now()
print(f"Current time: {now}")

# Import with custom namespace
import random as rand

print("\n6. Custom namespace:")
print(f"Random number: {rand.randint(1, 10)}")
print(f"Random choice: {rand.choice(['apple', 'banana', 'orange'])}")

# Import multiple modules with aliases
import os as operating_system
import sys as system_info

print("\n7. Multiple aliases:")
print(f"OS name: {operating_system.name}")
print(f"Platform: {system_info.platform}")

# Import with renaming
from math import sqrt as square_root
from math import pi as PI_CONSTANT

print("\n8. Function renaming:")
print(f"Square root of 16: {square_root(16)}")
print(f"PI constant: {PI_CONSTANT}")

# Import with multiple items
from math import sqrt, e, ceil, floor

print("\n9. Multiple imports:")
print(f"sqrt(9): {sqrt(9)}")
print(f"pi: {pi}")
print(f"e: {e}")
print(f"ceil(3.2): {ceil(3.2)}")
print(f"floor(3.8): {floor(3.8)}")

# Import with exception handling
print("\n10. Import with exception handling:")
modules_to_try = ["numpy", "pandas", "matplotlib", "requests"]

for module_name in modules_to_try:
    try:
        module = __import__(module_name)
        print(f"✓ {module_name} is available")
    except ImportError:
        print(f"✗ {module_name} is not available")

# Import with lazy loading
print("\n11. Lazy loading (simulated):")


class LazyModule:
    def __init__(self, module_name):
        self.module_name = module_name
        self._module = None

    def __getattr__(self, name):
        if self._module is None:
            self._module = __import__(self.module_name)
        return getattr(self._module, name)


# Usage example
math_lazy = LazyModule("math")
print(f"Lazy loaded PI: {math_lazy.pi}")

# Import with version checking
print("\n12. Version checking:")
import sys

if sys.version_info >= (3, 8):
    print("Python 3.8+ features available")
    # You could import newer features here
else:
    print("Using older Python version")

# Import with environment-based selection
print("\n13. Environment-based imports:")
import os

if os.getenv("USE_NUMPY", "false").lower() == "true":
    try:
        import numpy as np

        print("Using NumPy for calculations")
    except ImportError:
        print("NumPy requested but not available")
else:
    print("Using standard library for calculations")

# Import with custom import function
print("\n14. Custom import function:")


def safe_import(module_name):
    """Safely import a module"""
    try:
        return __import__(module_name)
    except ImportError:
        return None


# Test safe import
numpy_module = safe_import("numpy")
if numpy_module:
    print(f"Imported module: {numpy_module.__name__}")
else:
    print("NumPy not available")

print("\n=== END OF IMPORT TECHNIQUES ===")
