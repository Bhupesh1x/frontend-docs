"""
=============================================================================
 DICTIONARIES
=============================================================================
 Dictionaries are mutable collections of key-value pairs.
 They're one of the most important and widely used data structures in Python.
 Similar to objects in JavaScript or HashMaps in other languages.
=============================================================================
"""

# =============================================================================
# CREATING DICTIONARIES
# =============================================================================

# Using curly braces
person = {"name": "Alice", "age": 25, "city": "NYC"}
print(person)

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="LA")
print(person2)

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# Building incrementally
my_dict = {}
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"
print(my_dict)


# =============================================================================
# ACCESSING VALUES
# =============================================================================

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Using brackets (raises KeyError if not found)
print(person["name"])  # Alice
# print(person["job"])  # ❌ KeyError

# Using get() (returns None or default if not found)
print(person.get("name"))           # Alice
print(person.get("job"))            # None
print(person.get("job", "Unknown")) # Unknown (custom default)


# =============================================================================
# ADDING & MODIFYING VALUES
# =============================================================================

person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["city"] = "NYC"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Modify existing value
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'NYC'}

# ⚠️ Keys must be unique - duplicates overwrite
person["name"] = "Alicia"
print(person)  # name is now 'Alicia'

# update() - add/update multiple key-value pairs
person.update({"age": 27, "job": "Engineer"})
print(person)


# =============================================================================
# REMOVING ITEMS
# =============================================================================

person = {"name": "Alice", "age": 25, "city": "NYC"}

# pop() - remove and return value
age = person.pop("age")
print(age)      # 25
print(person)   # {'name': 'Alice', 'city': 'NYC'}

# pop() with default (no error if missing)
job = person.pop("job", "Not found")
print(job)      # Not found

# del - remove by key
del person["city"]
print(person)   # {'name': 'Alice'}

# clear() - remove all items
person.clear()
print(person)   # {}

# popitem() - remove and return last inserted pair (Python 3.7+)
person = {"a": 1, "b": 2, "c": 3}
last = person.popitem()
print(last)     # ('c', 3)
print(person)   # {'a': 1, 'b': 2}


# =============================================================================
# CHECKING KEYS
# =============================================================================

person = {"name": "Alice", "age": 25}

# 'in' checks for keys (not values!)
print("name" in person)     # True
print("Alice" in person)    # False (Alice is a value, not a key)
print("job" not in person)  # True


# =============================================================================
# DICTIONARY VIEWS
# =============================================================================

person = {"name": "Alice", "age": 25, "city": "NYC"}

# keys() - get all keys
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(list(person.keys()))  # ['name', 'age', 'city']

# values() - get all values
print(person.values())  # dict_values(['Alice', 25, 'NYC'])
print(list(person.values()))  # ['Alice', 25, 'NYC']

# items() - get key-value pairs as tuples
print(person.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'NYC')])


# =============================================================================
# ITERATING OVER DICTIONARIES
# =============================================================================

person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate over keys (default)
print("Keys:")
for key in person:
    print(key)  # name, age, city

# Iterate over values
print("\nValues:")
for value in person.values():
    print(value)  # Alice, 25, NYC

# Iterate over key-value pairs (most common)
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")


# =============================================================================
# DICTIONARY VALUES CAN BE ANY TYPE
# =============================================================================

# Values can be lists, dicts, or any other type
complex_dict = {
    "numbers": [1, 2, 3],
    "nested": {"x": 10, "y": 20},
    "mixed": (1, "hello", True)
}

print(complex_dict["numbers"])     # [1, 2, 3]
print(complex_dict["nested"]["x"]) # 10
print(complex_dict["numbers"][0])  # 1


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Convert list to dict (element -> index)
def list_to_dict(items):
    """Map each item to its index."""
    result = {}
    for i, item in enumerate(items):
        result[item] = i
    return result

print(list_to_dict(["a", "b", "c"]))  # {'a': 0, 'b': 1, 'c': 2}

# Get dict keys as list
def get_keys(d):
    return list(d.keys())

# Get dict values as list
def get_values(d):
    return list(d.values())

# Count character frequency
def count_chars(text):
    """Count frequency of each character."""
    counts = {}
    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

print(count_chars("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Alternative using get()
def count_chars_v2(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Remove keys from dict
def remove_keys(d, keys_to_remove):
    """Remove specified keys from dict."""
    for key in keys_to_remove:
        d.pop(key, None)  # Use None default to avoid error
    return d

print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))  # {'b': 2}


# =============================================================================
# USEFUL METHODS
# =============================================================================

# setdefault() - get value, set default if missing
person = {"name": "Alice"}
age = person.setdefault("age", 25)  # Sets and returns 25
print(person)  # {'name': 'Alice', 'age': 25}

name = person.setdefault("name", "Bob")  # Returns 'Alice', doesn't change
print(name)    # Alice

# fromkeys() - create dict with keys from iterable
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

# copy() - shallow copy
original = {"a": 1, "b": 2}
copied = original.copy()
copied["c"] = 3
print(original)  # {'a': 1, 'b': 2} (unchanged)


# =============================================================================
# MERGING DICTIONARIES
# =============================================================================

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update() (modifies dict1)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(dict1_copy)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using | operator (Python 3.9+)
# merged = dict1 | dict2


# =============================================================================
# NESTED DICTIONARIES
# =============================================================================

users = {
    "alice": {"age": 25, "city": "NYC"},
    "bob": {"age": 30, "city": "LA"}
}

# Access nested values
print(users["alice"]["age"])  # 25

# Modify nested values
users["alice"]["age"] = 26

# Add new nested entry
users["charlie"] = {"age": 35, "city": "Chicago"}

# Iterate nested
for username, info in users.items():
    print(f"{username}: {info['city']}")


# =============================================================================
# DICT COMPREHENSIONS (PREVIEW)
# =============================================================================

# Create dict from iterable
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invert dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}


# =============================================================================
# ORDERED BEHAVIOR (Python 3.7+)
# =============================================================================

# Since Python 3.7, dicts maintain insertion order
d = {}
d["first"] = 1
d["second"] = 2
d["third"] = 3

for key in d:
    print(key)  # Guaranteed: first, second, third


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. KeyError when accessing missing key
d = {"a": 1}
# print(d["b"])  # ❌ KeyError
print(d.get("b"))  # ✅ Returns None

# 2. Keys must be hashable (immutable)
valid = {(1, 2): "tuple key"}    # ✅ Tuple OK
# invalid = {[1, 2]: "list key"} # ❌ Lists not hashable

# 3. 'in' checks keys, not values
d = {"name": "Alice"}
print("name" in d)   # True (key)
print("Alice" in d)  # False (value, not key)
print("Alice" in d.values())  # True (check values)

# 4. Modifying dict while iterating
d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     del d[key]  # ❌ RuntimeError: dictionary changed size during iteration

# Solution: iterate over copy of keys
for key in list(d.keys()):
    if d[key] == 2:
        del d[key]


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use .get() for safe access with default values
# 2. Use .items() when you need both key and value
# 3. Use 'in' to check key existence before access
# 4. Use dict comprehensions for transformations
# 5. Remember: keys must be immutable (strings, numbers, tuples)
# 6. Python 3.7+ maintains insertion order
