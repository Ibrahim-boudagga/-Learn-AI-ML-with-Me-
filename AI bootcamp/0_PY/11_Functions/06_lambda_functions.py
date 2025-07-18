# Lambda Functions

print("=== LAMBDA FUNCTIONS ===\n")

# Basic lambda functions
square_lambda = lambda x: x**2
add_lambda = lambda x, y: x + y
multiply_lambda = lambda x, y, z: x * y * z

print("1. Basic lambda functions:")
print(f"Square of 4: {square_lambda(4)}")
print(f"Sum of 3 and 5: {add_lambda(3, 5)}")
print(f"Product of 2, 3, 4: {multiply_lambda(2, 3, 4)}")

# Lambda with conditional logic
is_even = lambda x: x % 2 == 0
get_sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
is_adult = lambda age: "Adult" if age >= 18 else "Minor"

print("\n2. Lambda with conditional logic:")
test_numbers = [2, 3, 0, -1, 5]
for num in test_numbers:
    even = is_even(num)
    sign = get_sign(num)
    print(f"{num} is even: {even}, sign: {sign}")

ages = [15, 20, 25, 17]
for age in ages:
    status = is_adult(age)
    print(f"Age {age}: {status}")

# Lambda with string operations
uppercase = lambda s: s.upper()
reverse = lambda s: s[::-1]
length_check = lambda s: "Long" if len(s) > 5 else "Short"

print("\n3. Lambda with string operations:")
words = ["hello", "python", "programming", "ai"]
for word in words:
    upper = uppercase(word)
    rev = reverse(word)
    length = length_check(word)
    print(f"'{word}' -> uppercase: '{upper}', reverse: '{rev}', length: {length}")

# Lambda with list operations
double_list = lambda lst: [x * 2 for x in lst]
filter_positive = lambda lst: [x for x in lst if x > 0]
sum_squares = lambda lst: sum(x**2 for x in lst)

print("\n4. Lambda with list operations:")
numbers = [1, 2, 3, 4, 5, -1, -2]
doubled = double_list(numbers)
positive = filter_positive(numbers)
squares_sum = sum_squares(numbers)
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Positive: {positive}")
print(f"Sum of squares: {squares_sum}")

# Lambda with dictionary operations
get_value = lambda d, key: d.get(key, "Not found")
filter_dict = lambda d, condition: {k: v for k, v in d.items() if condition(k, v)}

print("\n5. Lambda with dictionary operations:")
person = {"name": "Alice", "age": 25, "city": "New York"}
name = get_value(person, "name")
age = get_value(person, "age")
job = get_value(person, "job")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")

# Filter by value
adults = filter_dict(person, lambda k, v: k == "age" and v >= 18)
print(f"Adults: {adults}")

# Lambda with multiple conditions
complex_check = lambda x: (
    "positive even"
    if x > 0 and x % 2 == 0
    else "positive odd" if x > 0 else "negative" if x < 0 else "zero"
)

print("\n6. Lambda with multiple conditions:")
test_nums = [-3, 0, 2, 3, 4, 5]
for num in test_nums:
    result = complex_check(num)
    print(f"{num}: {result}")

# Lambda with default arguments
power = lambda x, n=2: x**n
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"

print("\n7. Lambda with default arguments:")
print(f"5 squared: {power(5)}")
print(f"5 cubed: {power(5, 3)}")
print(f"Greeting: {greet('Alice')}")
print(f"Custom greeting: {greet('Bob', 'Good morning')}")

# Lambda in built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() with lambda
squared = list(map(lambda x: x**2, numbers))
print(f"\n8. map() with lambda:")
print(f"Squared: {squared}")

# filter() with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# sorted() with lambda
words = ["banana", "apple", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda x: len(x))
sorted_by_last_char = sorted(words, key=lambda x: x[-1])
print(f"Sorted by length: {sorted_by_length}")
print(f"Sorted by last character: {sorted_by_last_char}")

# reduce() with lambda
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Product: {product}")
print(f"Maximum: {max_num}")

print("\n=== END OF LAMBDA FUNCTIONS ===")
