# Built-in Functions with Functions

print("=== BUILT-IN FUNCTIONS WITH FUNCTIONS ===\n")

# map() function
# it applies a function to each item in an iterable and returns a new list:

numbers = [1, 2, 3, 4, 5]
squared_map = list(map(lambda x: x**2, numbers))
# result: [1, 4, 9, 16, 25]
print(f"1. map() result: {squared_map}")

# map() with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
summed = list(map(lambda x, y: x + y, list1, list2))
print(f"map() with multiple iterables: {summed}")

# filter() function
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
# result: [2, 4]
print(f"\n2. filter() result: {evens_filter}")

# filter() with None (removes falsy values)
mixed_list = [0, 1, False, True, "", "hello", [], [1, 2]]
truthy_values = list(filter(None, mixed_list))
print(f"filter() with None: {truthy_values}")

# reduce() function
from functools import reduce

sum_reduce = reduce(lambda x, y: x + y, numbers)
print(f"\n3. reduce() result: {sum_reduce}")

# reduce() with initial value
product_reduce = reduce(lambda x, y: x * y, numbers, 1)
print(f"reduce() with initial value: {product_reduce}")

# sorted() with key function
words = ["banana", "apple", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"\n4. sorted() by length: {sorted_by_length}")

# sorted() with multiple criteria
people = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
    {"name": "Charlie", "age": 25, "city": "Boston"},
    {"name": "David", "age": 35, "city": "NYC"},
]

sorted_by_age = sorted(people, key=lambda x: x["age"])
sorted_by_age_city = sorted(people, key=lambda x: (x["age"], x["city"]))
print(f"sorted() by age: {[p['name'] for p in sorted_by_age]}")
print(f"sorted() by age then city: {[p['name'] for p in sorted_by_age_city]}")

# max() and min() with key function
max_word = max(words, key=lambda x: len(x))
min_word = min(words, key=lambda x: len(x))
print(f"\n5. max() and min() with key:")
print(f"Longest word: {max_word}")
print(f"Shortest word: {min_word}")

# any() and all() with functions
numbers_list = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in numbers_list)
any_odd = any(x % 2 != 0 for x in numbers_list)
print(f"\n6. any() and all() with functions:")
print(f"All even: {all_even}")
print(f"Any odd: {any_odd}")

# zip() with functions
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Boston"]

combined = list(zip(names, ages, cities))
print(f"\n7. zip() result: {combined}")

# zip() with map()
name_age_pairs = list(zip(names, ages))
formatted = list(map(lambda pair: f"{pair[0]} is {pair[1]} years old", name_age_pairs))
print(f"zip() with map(): {formatted}")

# enumerate() with functions
fruits = ["apple", "banana", "orange"]
indexed_fruits = list(enumerate(fruits))
formatted_fruits = list(map(lambda pair: f"{pair[0]}: {pair[1]}", indexed_fruits))
print(f"\n8. enumerate() with functions:")
print(f"Indexed fruits: {formatted_fruits}")

# filter() with map() chain
numbers_chain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_and_mapped = list(
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers_chain))
)
print(f"\n9. filter() with map() chain:")
print(f"Even numbers squared: {filtered_and_mapped}")

# reduce() with filter() and map()
sum_even_squares = reduce(
    lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers_chain))
)
print(f"\n10. reduce() with filter() and map():")
print(f"Sum of even numbers squared: {sum_even_squares}")


# sorted() with custom key function
def get_second_letter(word):
    return word[1] if len(word) > 1 else word[0]


words_custom = ["python", "java", "javascript", "c++"]
sorted_by_second = sorted(words_custom, key=get_second_letter)
print(f"\n11. sorted() with custom function:")
print(f"Sorted by second letter: {sorted_by_second}")


# map() with multiple functions
def square(x):
    return x**2


def add_one(x):
    return x + 1


def double(x):
    return x * 2


numbers_multi = [1, 2, 3, 4, 5]
# Apply multiple functions using map()
squared = list(map(square, numbers_multi))
squared_plus_one = list(map(add_one, squared))
doubled_final = list(map(double, squared_plus_one))

print(f"\n12. map() with multiple functions:")
print(f"Original: {numbers_multi}")
print(f"Squared: {squared}")
print(f"Squared + 1: {squared_plus_one}")
print(f"Final (doubled): {doubled_final}")


# filter() with complex conditions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


numbers_complex = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101]
prime_palindromes = list(
    filter(lambda x: is_prime(x) and is_palindrome(x), numbers_complex)
)
print(f"\n13. filter() with complex conditions:")
print(f"Prime palindromes: {prime_palindromes}")

print("\n=== END OF BUILT-IN FUNCTIONS WITH FUNCTIONS ===")
