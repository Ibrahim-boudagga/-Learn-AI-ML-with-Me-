# Practice Problems 1

print("=== PRACTICE PROBLEMS 1 ===\n")

# 9. Practice Problems
print("9. Practice Problems:")


# Problem 1: Count character frequencies
def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


text = "Hello World"
char_freq = count_characters(text)
print(f"Character frequencies in '{text}': {char_freq}")


# Problem 2: Find most common word
def most_common_word(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    if not word_count:
        return None

    return max(word_count.items(), key=lambda x: x[1])


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
most_common = most_common_word(words)
print(f"Most common word: {most_common}")


# Problem 3: Merge dictionaries with conflict resolution
def merge_dicts(dict1, dict2, conflict_strategy="first"):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            if conflict_strategy == "first":
                continue  # Keep first value
            elif conflict_strategy == "second":
                result[key] = value  # Use second value
            elif conflict_strategy == "combine":
                if isinstance(result[key], list) and isinstance(value, list):
                    result[key].extend(value)
                else:
                    result[key] = [result[key], value]
        else:
            result[key] = value

    return result


dict1 = {"a": 1, "b": 2, "c": [1, 2]}
dict2 = {"b": 3, "c": [3, 4], "d": 4}

merged_first = merge_dicts(dict1, dict2, "first")
merged_second = merge_dicts(dict1, dict2, "second")
merged_combine = merge_dicts(dict1, dict2, "combine")

print(f"Merge with 'first' strategy: {merged_first}")
print(f"Merge with 'second' strategy: {merged_second}")
print(f"Merge with 'combine' strategy: {merged_combine}")


# Problem 4: Invert dictionary
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted


original = {"a": 1, "b": 2, "c": 1, "d": 3}
inverted = invert_dict(original)
print(f"Original: {original}")
print(f"Inverted: {inverted}")

print("\n=== END ===")
