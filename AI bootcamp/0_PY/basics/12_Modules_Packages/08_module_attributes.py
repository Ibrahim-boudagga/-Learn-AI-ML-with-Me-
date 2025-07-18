# Module Attributes

print("=== MODULE ATTRIBUTES ===\n")

print("1. Basic Module Attributes:")

# Simulating module attributes
module_name = "__main__"
module_file = "practice.py"
module_doc = "This is a practice module for Python modules and packages"

print(f"Module name: {module_name}")
print(f"Module file: {module_file}")
print(f"Module doc: {module_doc}")

# Simulating __all__
__all__ = ["Calculator", "StringUtils", "MathUtils", "Config", "Logger"]  # type:ignore

print(f"All exports: {__all__}")

print("\n2. Module Information:")

import sys
import os

print(f"Current module name: {__name__}")
print(f"Current file: {__file__}")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

print("\n3. Module Path and Location:")

# Get module path
module_path = os.path.abspath(__file__)
module_dir = os.path.dirname(module_path)
print(f"Module absolute path: {module_path}")
print(f"Module directory: {module_dir}")

print("\n4. Module Documentation:")

# Module docstring
"""
This module demonstrates various module attributes and concepts.
It shows how to work with module metadata and exports.
"""

print("Module docstring:")
print(__doc__)

print("\n5. Module Exports:")


# Define what should be exported
def public_function():
    """This function is part of the public API."""
    return "Public function called"


def _private_function():
    """This function is private and should not be imported."""
    return "Private function called"


# Public variables
PUBLIC_CONSTANT = 42
_private_constant = "secret"

# Update __all__ to control exports
__all__ = ["public_function", "PUBLIC_CONSTANT", "Calculator", "StringUtils"]  # type: ignore

print(f"Public exports: {__all__}")

print("\n6. Module Configuration:")

# Module-level configuration
DEBUG = True
VERSION = "1.0.0"
AUTHOR = "Python Course"


def get_config():
    """Get module configuration."""
    return {"debug": DEBUG, "version": VERSION, "author": AUTHOR}


print("Module configuration:")
config = get_config()
for key, value in config.items():
    print(f"  {key}: {value}")

print("\n7. Module State:")

# Module-level state
_module_state = {"initialized": False, "call_count": 0, "last_called": None}


def initialize_module():
    """Initialize the module."""
    _module_state["initialized"] = True
    _module_state["last_called"] = "initialize"
    _module_state["call_count"] += 1
    return "Module initialized"


def get_module_state():
    """Get current module state."""
    return _module_state.copy()


def reset_module_state():
    """Reset module state."""
    _module_state.clear()
    _module_state.update({"initialized": False, "call_count": 0, "last_called": None})


# Test module state
print("Module state management:")
initialize_module()
print(f"State after initialization: {get_module_state()}")

print("\n8. Module Classes:")


class ModuleInfo:
    """Class to hold module information."""

    def __init__(self, name, version, author):
        self.name = name
        self.version = version
        self.author = author
        self.created = "2023-01-01"

    def __str__(self):
        return f"{self.name} v{self.version} by {self.author}"

    def get_info(self):
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "created": self.created,
        }


# Create module info
module_info = ModuleInfo("PythonModules", "1.0.0", "Python Course")
print(f"Module info: {module_info}")
print(f"Module details: {module_info.get_info()}")

print("\n9. Module Utilities:")


def get_module_attributes():
    """Get all module attributes."""
    return {
        "name": __name__,
        "file": __file__,
        "doc": __doc__,
        "all": __all__,
        "debug": DEBUG,
        "version": VERSION,
        "author": AUTHOR,
    }


def print_module_info():
    """Print comprehensive module information."""
    print("Module Information:")
    print("=" * 50)

    attrs = get_module_attributes()
    for key, value in attrs.items():
        print(f"{key:12}: {value}")

    print(f"{'state':12}: {get_module_state()}")
    print(f"{'info':12}: {module_info}")


print_module_info()

print("\n10. Module Testing:")


def test_module_functionality():
    """Test module functionality."""
    print("Testing module functionality:")

    # Test public function
    result = public_function()
    print(f"  Public function: {result}")

    # Test configuration
    config = get_config()
    print(f"  Configuration: {config}")

    # Test module state
    state = get_module_state()
    print(f"  State: {state}")

    # Test module info
    info = module_info.get_info()
    print(f"  Module info: {info}")

    return "All tests passed"


# Run tests
test_result = test_module_functionality()
print(f"Test result: {test_result}")

print("\n11. Module Cleanup:")


def cleanup_module():
    """Clean up module resources."""
    print("Cleaning up module...")
    reset_module_state()
    print("Module cleanup completed")


# Register cleanup function
import atexit

atexit.register(cleanup_module)

print("\n12. Module Constants:")

# Module constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
SUPPORTED_FORMATS = ["json", "xml", "csv"]
ERROR_MESSAGES = {
    "file_not_found": "File not found",
    "invalid_format": "Invalid format",
    "permission_denied": "Permission denied",
}


def get_constants():
    """Get module constants."""
    return {
        "max_retries": MAX_RETRIES,
        "default_timeout": DEFAULT_TIMEOUT,
        "supported_formats": SUPPORTED_FORMATS,
        "error_messages": ERROR_MESSAGES,
    }


print("Module constants:")
constants = get_constants()
for key, value in constants.items():
    print(f"  {key}: {value}")

print("\n13. Module Versioning:")

# Version information
VERSION_INFO = {"major": 1, "minor": 0, "patch": 0, "release": "stable"}


def get_version_string():
    """Get version as string."""
    v = VERSION_INFO
    return f"{v['major']}.{v['minor']}.{v['patch']}-{v['release']}"


def check_version_compatibility(required_version):
    """Check if module version is compatible."""
    current = VERSION_INFO
    required = required_version

    if current["major"] > required["major"]:
        return True
    elif current["major"] == required["major"]:
        return current["minor"] >= required["minor"]
    else:
        return False


print("Version information:")
print(f"  Version string: {get_version_string()}")
print(f"  Version info: {VERSION_INFO}")

# Test compatibility
test_version = {"major": 0, "minor": 9}
compatible = check_version_compatibility(test_version)
print(f"  Compatible with 0.9: {compatible}")

print("\n=== END OF MODULE ATTRIBUTES ===")
