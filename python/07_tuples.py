"""
=============================================================================
 TUPLES
=============================================================================
 Tuples are ordered, immutable sequences. Once created, they cannot be
 modified. They're useful for storing related data that shouldn't change.
=============================================================================
"""

# =============================================================================
# CREATING TUPLES
# =============================================================================

# Using parentheses
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)

# Without parentheses (tuple packing)
my_tuple = 1, 2, 3
print(my_tuple)  # (1, 2, 3)

# Empty tuple
empty = ()
empty2 = tuple()

# Single element tuple - ⚠️ needs trailing comma!
single = (42,)   # ✅ This is a tuple
not_tuple = (42) # ❌ This is just the number 42

print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# From other iterables
from_list = tuple([1, 2, 3])      # (1, 2, 3)
from_string = tuple("hello")       # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))       # (0, 1, 2, 3, 4)


# =============================================================================
# ACCESSING ELEMENTS
# =============================================================================

coordinates = (10, 20, 30)
#               0   1   2   (positive index)
#              -3  -2  -1   (negative index)

# Indexing (same as lists)
print(coordinates[0])   # 10
print(coordinates[-1])  # 30

# Slicing (same as lists)
print(coordinates[0:2])  # (10, 20)
print(coordinates[::-1]) # (30, 20, 10) - reversed

# Length
print(len(coordinates))  # 3


# =============================================================================
# TUPLES ARE IMMUTABLE
# =============================================================================

point = (10, 20)

# ❌ Cannot modify elements
# point[0] = 15  # TypeError: 'tuple' object does not support item assignment

# ❌ Cannot add or remove elements
# point.append(30)  # AttributeError: no attribute 'append'
# point.pop()       # AttributeError: no attribute 'pop'

# To "modify", create a new tuple
point = (15, 20)  # ✅ Creates new tuple

# Or convert to list, modify, convert back
temp_list = list(point)
temp_list[0] = 15
point = tuple(temp_list)


# =============================================================================
# TUPLE UNPACKING (DESTRUCTURING)
# =============================================================================

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # 10 20 30

# Swapping variables (uses tuple unpacking)
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Unpacking in function returns
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns tuple

minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(minimum, maximum)  # 1 5

# Unpacking with * (extended unpacking)
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] - Note: rest is a list!

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)  # 1 [2, 3, 4] 5

# Ignoring values with _
x, _, z = (10, 20, 30)  # Ignore middle value
print(x, z)  # 10 30


# =============================================================================
# TUPLE OPERATIONS
# =============================================================================

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3
print(repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)      # True
print(9 not in t1)  # True


# =============================================================================
# TUPLE METHODS
# =============================================================================

# Tuples have only 2 methods (because they're immutable)
numbers = (1, 2, 3, 2, 4, 2)

# count() - count occurrences
print(numbers.count(2))  # 3

# index() - find first occurrence
print(numbers.index(2))  # 1
# print(numbers.index(9))  # ValueError if not found


# =============================================================================
# ITERATING OVER TUPLES
# =============================================================================

colors = ("red", "green", "blue")

# Simple iteration
for color in colors:
    print(color)

# With index using enumerate
for index, color in enumerate(colors):
    print(f"{index}: {color}")


# =============================================================================
# TUPLES VS LISTS
# =============================================================================

# ┌────────────┬──────────────────────┬─────────────────────┐
# │ Feature    │ Tuple                │ List                │
# ├────────────┼──────────────────────┼─────────────────────┤
# │ Syntax     │ (1, 2, 3)            │ [1, 2, 3]           │
# │ Mutability │ Immutable            │ Mutable             │
# │ Methods    │ count, index         │ Many (append, etc.) │
# │ Hashable   │ Yes (if contents are)│ No                  │
# │ Use Case   │ Fixed data           │ Dynamic data        │
# │ Memory     │ Slightly smaller     │ Slightly larger     │
# │ Speed      │ Slightly faster      │ Slightly slower     │
# └────────────┴──────────────────────┴─────────────────────┘


# =============================================================================
# WHEN TO USE TUPLES
# =============================================================================

# 1. Return multiple values from functions
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns tuple

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")

# 2. Store related data that shouldn't change
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)

# 3. Dictionary keys (lists can't be dict keys)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(locations[(40.7128, -74.0060)])  # New York

# 4. Data that represents a record/struct
def create_person(name: str, age: int):
    return (name, age)

person = create_person("Alice", 25)
print(person)  # ('Alice', 25)


# =============================================================================
# NAMED TUPLES (ADVANCED)
# =============================================================================

# For more readable tuple access, use namedtuple
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
p = Point(10, 20)
print(p.x)  # 10 (access by name)
print(p[0]) # 10 (access by index still works)

alice = Person("Alice", 25, "NYC")
print(alice.name)  # Alice
print(alice.age)   # 25


# =============================================================================
# NESTED TUPLES
# =============================================================================

# Tuple of tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[0])     # (1, 2, 3)
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Create coordinate pair
def create_pair(x, y):
    return (x, y)

print(create_pair(10, 20))  # (10, 20)

# Calculate distance between points
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

p1 = (0, 0)
p2 = (3, 4)
print(distance(p1, p2))  # 5.0

# Store student records
students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 92)
)

for name, score in students:
    print(f"{name}: {score}")


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Single element tuple needs comma
single = (1,)   # ✅ Tuple
not_tuple = (1) # ❌ Just int 1

# 2. Mutable objects inside tuple CAN be modified
t = ([1, 2], [3, 4])
t[0].append(99)      # ✅ This works!
print(t)             # ([1, 2, 99], [3, 4])
# t[0] = [5, 6]      # ❌ Can't reassign, but can modify contents

# 3. Unpacking must match count
a, b = (1, 2, 3)     # ❌ ValueError: too many values
a, b, c = (1, 2)     # ❌ ValueError: not enough values
a, b, c = (1, 2, 3)  # ✅ Correct


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use tuples for fixed collections (coordinates, RGB values, etc.)
# 2. Use tuples when you need hashable sequences (dict keys, set elements)
# 3. Use tuple unpacking to make code cleaner
# 4. Use namedtuple for more readable tuple access
# 5. Remember: tuples are faster and use less memory than lists
