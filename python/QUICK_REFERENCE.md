# Python Quick Reference Cheat Sheet 📋

A condensed reference for quick lookups. For detailed explanations, see the individual topic files.

---

## 1. Variables & Types

```python
# Basic Types
name = "Alice"      # str
age = 25            # int
price = 19.99       # float
is_valid = True     # bool
nothing = None      # NoneType

# Multiple Assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Type Conversion
int("42")           # 42
float("3.14")       # 3.14
str(100)            # "100"
bool(1)             # True

# Type Check
type(variable)      # <class 'int'>

# Arithmetic
+  -  *  /          # Basic
//                  # Floor division (rounds down)
%                   # Modulus (remainder)
**                  # Exponent

# Assignment Shortcuts
n += 1              # n = n + 1
n -= 1              # n = n - 1
n *= 2              # n = n * 2
```

---

## 2. Functions

```python
# Basic Function
def greet():
    print("Hello!")

# With Parameters
def greet(name):
    print(f"Hello, {name}!")

# With Return
def add(a, b):
    return a + b

# Type Hints (optional, not enforced)
def add(a: int, b: int) -> int:
    return a + b

# Default Parameters
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# Multiple Return Values
def min_max(nums):
    return min(nums), max(nums)

a, b = min_max([1, 2, 3])

# *args and **kwargs
def func(*args):           # Tuple of positional args
def func(**kwargs):        # Dict of keyword args
```

---

## 3. Conditionals

```python
# Comparison Operators
==   !=   <   >   <=   >=

# Logical Operators
and   or   not

# If Statement
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# Ternary Operator
result = "yes" if condition else "no"

# Truthy/Falsy
# Falsy: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy

# Identity
x is None           # Preferred for None checks
x is not None
```

---

## 4. Loops

```python
# While Loop
i = 0
while i < 5:
    print(i)
    i += 1

# For Loop with Range
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(2, 5):       # 2, 3, 4
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1

# For Loop with Iterable
for item in items:
    print(item)

# With Index
for i, item in enumerate(items):
    print(i, item)

# Loop Control
break               # Exit loop
continue            # Skip to next iteration
pass                # Do nothing (placeholder)

# Loop with Else
for i in range(5):
    pass
else:
    print("Completed!")  # Runs if no break
```

---

## 5. Strings

```python
# Indexing
s = "Python"
s[0]                # 'P' (first)
s[-1]               # 'n' (last)

# Slicing [start:end:step]
s[0:3]              # 'Pyt'
s[:3]               # 'Pyt' (from start)
s[3:]               # 'hon' (to end)
s[::2]              # 'Pto' (every 2nd)
s[::-1]             # 'nohtyP' (reverse)

# Common Methods
len(s)              # Length
s.upper()           # UPPERCASE
s.lower()           # lowercase
s.strip()           # Remove whitespace
s.split(",")        # Split to list
",".join(list)      # Join list to string
s.replace("a", "b") # Replace
s.find("x")         # Find index (-1 if not found)
s.count("a")        # Count occurrences
s.startswith("Py")  # True/False
s.endswith("on")    # True/False

# Formatting
f"Hello, {name}!"   # f-string (preferred)
"Hi {}".format(x)   # .format()

# ⚠️ Strings are IMMUTABLE
```

---

## 6. Lists

```python
# Create
lst = [1, 2, 3]
lst = list(range(5))
lst = [0] * 5           # [0, 0, 0, 0, 0]

# Access
lst[0]                  # First
lst[-1]                 # Last
lst[1:3]                # Slice

# Modify
lst[0] = 99             # Change element
lst.append(4)           # Add to end
lst.insert(0, 99)       # Insert at index
lst.extend([5, 6])      # Add multiple
lst.pop()               # Remove & return last
lst.pop(0)              # Remove & return at index
lst.remove(value)       # Remove first occurrence
del lst[0]              # Delete at index
lst.clear()             # Remove all

# Search
3 in lst                # True/False
lst.index(3)            # Find index (error if not found)
lst.count(3)            # Count occurrences

# Sort & Reverse
lst.sort()              # Sort in place
lst.sort(reverse=True)  # Descending
sorted(lst)             # Return new sorted list
lst.reverse()           # Reverse in place
lst[::-1]               # Return reversed copy

# Built-in Functions
len(lst)                # Length
sum(lst)                # Sum
min(lst)                # Minimum
max(lst)                # Maximum

# Copy
new = lst.copy()        # Shallow copy
new = lst[:]            # Shallow copy

# Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]
```

---

## 7. Tuples

```python
# Create
t = (1, 2, 3)
t = 1, 2, 3             # Parentheses optional
single = (1,)           # ⚠️ Need comma for single!

# Access (same as lists)
t[0]                    # First
t[-1]                   # Last
t[1:3]                  # Slice

# Methods
t.count(1)              # Count occurrences
t.index(1)              # Find index

# Unpacking
x, y = (10, 20)
a, b = b, a             # Swap

# ⚠️ Tuples are IMMUTABLE
# ✅ Can be dict keys (unlike lists)
```

---

## 8. Sets

```python
# Create
s = {1, 2, 3}
s = set()               # ⚠️ Empty set (NOT {})
s = set([1, 2, 2, 3])   # {1, 2, 3} (no duplicates)

# Modify
s.add(4)                # Add element
s.update([5, 6])        # Add multiple
s.remove(1)             # Remove (error if not found)
s.discard(1)            # Remove (no error)
s.pop()                 # Remove arbitrary element
s.clear()               # Remove all

# Membership
3 in s                  # True/False (O(1) - fast!)

# Set Operations
A | B                   # Union
A & B                   # Intersection
A - B                   # Difference (in A, not in B)
A ^ B                   # Symmetric difference

# Comparisons
A <= B                  # A is subset of B
A < B                   # A is proper subset of B
A >= B                  # A is superset of B

# Remove duplicates from list
unique = list(set(my_list))
```

---

## 9. Dictionaries

```python
# Create
d = {"name": "Alice", "age": 25}
d = dict(name="Alice", age=25)
d = {}                  # Empty dict

# Access
d["name"]               # "Alice" (KeyError if missing)
d.get("name")           # "Alice" (None if missing)
d.get("job", "N/A")     # "N/A" (custom default)

# Modify
d["name"] = "Bob"       # Update
d["city"] = "NYC"       # Add new
d.update({"a": 1})      # Update multiple
del d["name"]           # Delete
d.pop("name")           # Delete and return
d.pop("name", None)     # Safe delete
d.clear()               # Remove all

# Check
"name" in d             # Check key exists
"Alice" in d.values()   # Check value exists

# Iterate
for key in d:           # Keys
for value in d.values(): # Values
for k, v in d.items():  # Key-value pairs

# Views
d.keys()                # All keys
d.values()              # All values
d.items()               # Key-value tuples
```

---

## 10. Input/Output

```python
# Output
print("Hello")
print("a", "b", "c")        # a b c
print("a", "b", sep="-")    # a-b
print("Hi", end=" ")        # No newline

# Input (always returns string!)
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))

# Parse comma-separated
nums = input().split(",")   # ['1', '2', '3']
nums = [int(x) for x in input().split(",")]

# Multiple values
x, y = input().split()
x, y = map(int, input().split())
```

---

## 11. Error Handling

```python
# Basic Try/Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Multiple Exceptions
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch All
except Exception as e:
    print(f"Error: {e}")

# Else (runs if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    pass
else:
    print("Success!")

# Finally (always runs)
try:
    pass
except:
    pass
finally:
    print("Cleanup")

# Raise Exception
raise ValueError("Invalid input")

# Common Exceptions
# ValueError, TypeError, KeyError, IndexError
# ZeroDivisionError, FileNotFoundError, AttributeError
```

---

## Common Patterns

```python
# Swap variables
a, b = b, a

# Check empty
if not items:           # Empty list/string/dict
if items:               # Not empty

# Safe dict access
value = d.get("key", default)

# Remove duplicates
unique = list(set(items))

# Count occurrences
from collections import Counter
counts = Counter(items)

# Iterate with index
for i, item in enumerate(items):

# Iterate two lists
for a, b in zip(list1, list2):

# Filter list
filtered = [x for x in items if condition]

# Transform list
transformed = [f(x) for x in items]
```

---

## Quick Tips

| Want to... | Use |
|------------|-----|
| Check if item in collection | `x in collection` |
| Get length | `len(collection)` |
| Reverse | `collection[::-1]` |
| Sort | `sorted(collection)` |
| Get unique items | `set(collection)` |
| Count items | `collection.count(x)` |
| Find index | `collection.index(x)` |
| Check type | `type(x)` or `isinstance(x, Type)` |
| Convert types | `int()`, `str()`, `list()`, etc. |

---

## ⚠️ Common Pitfalls

1. **Strings/Tuples are immutable** - can't modify in place
2. **`input()` always returns string** - convert with `int()` or `float()`
3. **Empty set is `set()`, not `{}`** - `{}` creates empty dict
4. **Single-element tuple needs comma** - `(1,)` not `(1)`
5. **Python has no `++` or `--`** - use `+= 1` or `-= 1`
6. **`=` assigns, `==` compares**
7. **Use `is` for `None` checks** - `if x is None`
8. **Don't use `str`, `list`, `dict` as variable names**
