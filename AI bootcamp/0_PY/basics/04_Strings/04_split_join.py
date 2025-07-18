# String Splitting and Joining

print("=== STRING SPLITTING AND JOINING ===\n")

csv_data = "apple,banana,orange,grape"
print(f"CSV data: '{csv_data}'")
fruits = csv_data.split(",")
print(f"Split fruits: {fruits}")

words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"Joined words: '{joined}'")

# Split by multiple delimiters
text_with_spaces = "apple, banana; orange. grape"
import re

cleaned = re.split(r"[,;\s.]+", text_with_spaces)
print(f"Split by multiple delimiters: {cleaned}")
print()

# Split and join methods:
# split() : Split string into list
# join() : Join list into string
# splitlines() : Split by line breaks
# partition() : Split into 3 parts (before, separator, after)
