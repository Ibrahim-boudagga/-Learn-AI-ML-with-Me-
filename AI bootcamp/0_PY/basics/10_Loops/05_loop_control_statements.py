# Loop Control Statements

print("=== LOOP CONTROL STATEMENTS ===\n")

# Break statement
print("1. Break statement:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

# Continue statement
print("\n2. Continue statement (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# Pass statement
print("\n3. Pass statement:")
for i in range(5):
    if i < 3:
        pass  # Do nothing for now
    else:
        print(f"  Processing: {i}")

# Break in while loop
print("\n4. Break in while loop:")
count = 0
while True:
    count += 1
    if count > 5:
        break
    print(f"  Count: {count}")

# Continue in while loop
print("\n5. Continue in while loop (skip multiples of 3):")
num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        continue
    print(f"  {num}")

# Nested loops with break
print("\n6. Nested loops with break:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # Breaks inner loop only
        print(f"  ({i}, {j})")

# Break with else clause
print("\n7. Break with else clause:")
for i in range(5):
    if i == 10:  # This condition is never met
        break
else:
    print("  Loop completed without break")

print("\n=== END OF LOOP CONTROL STATEMENTS ===")
