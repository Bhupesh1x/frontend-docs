# Python Learning Notes 🐍

A structured collection of Python fundamentals for quick revision and reference.

## 📚 Table of Contents

| # | Topic | File | Description |
|---|-------|------|-------------|
| 1 | [Variables](#1-variables) | [01_variables.py](01_variables.py) | Variables, assignment, basic types |
| 2 | [Functions](#2-functions) | [02_functions.py](02_functions.py) | Defining functions, parameters, return, type hints |
| 3 | [Conditionals](#3-conditionals) | [03_conditionals.py](03_conditionals.py) | If/elif/else, comparisons, truthy/falsy |
| 4 | [Loops](#4-loops) | [04_loops.py](04_loops.py) | While, for, range, nested loops, break/continue |
| 5 | [Strings](#5-strings) | [05_strings.py](05_strings.py) | String operations, indexing, slicing, formatting |
| 6 | [Lists](#6-lists) | [06_lists.py](06_lists.py) | List operations, methods, slicing |
| 7 | [Tuples](#7-tuples) | [07_tuples.py](07_tuples.py) | Immutable sequences |
| 8 | [Sets](#8-sets) | [08_sets.py](08_sets.py) | Unique collections, set operations |
| 9 | [Dictionaries](#9-dictionaries) | [09_dictionaries.py](09_dictionaries.py) | Key-value pairs, dict methods |
| 10 | [Input/Output](#10-inputoutput) | [10_input_output.py](10_input_output.py) | Reading input, parsing, type conversion |
| 11 | [Error Handling](#11-error-handling) | [11_error_handling.py](11_error_handling.py) | Try/except basics |

📋 **Quick Reference:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Condensed cheat sheet for all topics

---

## Topic Summaries

### 1. Variables
Basic variable assignment and types in Python.
```python
message = "Hello"    # String
count = 42           # Integer
price = 19.99        # Float
is_valid = True      # Boolean
```

### 2. Functions
Defining reusable blocks of code with parameters and return values.
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### 3. Conditionals
Making decisions with if/elif/else statements.
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### 4. Loops
Repeating code with while and for loops.
```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

while condition:
    # do something
```

### 5. Strings
Text manipulation with indexing, slicing, and formatting.
```python
text = "Python"
text[0]      # 'P'
text[1:4]    # 'yth'
text[::-1]   # 'nohtyP' (reversed)
f"Language: {text}"
```

### 6. Lists
Ordered, mutable collections.
```python
nums = [1, 2, 3]
nums.append(4)    # [1, 2, 3, 4]
nums.pop()        # [1, 2, 3]
nums[0]           # 1
```

### 7. Tuples
Ordered, immutable collections.
```python
point = (10, 20)
x, y = point      # Unpacking
```

### 8. Sets
Unordered collections of unique elements.
```python
unique = {1, 2, 3}
unique.add(4)
2 in unique       # True
```

### 9. Dictionaries
Key-value pair collections.
```python
person = {"name": "Alice", "age": 25}
person["name"]    # "Alice"
person["city"] = "NYC"
```

### 10. Input/Output
Reading and parsing user input.
```python
name = input("Enter name: ")
nums = input("Enter numbers: ").split(",")
```

### 11. Error Handling
Handling exceptions gracefully.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## 🚀 How to Use

1. **Learning:** Read through files in order (01 → 11)
2. **Revision:** Jump to specific topic files
3. **Quick Lookup:** Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
4. **Practice:** Run the example code in each file

```bash
# Run any file
python 01_variables.py

# Run specific examples (uncomment the code you want to test)
```

## 💡 Tips

- Each file contains runnable examples
- Code is organized with clear section headers
- Common pitfalls are marked with ⚠️
- Best practices are marked with ✅
