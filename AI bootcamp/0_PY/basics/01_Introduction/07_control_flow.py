# Control Flow - If Statements

print("=== CONTROL FLOW - IF STATEMENTS ===\n")

ages = [15, 18, 25, 12, 30]

for age in ages:
    if age >= 18:
        print(f"Age {age}: Adult")
    elif age >= 13:
        print(f"Age {age}: Teenager")
    else:
        print(f"Age {age}: Child")
print()

# if, elif, else statements for decision making
# Conditions use comparison operators: ==, !=, <, >, <=, >=
# elif means "else if" - only checked if previous conditions are False
