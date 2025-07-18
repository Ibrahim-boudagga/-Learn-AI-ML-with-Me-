# Practice Problems - Part 1

print("=== PRACTICE PROBLEMS - PART 1 ===\n")


# Problem 1: Find the second largest number
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[1]


test_numbers = [10, 5, 8, 12, 3, 9]
second_largest = find_second_largest(test_numbers)
print(f"Problem 1 - Second largest in {test_numbers}: {second_largest}")


# Problem 2: Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


duplicate_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = remove_duplicates(duplicate_list)
print(f"\nProblem 2 - Original: {duplicate_list}")
print(f"Without duplicates: {unique_list}")


# Problem 3: Find common elements between two lists
def find_common(list1, list2):
    return list(set(list1) & set(list2))


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common(list_a, list_b)
print(f"\nProblem 3 - List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common elements: {common}")


# Problem 4: Check if list is sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


sorted_test = [1, 2, 3, 4, 5]
unsorted_test = [1, 3, 2, 4, 5]
print(f"\nProblem 4 - {sorted_test} is sorted: {is_sorted(sorted_test)}")
print(f"{unsorted_test} is sorted: {is_sorted(unsorted_test)}")

print("\n=== END ===")
