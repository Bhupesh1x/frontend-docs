"""
=============================================================================
 LOOPS
=============================================================================
 Loops allow you to execute a block of code repeatedly.
 Python has two main loop types: while and for.
=============================================================================
"""

# =============================================================================
# WHILE LOOP
# =============================================================================

# Basic while loop - runs while condition is True
i = 0
while i < 5:
    print(f"Iteration: {i}")
    i += 1  # Don't forget to update the counter!

# Output: 0, 1, 2, 3, 4

print("---")

# Print multiples of 10
i = 10
while i <= 50:
    print(i)  # 10, 20, 30, 40, 50
    i += 10


# =============================================================================
# FOR LOOP WITH RANGE
# =============================================================================

# range(stop) - 0 to stop-1
print("\nrange(5):")
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
print("\nrange(10, 15):")
for i in range(10, 15):
    print(i)  # 10, 11, 12, 13, 14

# range(start, stop, step) - with custom step
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Counting backwards (negative step)
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Using reversed() - alternative for counting backwards
print("\nreversed(range(1, 6)):")
for i in reversed(range(1, 6)):
    print(i)  # 5, 4, 3, 2, 1


# =============================================================================
# FOR LOOP WITH ITERABLES
# =============================================================================

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string
for char in "Hello":
    print(char)  # H, e, l, l, o

# Looping with index using enumerate()
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start enumerate from different index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry


# =============================================================================
# NESTED LOOPS
# =============================================================================

print("\nNested loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# Creating a grid
print("\nGrid pattern:")
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row


# =============================================================================
# LOOP CONTROL STATEMENTS
# =============================================================================

# break - exit the loop immediately
print("\nUsing break:")
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)  # 0, 1, 2, 3, 4

# continue - skip to next iteration
print("\nUsing continue:")
for i in range(10):
    if i == 5:
        continue  # Skip when i is 5
    print(i)  # 0, 1, 2, 3, 4, 6, 7, 8, 9

# pass - placeholder, does nothing
print("\nUsing pass:")
for i in range(3):
    pass  # Placeholder for future code
print("Loop with pass completed")

# ⚠️ pass is needed because Python doesn't allow empty blocks


# =============================================================================
# COMBINING BREAK AND CONTINUE
# =============================================================================

print("\nBreak and continue combined:")
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)      # 0, 1, 2, 4, 5, 6


# =============================================================================
# ELSE WITH LOOPS
# =============================================================================

# The else block runs if loop completes without break

print("\nLoop with else (no break):")
for i in range(3):
    print(i)
else:
    print("Loop completed normally")  # Runs

print("\nLoop with else (with break):")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed normally")  # Doesn't run (break occurred)


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Example 1: Count occurrences
def count_occurrences(items, target):
    """Count how many times target appears in items."""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

print(count_occurrences([1, 2, 5, 4, 5], 5))  # 2

# Example 2: Find first match
def find_first(items, target):
    """Find index of first occurrence, -1 if not found."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

print(find_first([1, 2, 3, 4, 5], 3))  # 2
print(find_first([1, 2, 3, 4, 5], 9))  # -1

# Example 3: Sum with early exit
def sum_until_negative(numbers):
    """Sum numbers until a negative is encountered."""
    total = 0
    for num in numbers:
        if num < 0:
            break
        total += num
    return total

print(sum_until_negative([1, 2, 3, -1, 4, 5]))  # 6

# Example 4: Filter with continue
def get_positive_numbers(numbers):
    """Return only positive numbers."""
    result = []
    for num in numbers:
        if num <= 0:
            continue
        result.append(num)
    return result

print(get_positive_numbers([1, -2, 3, 0, -4, 5]))  # [1, 3, 5]


# =============================================================================
# LOOPING PATTERNS
# =============================================================================

# Looping with two lists using zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("\nUsing zip:")
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Creating lists with loops
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares: {squares}")  # [1, 4, 9, 16, 25]

# List comprehension (more Pythonic, but covered separately)
# squares = [i ** 2 for i in range(1, 6)]


# =============================================================================
# INFINITE LOOPS (USE WITH CAUTION!)
# =============================================================================

# while True creates an infinite loop - must have break condition!
"""
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # Essential! Without this, loop runs forever
"""


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Forgetting to update loop variable
"""
i = 0
while i < 5:
    print(i)
    # Forgot i += 1 - infinite loop!
"""

# 2. Off-by-one errors with range
# range(5) gives 0-4, not 0-5
# range(1, 5) gives 1-4, not 1-5

# 3. Modifying list while iterating
"""
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)  # ❌ Don't modify list during iteration!
"""
# Solution: iterate over a copy or use list comprehension
items = [1, 2, 3, 4, 5]
items = [item for item in items if item % 2 != 0]  # [1, 3, 5]


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use enumerate() instead of manual counter
# Instead of:
i = 0
for item in items:
    print(i, item)
    i += 1

# Do:
for i, item in enumerate(items):
    print(i, item)

# 2. Use zip() for parallel iteration
# 3. Use range(len(list)) only when you need to modify by index
# 4. Prefer for loops when iteration count is known
# 5. Use while loops for unknown/conditional iterations
