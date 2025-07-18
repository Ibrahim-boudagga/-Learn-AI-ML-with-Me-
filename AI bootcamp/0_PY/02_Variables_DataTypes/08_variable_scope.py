# Variable Scope

print("=== VARIABLE SCOPE ===\n")

global_var = "I'm a global variable"


def test_function():
    local_var = "I'm a local variable"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")


test_function()
print(f"Outside function - global_var: {global_var}")
# print(f"Outside function - local_var: {local_var}")  # This would raise an error
print()

# Global variables are accessible throughout the module
# Local variables are only accessible within their function
# Variables created inside a function are local to that function
# Use global keyword to modify global variables inside functions
