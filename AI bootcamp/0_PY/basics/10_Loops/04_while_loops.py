# While Loops

print("=== WHILE LOOPS ===\n")

# Simple counter
print("1. Simple counter:")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

# User input simulation
print("\n2. Password check (simulated):")
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    if attempts == 2:  # Simulate correct password on second attempt
        print("  Access granted!")
        break
    else:
        print(f"  Wrong password. {max_attempts - attempts} attempts left")

# Countdown
print("\n3. Countdown:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  Blast off!")

# Sum until condition
print("\n4. Sum until reaching target:")
total = 0
number = 1
target = 10

while total < target:
    total += number
    number += 1
    print(f"  Added {number-1}, total: {total}")

# Infinite loop with break
print("\n5. Infinite loop with break:")
counter = 0
while True:
    counter += 1
    if counter > 5:
        break
    print(f"  Iteration: {counter}")

print("\n=== END OF WHILE LOOPS ===")
