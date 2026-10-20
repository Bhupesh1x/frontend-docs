"""
=============================================================================
 SETS
=============================================================================
 Sets are unordered collections of unique elements.
 They're useful for membership testing, removing duplicates, and set operations.
=============================================================================
"""

# =============================================================================
# CREATING SETS
# =============================================================================

# Using curly braces
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}

# Duplicates are automatically removed
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

# ⚠️ Empty set - use set(), NOT {}
empty_set = set()    # ✅ Empty set
empty_dict = {}      # ❌ This is an empty dict!

print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>

# From other iterables
from_list = set([1, 2, 3, 2, 1])    # {1, 2, 3}
from_string = set("hello")           # {'h', 'e', 'l', 'o'}
from_tuple = set((1, 2, 3))          # {1, 2, 3}


# =============================================================================
# SET CHARACTERISTICS
# =============================================================================

# 1. Unordered - no guaranteed order
my_set = {3, 1, 2}
print(my_set)  # Could be {1, 2, 3} or any order

# 2. No duplicates
my_set = {1, 1, 2, 2, 3}
print(my_set)  # {1, 2, 3}

# 3. Only hashable (immutable) elements allowed
valid_set = {1, 2, "hello", (1, 2)}  # ✅ Numbers, strings, tuples OK
# invalid_set = {[1, 2]}  # ❌ TypeError: lists are not hashable

# 4. No indexing (because unordered)
# print(my_set[0])  # ❌ TypeError


# =============================================================================
# ADDING ELEMENTS
# =============================================================================

my_set = {1, 2, 3}

# add() - add single element
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Adding duplicate does nothing
my_set.add(1)
print(my_set)  # {1, 2, 3, 4}

# update() - add multiple elements
my_set.update([5, 6, 7])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

my_set.update({8, 9}, [10])  # Can mix iterables
print(my_set)


# =============================================================================
# REMOVING ELEMENTS
# =============================================================================

my_set = {1, 2, 3, 4, 5}

# remove() - raises error if not found
my_set.remove(1)
print(my_set)  # {2, 3, 4, 5}
# my_set.remove(99)  # ❌ KeyError

# discard() - no error if not found (safer)
my_set.discard(2)
print(my_set)  # {3, 4, 5}
my_set.discard(99)  # ✅ No error

# pop() - remove and return arbitrary element
element = my_set.pop()
print(f"Removed: {element}")

# clear() - remove all elements
my_set.clear()
print(my_set)  # set()


# =============================================================================
# MEMBERSHIP TESTING
# =============================================================================

fruits = {"apple", "banana", "cherry"}

# 'in' operator - very fast for sets (O(1))
print("apple" in fruits)      # True
print("mango" in fruits)      # False
print("mango" not in fruits)  # True

# Comparison with list (O(n)) vs set (O(1))
# For large collections, sets are MUCH faster for membership tests


# =============================================================================
# ITERATING OVER SETS
# =============================================================================

colors = {"red", "green", "blue"}

for color in colors:
    print(color)
# Order is not guaranteed!


# =============================================================================
# SET OPERATIONS (MATHEMATICAL)
# =============================================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (elements in A OR B)
print(A | B)           # {1, 2, 3, 4, 5, 6}
print(A.union(B))      # {1, 2, 3, 4, 5, 6}

# Intersection (elements in A AND B)
print(A & B)              # {3, 4}
print(A.intersection(B))  # {3, 4}

# Difference (elements in A but NOT in B)
print(A - B)             # {1, 2}
print(A.difference(B))   # {1, 2}

# Symmetric Difference (elements in A OR B, but NOT both)
print(A ^ B)                      # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}

# Visual representation:
# A = {1, 2, 3, 4}    B = {3, 4, 5, 6}
#
# Union:        {1, 2, 3, 4, 5, 6}    - everything
# Intersection: {3, 4}                - overlap only
# A - B:        {1, 2}                - A without overlap
# B - A:        {5, 6}                - B without overlap
# Symmetric:    {1, 2, 5, 6}          - everything except overlap


# =============================================================================
# SET COMPARISONS
# =============================================================================

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# Subset (A ⊆ B)
print(A <= B)          # True (A is subset of B)
print(A.issubset(B))   # True

# Proper subset (A ⊂ B) - subset but not equal
print(A < B)           # True
print(A < C)           # False (they're equal)

# Superset (B ⊇ A)
print(B >= A)           # True (B is superset of A)
print(B.issuperset(A))  # True

# Disjoint (no common elements)
X = {1, 2}
Y = {3, 4}
print(X.isdisjoint(Y))  # True


# =============================================================================
# MODIFYING SETS IN PLACE
# =============================================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Update with union
A_copy = A.copy()
A_copy |= B
print(A_copy)  # {1, 2, 3, 4, 5, 6}

# Update with intersection
A_copy = A.copy()
A_copy &= B
print(A_copy)  # {3, 4}

# Update with difference
A_copy = A.copy()
A_copy -= B
print(A_copy)  # {1, 2}

# Or use methods:
# A.update(B)                 - union
# A.intersection_update(B)    - intersection
# A.difference_update(B)      - difference
# A.symmetric_difference_update(B)


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Remove duplicates from list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(my_list))
print(unique)  # [1, 2, 3, 4]

# Check for duplicates
def has_duplicates(items):
    """Return True if items has duplicates."""
    return len(items) != len(set(items))

print(has_duplicates([1, 2, 3, 1]))  # True
print(has_duplicates([1, 2, 3, 4]))  # False

# Find duplicates
def find_duplicates(items):
    """Return set of duplicate items."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return duplicates

print(find_duplicates([1, 2, 2, 3, 3, 3]))  # {2, 3}

# Check if word contains duplicate characters
def has_duplicate_chars(word):
    return len(word) != len(set(word))

print(has_duplicate_chars("hello"))  # True (has 'l' twice)
print(has_duplicate_chars("world"))  # False

# Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(common)  # {3, 4}


# =============================================================================
# FROZEN SETS (IMMUTABLE SETS)
# =============================================================================

# frozenset is an immutable version of set
frozen = frozenset([1, 2, 3])
print(frozen)  # frozenset({1, 2, 3})

# Cannot modify
# frozen.add(4)  # ❌ AttributeError

# Can be used as dict key or in another set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}


# =============================================================================
# SET COMPREHENSIONS (PREVIEW)
# =============================================================================

# Similar to list comprehensions
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Empty set syntax
empty_set = set()  # ✅ Correct
# empty_set = {}   # ❌ This is a dict!

# 2. Sets are unordered - can't rely on order
my_set = {3, 1, 2}
# Don't expect specific order when iterating

# 3. Can't have mutable elements
# {[1, 2]}  # ❌ Lists are not hashable
# {{1, 2}}  # ❌ Sets are not hashable
{(1, 2)}    # ✅ Tuples are hashable

# 4. Sets don't support indexing
my_set = {1, 2, 3}
# my_set[0]  # ❌ TypeError


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use sets when you need:
#    - Unique elements only
#    - Fast membership testing
#    - Set operations (union, intersection, etc.)

# 2. Convert list to set to remove duplicates
#    unique = list(set(my_list))

# 3. Use discard() instead of remove() to avoid KeyError

# 4. Sets are much faster than lists for 'in' checks:
#    - List: O(n)
#    - Set: O(1)

# 5. Use frozenset when you need immutable set (for dict keys)
