# Dynamic Imports

print("=== DYNAMIC IMPORTS ===\n")

import importlib

print("1. Basic Dynamic Module Import:")

# Dynamic module import
module_name = "math"
math_module = importlib.import_module(module_name)
print(f"Imported module: {math_module}")
print(f"Module PI: {math_module.pi}")
print(f"Module sqrt: {math_module.sqrt(16)}")

print("\n2. Dynamic Function Import:")


# Dynamic function import
def import_function(module_name, function_name):
    """Dynamically import a function from a module."""
    module = importlib.import_module(module_name)
    return getattr(module, function_name)


sqrt_func = import_function("math", "sqrt")
print(f"Dynamic sqrt function: {sqrt_func(16)}")

ceil_func = import_function("math", "ceil")
print(f"Dynamic ceil function: {ceil_func(4.3)}")

print("\n3. Dynamic Class Import:")


# Dynamic class import
def import_class(module_name, class_name):
    """Dynamically import a class from a module."""
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


# Example with datetime
datetime_class = import_class("datetime", "datetime")
now = datetime_class.now()
print(f"Dynamic datetime: {now}")

print("\n4. Conditional Dynamic Imports:")

# Try to import optional modules
optional_modules = ["numpy", "pandas", "matplotlib", "requests"]

print("Checking optional modules:")
for module_name in optional_modules:
    try:
        module = importlib.import_module(module_name)
        print(f"  ✓ {module_name} is available")
    except ImportError:
        print(f"  ✗ {module_name} is not available")

print("\n5. Dynamic Import with Fallback:")


def safe_import_module(module_name, fallback_module=None):
    """Safely import a module with fallback."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        if fallback_module:
            print(f"  {module_name} not available, using {fallback_module}")
            return importlib.import_module(fallback_module)
        return None


# Test with fallback
numpy_module = safe_import_module("numpy", "math")
if numpy_module:
    print(f"  Using module: {numpy_module.__name__}")

print("\n6. Dynamic Import with Configuration:")

# Configuration-based imports
import os


def get_math_module():
    """Get math module based on configuration."""
    preferred_module = os.getenv("MATH_MODULE", "math")

    if preferred_module == "numpy":
        try:
            return importlib.import_module("numpy")
        except ImportError:
            print("  NumPy not available, falling back to math")
            return importlib.import_module("math")
    else:
        return importlib.import_module("math")


math_lib = get_math_module()
print(f"  Using math library: {math_lib.__name__}")

print("\n7. Dynamic Import with Plugin System:")


class PluginLoader:
    """Load plugins dynamically."""

    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name, module_name):
        """Load a plugin from a module."""
        try:
            module = importlib.import_module(module_name)
            plugin_class = getattr(module, plugin_name)
            self.plugins[plugin_name] = plugin_class()
            print(f"  Loaded plugin: {plugin_name}")
            return True
        except (ImportError, AttributeError) as e:
            print(f"  Failed to load plugin {plugin_name}: {e}")
            return False

    def get_plugin(self, plugin_name):
        """Get a loaded plugin."""
        return self.plugins.get(plugin_name)

    def list_plugins(self):
        """List all loaded plugins."""
        return list(self.plugins.keys())


# Test plugin loader
loader = PluginLoader()
loader.load_plugin("Calculator", "math")  # This will fail, but demonstrates the concept
print(f"  Loaded plugins: {loader.list_plugins()}")

print("\n8. Dynamic Import with Module Reloading:")


def reload_module(module_name):
    """Reload a module dynamically."""
    try:
        module = importlib.import_module(module_name)
        reloaded_module = importlib.reload(module)
        print(f"  Reloaded module: {module_name}")
        return reloaded_module
    except Exception as e:
        print(f"  Failed to reload {module_name}: {e}")
        return None


# Note: reloading is generally not recommended in production
print("Module reloading (demonstration):")
reload_module("math")

print("\n9. Dynamic Import with Submodules:")


def import_submodule(parent_module, submodule_name):
    """Import a submodule dynamically."""
    try:
        full_module_name = f"{parent_module}.{submodule_name}"
        return importlib.import_module(full_module_name)
    except ImportError:
        print(f"  Submodule {full_module_name} not found")
        return None


# Test submodule import
datetime_module = import_submodule("datetime", "datetime")
if datetime_module:
    print(f"  Imported submodule: {datetime_module}")

print("\n10. Dynamic Import with Error Handling:")


def robust_import(module_name, item_name=None):
    """Robustly import a module or item from a module."""
    try:
        module = importlib.import_module(module_name)

        if item_name:
            try:
                item = getattr(module, item_name)
                return item
            except AttributeError:
                print(f"  Item '{item_name}' not found in module '{module_name}'")
                return None
        else:
            return module

    except ImportError as e:
        print(f"  Module '{module_name}' not found: {e}")
        return None
    except Exception as e:
        print(f"  Unexpected error importing '{module_name}': {e}")
        return None


# Test robust import
print("Robust import testing:")
math_module = robust_import("math")
sqrt_func = robust_import("math", "sqrt")
nonexistent = robust_import("nonexistent_module")
nonexistent_func = robust_import("math", "nonexistent_function")

print(f"  math module: {math_module is not None}")
print(f"  sqrt function: {sqrt_func is not None}")
print(f"  nonexistent module: {nonexistent is not None}")
print(f"  nonexistent function: {nonexistent_func is not None}")

print("\n11. Dynamic Import with Caching:")


class ModuleCache:
    """Cache for dynamically imported modules."""

    def __init__(self):
        self._cache = {}

    def get_module(self, module_name):
        """Get a module from cache or import it."""
        if module_name not in self._cache:
            try:
                self._cache[module_name] = importlib.import_module(module_name)
                print(f"  Cached module: {module_name}")
            except ImportError:
                print(f"  Failed to import: {module_name}")
                self._cache[module_name] = None

        return self._cache[module_name]

    def clear_cache(self):
        """Clear the module cache."""
        self._cache.clear()
        print("  Module cache cleared")

    def list_cached_modules(self):
        """List all cached modules."""
        return list(self._cache.keys())


# Test module cache
cache = ModuleCache()
math_module = cache.get_module("math")
random_module = cache.get_module("random")
print(f"  Cached modules: {cache.list_cached_modules()}")

print("\n12. Dynamic Import with Validation:")


def validate_import(module_name, required_attributes=None):
    """Import a module and validate it has required attributes."""
    try:
        module = importlib.import_module(module_name)

        if required_attributes:
            missing_attributes = []
            for attr in required_attributes:
                if not hasattr(module, attr):
                    missing_attributes.append(attr)

            if missing_attributes:
                print(
                    f"  Module '{module_name}' missing attributes: {missing_attributes}"
                )
                return None
            else:
                print(f"  Module '{module_name}' validation passed")
                return module
        else:
            return module

    except ImportError as e:
        print(f"  Failed to import '{module_name}': {e}")
        return None


# Test validation
print("Import validation testing:")
math_valid = validate_import("math", ["pi", "sqrt", "cos"])
random_valid = validate_import("random", ["randint", "choice"])
invalid_valid = validate_import("math", ["nonexistent"])

print(f"  math validation: {math_valid is not None}")
print(f"  random validation: {random_valid is not None}")
print(f"  invalid validation: {invalid_valid is not None}")

print("\n13. Dynamic Import with Performance Monitoring:")

import time


def timed_import(module_name):
    """Import a module and measure the time."""
    start_time = time.time()
    try:
        module = importlib.import_module(module_name)
        end_time = time.time()
        import_time = end_time - start_time
        print(f"  Imported '{module_name}' in {import_time:.4f} seconds")
        return module
    except ImportError as e:
        print(f"  Failed to import '{module_name}': {e}")
        return None


# Test timed imports
print("Timed import testing:")
timed_import("math")
timed_import("random")
timed_import("datetime")

print("\n=== END OF DYNAMIC IMPORTS ===")
