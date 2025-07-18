# Variable Scope

print("=== VARIABLE SCOPE ===\n")

# Global variable
global_var = "I'm global"


# Function with local variable
def test_scope():
    local_var = "I'm local"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")


# Function that modifies global variable
def modify_global():
    global global_var
    global_var = "Modified global"
    print(f"Modified global_var to: {global_var}")


# Function with nonlocal variable (for nested functions)
def outer_function():
    outer_var = "I'm outer"

    def inner_function():
        nonlocal outer_var
        outer_var = "Modified outer"
        print(f"Inner function - outer_var: {outer_var}")

    print(f"Before inner function - outer_var: {outer_var}")
    inner_function()
    print(f"After inner function - outer_var: {outer_var}")


# Function that creates a new local variable with same name as global
def create_local():
    global_var = "I'm local with same name"
    print(f"Local variable: {global_var}")


# Function that demonstrates LEGB rule
def demonstrate_legb():
    # Local variable
    x = "local"

    def inner():
        # Enclosing variable
        x = "enclosing"

        def innermost():
            # Global variable
            global x
            x = "global"
            print(f"Innermost: {x}")

        print(f"Inner: {x}")
        innermost()
        print(f"Inner after innermost: {x}")

    print(f"Outer: {x}")
    inner()
    print(f"Outer after inner: {x}")


# Function with variable shadowing
def shadowing_example():
    x = "outer"

    def inner():
        x = "inner"  # Shadows the outer x
        print(f"Inner x: {x}")

    print(f"Outer x: {x}")
    inner()
    print(f"Outer x after inner: {x}")


# Testing variable scope
print("1. Basic scope test:")
test_scope()

print("\n2. Modifying global variable:")
print(f"Before modification - global_var: {global_var}")
modify_global()
print(f"After modification - global_var: {global_var}")

print("\n3. Nonlocal variable:")
outer_function()

print("\n4. Creating local variable with same name:")
create_local()
print(f"Global variable unchanged: {global_var}")

print("\n5. LEGB rule demonstration:")
demonstrate_legb()

print("\n6. Variable shadowing:")
shadowing_example()

print("\n7. Global variable access from different scopes:")


def function1():
    print(f"Function1 accessing global_var: {global_var}")


def function2():
    local_var = "Function2 local"
    print(f"Function2 local_var: {local_var}")
    print(f"Function2 accessing global_var: {global_var}")


function1()
function2()

print("\n8. Nested scope with multiple levels:")


def level1():
    x = "level1"

    def level2():
        y = "level2"

        def level3():
            z = "level3"
            print(f"Level3: x={x}, y={y}, z={z}")

        print(f"Level2: x={x}, y={y}")
        level3()

    print(f"Level1: x={x}")
    level2()


level1()

print("\n=== END OF VARIABLE SCOPE ===")
