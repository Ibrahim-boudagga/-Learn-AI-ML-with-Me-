# String Search and Replace

print("=== STRING SEARCH AND REPLACE ===\n")

sentence = "Python is awesome and Python is powerful"
print(f"Original: '{sentence}'")
print(f"Find 'Python': {sentence.find('Python')}")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Replace 'Python' with 'Java': '{sentence.replace('Python', 'Java')}'")
print(f"Replace first 'Python' only: '{sentence.replace('Python', 'Java', 1)}'")
print()

# Search and replace methods:
# find() : Find first occurrence (returns index or -1)
# count() : Count occurrences of substring
# replace() : Replace substring with another
# index() : Find first occurrence (raises error if not found)
# rfind() : Find last occurrence from right
