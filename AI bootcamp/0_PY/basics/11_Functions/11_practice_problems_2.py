# Practice Problems - Part 2

print("=== PRACTICE PROBLEMS - PART 2 ===\n")


# Problem 6: Generate all permutations
def generate_permutations(items):
    if len(items) <= 1:
        return [items]

    permutations = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1 :]

        for perm in generate_permutations(remaining):
            permutations.append([current] + perm)

    return permutations


test_items = [1, 2, 3]
permutations = generate_permutations(test_items)
print("6. Generate all permutations:")
print(f"Permutations of {test_items}: {permutations}")


# Problem 7: Calculate compound interest
def compound_interest(principal, rate, time, compounds_per_year=1):
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (
        compounds_per_year * time
    )
    return amount - principal


principal = 1000
rate = 5  # 5%
time = 3  # 3 years

simple_interest = compound_interest(principal, rate, time, 1)
monthly_interest = compound_interest(principal, rate, time, 12)
daily_interest = compound_interest(principal, rate, time, 365)

print("\n7. Compound interest calculation:")
print(f"Principal: ${principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple interest: ${simple_interest:.2f}")
print(f"Monthly compound: ${monthly_interest:.2f}")
print(f"Daily compound: ${daily_interest:.2f}")


# Problem 8: Find longest common subsequence
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


test_pairs = [("ABCDGH", "AEDFHR"), ("AGGTAB", "GXTXAYB"), ("HELLO", "WORLD")]

print("\n8. Longest common subsequence:")
for str1, str2 in test_pairs:
    length = lcs(str1, str2)
    print(f"LCS of '{str1}' and '{str2}': {length}")


# Problem 9: Validate credit card number (Luhn algorithm)
def validate_credit_card(card_number):
    # Remove spaces and convert to list of digits
    digits = [int(d) for d in str(card_number).replace(" ", "")]

    # Double every second digit from right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all digits
    total = sum(digits)

    return total % 10 == 0


test_cards = [
    "4532015112830366",  # Valid
    "4532015112830367",  # Invalid
    "1234567890123456",  # Invalid
]

print("\n9. Credit card validation:")
for card in test_cards:
    valid = validate_credit_card(card)
    print(f"Card {card}: {'Valid' if valid else 'Invalid'}")


# Problem 10: Create a simple calculator function
def calculator(operation, *args):
    if not args:
        return "Error: No numbers provided"

    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        if len(args) < 2:
            return "Error: Need at least 2 numbers for division"
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
        return result
    elif operation == "subtract":
        if len(args) < 2:
            return "Error: Need at least 2 numbers for subtraction"
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    else:
        return "Error: Unknown operation"


print("\n10. Simple calculator:")
print(f"Add 1, 2, 3, 4: {calculator('add', 1, 2, 3, 4)}")
print(f"Multiply 2, 3, 4: {calculator('multiply', 2, 3, 4)}")
print(f"Divide 20, 4, 2: {calculator('divide', 20, 4, 2)}")
print(f"Subtract 10, 3, 2: {calculator('subtract', 10, 3, 2)}")

print("\n=== END OF PRACTICE PROBLEMS - PART 2 ===")
