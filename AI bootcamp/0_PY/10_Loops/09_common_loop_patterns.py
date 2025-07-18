# Common Loop Patterns

print("=== COMMON LOOP PATTERNS ===\n")

# Accumulator pattern
print("1. Accumulator - Sum numbers:")
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(f"  Total: {total}")

# Counter pattern
print("\n2. Counter - Count characters:")
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"  Character count: {char_count}")

# Filter pattern
print("\n3. Filter - Even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"  Even numbers: {even_numbers}")

# Map pattern
print("\n4. Map - Double numbers:")
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(f"  Doubled: {doubled}")

# Search pattern
print("\n5. Search - Find first occurrence:")
target = 7
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"  Found {target}: {found}")

# Maximum pattern
print("\n6. Maximum - Find largest number:")
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(f"  Maximum: {max_num}")

# Minimum pattern
print("\n7. Minimum - Find smallest number:")
min_num = numbers[0]
for num in numbers[1:]:
    if num < min_num:
        min_num = num
print(f"  Minimum: {min_num}")

# Average pattern
print("\n8. Average - Calculate mean:")
sum_nums = 0
count = 0
for num in numbers:
    sum_nums += num
    count += 1
average = sum_nums / count
print(f"  Average: {average}")

# Grouping pattern
print("\n9. Grouping - Group by parity:")
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"  Even: {even}")
print(f"  Odd: {odd}")

# Transformation pattern
print("\n10. Transformation - Convert to uppercase:")
words = ["python", "programming", "language"]
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())
print(f"  Uppercase: {uppercase_words}")

print("\n=== END OF COMMON LOOP PATTERNS ===")
