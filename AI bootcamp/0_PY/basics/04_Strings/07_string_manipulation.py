# String Manipulation

print("=== STRING MANIPULATION ===\n")

text = "   Python Programming   "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lstrip: '{text.lstrip()}'")
print(f"Rstrip: '{text.rstrip()}'")

# Padding
name = "John"
print(f"Original: '{name}'")
print(f"Center (10): '{name.center(10)}'")
print(f"Left justify (10): '{name.ljust(10)}'")
print(f"Right justify (10): '{name.rjust(10)}'")
print()

# String manipulation methods:
# strip() : Remove whitespace from both ends
# lstrip() : Remove whitespace from left end
# rstrip() : Remove whitespace from right end
# center() : Center string with padding
# ljust() : Left justify with padding
# rjust() : Right justify with padding
