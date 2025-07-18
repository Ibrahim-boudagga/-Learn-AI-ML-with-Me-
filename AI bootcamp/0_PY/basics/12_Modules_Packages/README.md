# Python Modules and Packages

This section covers Python modules and packages, including creating modules, using built-in modules, import techniques, and advanced package concepts.

## Course Structure

### 1. Creating Simple Modules
**File:** `01_creating_simple_modules.py`
- Creating module-like classes
- Static methods and class methods
- Module constants and configuration
- Error handling in modules

### 2. Built-in Modules
**File:** `02_builtin_modules.py`
- Math module (sqrt, pi, e, ceil, floor, etc.)
- Random module (randint, choice, shuffle, etc.)
- Datetime module (now, strftime, timedelta, etc.)
- OS module (getcwd, listdir, environ, etc.)
- Sys module (version, platform, path, etc.)
- Collections module (defaultdict, Counter, namedtuple, deque, etc.)
- Re module (findall, sub, match, etc.)
- JSON module (dumps, loads, etc.)
- Pickle module (dumps, loads, etc.)
- Urllib module (urlparse, parse_qs, etc.)

### 3. Import Techniques
**File:** `03_import_techniques.py`
- Import with aliases
- Import specific functions
- Conditional imports
- Relative imports (simulated)
- Import from submodules
- Custom namespaces
- Function renaming
- Multiple imports
- Exception handling for imports
- Lazy loading
- Version checking
- Environment-based imports
- Custom import functions

### 4. Collections Module
**File:** `04_collections_module.py`
- DefaultDict with different factories
- Counter operations and methods
- NamedTuple with defaults and type hints
- Deque operations and rotation
- OrderedDict with move_to_end
- ChainMap for multiple dictionaries
- Practical examples and use cases

### 5. JSON Module
**File:** `05_json_module.py`
- Python object to JSON conversion
- JSON to Python object conversion
- Different data types handling
- Custom objects and encoders
- File operations (simulated)
- Pretty printing and sorting
- Unicode handling
- JSON validation
- Nested structures
- Date handling
- Error handling

### 6. Pickle Module
**File:** `06_pickle_module.py`
- Basic pickle operations
- Different data types
- Custom objects
- Functions and lambda functions
- Classes and instances
- Nested structures
- Error handling
- Different protocols
- File operations (simulated)
- Security considerations
- Pickle vs JSON comparison

### 7. Creating Package Structure
**File:** `07_creating_package_structure.py`
- Basic package structure
- Calculator package
- StringUtils package
- Configuration modules
- Singleton logger
- Data formatters (JSON, XML, CSV, YAML)
- Plugin system
- File manager
- Data validator

### 8. Module Attributes
**File:** `08_module_attributes.py`
- Basic module attributes
- Module information
- Module path and location
- Module documentation
- Module exports
- Module configuration
- Module state management
- Module classes
- Module utilities
- Module testing
- Module cleanup
- Module constants
- Module versioning

### 9. Dynamic Imports
**File:** `09_dynamic_imports.py`
- Basic dynamic module import
- Dynamic function import
- Dynamic class import
- Conditional dynamic imports
- Dynamic import with fallback
- Configuration-based imports
- Plugin system with dynamic imports
- Module reloading
- Submodule imports
- Error handling
- Module caching
- Import validation
- Performance monitoring

### 10. Practice Problems - Part 1
**File:** `10_practice_problems_1.py`
- Configuration module with class methods
- Singleton logger with advanced features
- Data formatter factory (JSON, XML, CSV, YAML)
- Plugin system with multiple plugins

### 11. Practice Problems - Part 2
**File:** `11_practice_problems_2.py`
- File manager with comprehensive operations
- Data validator with multiple validation types
- Cache implementation with TTL and LRU
- Rate limiter with time windows

## How to Use These Files

### Running Individual Files
Each file can be run independently to learn specific concepts:

```bash
# Run basic module creation
python 01_creating_simple_modules.py

# Run built-in modules examples
python 02_builtin_modules.py

# Run import techniques
python 03_import_techniques.py

# Run collections module examples
python 04_collections_module.py

# Run JSON module examples
python 05_json_module.py

# Run pickle module examples
python 06_pickle_module.py

# Run package structure examples
python 07_creating_package_structure.py

# Run module attributes examples
python 08_module_attributes.py

# Run dynamic imports examples
python 09_dynamic_imports.py

# Run practice problems
python 10_practice_problems_1.py
python 11_practice_problems_2.py
```

### Running All Files Sequentially
To run all files in order:

```bash
# Run all files in sequence
for file in *.py; do
    echo "Running $file..."
    python "$file"
    echo "----------------------------------------"
done
```

## Key Learning Objectives

### Module Creation
- Understand how to create reusable modules
- Learn to use static methods and class methods
- Master module configuration and state management

### Built-in Modules
- Explore Python's standard library modules
- Learn mathematical operations with math module
- Understand random number generation
- Work with dates and times
- Handle file system operations
- Process collections efficiently

### Import Techniques
- Master different import styles
- Learn conditional and dynamic imports
- Understand import error handling
- Explore lazy loading techniques

### Advanced Collections
- Use defaultdict for automatic key creation
- Count elements with Counter
- Create structured data with namedtuple
- Implement efficient queues with deque
- Maintain order with OrderedDict
- Chain multiple dictionaries with ChainMap

### Data Serialization
- Convert Python objects to JSON and back
- Serialize complex objects with pickle
- Handle different data formats
- Work with file I/O operations

### Package Development
- Create organized package structures
- Implement plugin systems
- Build configuration management
- Design singleton patterns
- Create factory patterns

### Dynamic Programming
- Import modules at runtime
- Build plugin architectures
- Implement configuration-driven imports
- Handle import errors gracefully

## Practice Problems

The practice problems cover real-world scenarios:

1. **Configuration Management**: Create a centralized configuration system
2. **Logging System**: Implement a singleton logger with multiple features
3. **Data Formatting**: Build a factory for different output formats
4. **Plugin Architecture**: Create an extensible plugin system
5. **File Operations**: Build a comprehensive file management system
6. **Data Validation**: Create a robust validation framework
7. **Caching System**: Implement an LRU cache with TTL
8. **Rate Limiting**: Build a rate limiter for API protection

## Tips for Learning

1. **Start with Basics**: Begin with simple module creation before moving to advanced concepts
2. **Experiment**: Modify the examples to see how changes affect behavior
3. **Combine Concepts**: Try combining multiple modules in your own projects
4. **Practice Regularly**: Use the practice problems to reinforce your learning
5. **Read Documentation**: Explore the official Python documentation for each module
6. **Build Projects**: Create your own modules and packages to apply what you've learned

## Common Patterns

- **Singleton Pattern**: For loggers and configuration managers
- **Factory Pattern**: For creating different types of objects
- **Plugin Pattern**: For extensible systems
- **Configuration Pattern**: For centralized settings management
- **Cache Pattern**: For performance optimization
- **Rate Limiting Pattern**: For API protection

## Next Steps

After completing this section, you should be able to:
- Create well-structured Python modules and packages
- Use Python's built-in modules effectively
- Implement advanced import strategies
- Build extensible systems with plugins
- Handle data serialization and validation
- Design robust configuration and logging systems

This foundation will prepare you for building larger Python applications and working with external libraries and frameworks. 