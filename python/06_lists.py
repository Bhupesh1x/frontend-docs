"""
=============================================================================
 LISTS
=============================================================================
 Lists are ordered, mutable collections that can hold items of any type.
 They are one of the most commonly used data structures in Python.
=============================================================================
"""

# =============================================================================
# CREATING LISTS
# =============================================================================

# Basic list creation
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", True, None, 3.14]  # Can mix types

# Empty list
empty_list = []
empty_list2 = list()

# List from string
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# List from range
nums = list(range(5))  # [0, 1, 2, 3, 4]

# List with repeated elements
zeros = [0] * 5  # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]


# =============================================================================
# ACCESSING ELEMENTS
# =============================================================================

fruits = ["apple", "banana", "cherry", "date"]
#          0         1         2         3      (positive)
#         -4        -3        -2        -1      (negative)

# Indexing
print(fruits[0])    # apple (first)
print(fruits[2])    # cherry
print(fruits[-1])   # date (last)
print(fruits[-2])   # cherry

# Length
print(len(fruits))  # 4


# =============================================================================
# LIST SLICING
# =============================================================================

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end]
print(nums[2:5])    # [2, 3, 4]
print(nums[:4])     # [0, 1, 2, 3] (from start)
print(nums[6:])     # [6, 7, 8, 9] (to end)
print(nums[:])      # Full copy

# With step [start:end:step]
print(nums[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(nums[1::2])   # [1, 3, 5, 7, 9] (every 2nd from index 1)

# Reverse
print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Negative indices in slicing
print(nums[-3:])    # [7, 8, 9] (last 3)
print(nums[:-3])    # [0, 1, 2, 3, 4, 5, 6] (all except last 3)

def get_last_three(items):
    """Return last 3 elements."""
    return items[-3:]

print(get_last_three([1, 2, 3, 4, 5]))  # [3, 4, 5]


# =============================================================================
# MODIFYING LISTS (LISTS ARE MUTABLE!)
# =============================================================================

fruits = ["apple", "banana", "cherry"]

# Change element
fruits[0] = "apricot"
print(fruits)  # ['apricot', 'banana', 'cherry']

# Change multiple elements with slicing
fruits[1:3] = ["blueberry", "coconut"]
print(fruits)  # ['apricot', 'blueberry', 'coconut']


# =============================================================================
# ADDING ELEMENTS
# =============================================================================

nums = [1, 2, 3]

# append() - add to end
nums.append(4)
print(nums)  # [1, 2, 3, 4]

# insert() - add at specific position
nums.insert(0, 0)   # Insert 0 at index 0
print(nums)  # [0, 1, 2, 3, 4]

nums.insert(2, 99)  # Insert 99 at index 2
print(nums)  # [0, 1, 99, 2, 3, 4]

# extend() - add multiple elements
nums.extend([5, 6, 7])
print(nums)  # [0, 1, 99, 2, 3, 4, 5, 6, 7]

# Using + operator (creates new list)
more_nums = nums + [8, 9]
print(more_nums)


# =============================================================================
# REMOVING ELEMENTS
# =============================================================================

fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - remove first occurrence of value
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# pop() - remove and return element
# Default: removes last element
last = fruits.pop()
print(last)    # date
print(fruits)  # ['apple', 'cherry', 'banana']

# pop(index) - remove at specific index
first = fruits.pop(0)
print(first)   # apple
print(fruits)  # ['cherry', 'banana']

# del - delete by index or slice
nums = [0, 1, 2, 3, 4, 5]
del nums[0]      # Remove index 0
print(nums)      # [1, 2, 3, 4, 5]

del nums[1:3]    # Remove slice
print(nums)      # [1, 4, 5]

# clear() - remove all elements
nums.clear()
print(nums)      # []


# =============================================================================
# SEARCHING IN LISTS
# =============================================================================

nums = [10, 20, 30, 40, 30, 50]

# 'in' operator - check existence
print(30 in nums)   # True
print(99 in nums)   # False
print(30 not in nums)  # False

# index() - find position of first occurrence
print(nums.index(30))  # 2
# print(nums.index(99))  # ❌ ValueError if not found

# count() - count occurrences
print(nums.count(30))  # 2
print(nums.count(99))  # 0

# Safe find function
def find_index(items, target):
    """Find index of target, return -1 if not found."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

# Or using try/except
def find_index_safe(items, target):
    try:
        return items.index(target)
    except ValueError:
        return -1


# =============================================================================
# ITERATING OVER LISTS
# =============================================================================

fruits = ["apple", "banana", "cherry"]

# Simple iteration
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With index using range
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Iterate two lists together with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")


# =============================================================================
# LIST FUNCTIONS
# =============================================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Built-in functions
print(len(nums))    # 8 (length)
print(sum(nums))    # 31 (sum of elements)
print(min(nums))    # 1 (minimum)
print(max(nums))    # 9 (maximum)

# Manual implementations
def get_sum(items):
    total = 0
    for item in items:
        total += item
    return total

def get_max(items):
    maximum = items[0]
    for item in items:
        if item > maximum:
            maximum = item
    return maximum

def get_min(items):
    minimum = items[0]
    for item in items:
        if item < minimum:
            minimum = item
    return minimum


# =============================================================================
# SORTING LISTS
# =============================================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - modifies list in place
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort descending
nums.sort(reverse=True)
print(nums)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_nums = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_nums)  # [1, 1, 3, 4, 5]

# reverse() - reverse in place
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]


# =============================================================================
# COPYING LISTS
# =============================================================================

original = [1, 2, 3]

# ⚠️ This does NOT copy - both point to same list
not_a_copy = original
not_a_copy.append(4)
print(original)  # [1, 2, 3, 4] - original changed!

# Proper ways to copy
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(99)
print(original)  # [1, 2, 3] - original unchanged


# =============================================================================
# UNPACKING (DESTRUCTURING)
# =============================================================================

# Basic unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

# With * for remaining elements
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)  # 1 [2, 3, 4] 5


# =============================================================================
# LISTS AS STACKS
# =============================================================================

# Lists can be used as stacks (LIFO - Last In, First Out)
stack = []

# Push (add to top)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop (remove from top)
top = stack.pop()
print(top)    # 3
print(stack)  # [1, 2]


# =============================================================================
# NESTED LISTS (2D LISTS)
# =============================================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0])      # [1, 2, 3] (first row)
print(matrix[0][0])   # 1 (first element)
print(matrix[1][2])   # 6 (row 1, col 2)

# Iterate
for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Count occurrences of target
def count_x(nums, x):
    count = 0
    for num in nums:
        if num == x:
            count += 1
    return count

print(count_x([1, 2, 5, 4, 5], 5))  # 2

# Check if list is empty
def is_empty(items):
    return len(items) == 0
    # Or simply: return not items

# Remove duplicates (preserving order)
def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Modifying list while iterating
items = [1, 2, 3, 4, 5]
# for item in items:
#     if item % 2 == 0:
#         items.remove(item)  # ❌ Unpredictable results!

# Solution: iterate over copy or use list comprehension
items = [item for item in items if item % 2 != 0]

# 2. Assignment doesn't copy
a = [1, 2, 3]
b = a          # ❌ b points to same list
b = a.copy()   # ✅ b is a new list

# 3. List of lists - shallow copy gotcha
original = [[1, 2], [3, 4]]
copy = original.copy()  # Shallow copy
copy[0][0] = 99
print(original)  # [[99, 2], [3, 4]] - inner list modified!

# Use copy.deepcopy for nested structures
import copy
deep = copy.deepcopy(original)


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use 'in' to check membership: if x in my_list
# 2. Use enumerate() when you need index and value
# 3. Use zip() to iterate multiple lists together
# 4. Use list comprehensions for transformations (next level topic)
# 5. Remember: sort() modifies in place, sorted() returns new list
