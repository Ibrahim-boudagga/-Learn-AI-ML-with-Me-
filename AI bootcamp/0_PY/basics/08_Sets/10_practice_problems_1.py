# Practice Problems 1

print("=== PRACTICE PROBLEMS 1 ===\n")

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))


test_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = remove_duplicates(test_list)
print(f"Original: {test_list}")
print(f"Without duplicates: {unique_list}")


# Problem 2: Find common elements between two lists
def find_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common(list_a, list_b)
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common elements: {common}")


# Problem 3: Check if two lists have any common elements
def has_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return not set1.isdisjoint(set2)


list_c = [1, 2, 3]
list_d = [4, 5, 6]
list_e = [3, 4, 5]

print(f"List C and D have common elements: {has_common_elements(list_c, list_d)}")
print(f"List C and E have common elements: {has_common_elements(list_c, list_e)}")


# Problem 4: Find unique elements in either list but not both
def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 ^ set2)


unique = unique_elements(list_a, list_b)
print(f"Unique elements (not in both): {unique}")


# Problem 5: Check if string has all unique characters
def has_unique_chars(text):
    return len(text) == len(set(text))


test_strings = ["python", "hello", "algorithm", "unique"]
for text in test_strings:
    result = has_unique_chars(text)
    print(f"'{text}' has unique characters: {result}")

print("\n=== END ===")
