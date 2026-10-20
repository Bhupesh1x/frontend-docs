"""
=============================================================================
 STRINGS
=============================================================================
 Strings are sequences of characters. They are immutable in Python,
 meaning you cannot change them after creation.
=============================================================================
"""

# =============================================================================
# STRING BASICS
# =============================================================================

# Creating strings
single_quoted = 'Hello'
double_quoted = "Hello"
multi_line = """This is
a multi-line
string"""

# String length
text = "Hello"
print(len(text))  # 5


# =============================================================================
# STRING INDEXING
# =============================================================================

text = "Python"
#       012345  (positive indices)
#      -6-5-4-3-2-1  (negative indices)

# Positive indexing (left to right, starting at 0)
print(text[0])   # P (first character)
print(text[1])   # y
print(text[5])   # n (last character)

# Negative indexing (right to left, starting at -1)
print(text[-1])  # n (last character)
print(text[-2])  # o
print(text[-6])  # P (first character)

# Useful functions
def get_first_char(s):
    return s[0]

def get_last_char(s):
    return s[-1]
    # Or: s[len(s) - 1]

print(get_first_char("hello"))  # h
print(get_last_char("hello"))   # o


# =============================================================================
# STRING SLICING
# =============================================================================

text = "Hello, World!"
#       0123456789...

# Syntax: string[start:end]  (end is exclusive)
print(text[0:5])    # Hello
print(text[7:12])   # World

# Omitting start or end
print(text[:5])     # Hello (from beginning)
print(text[7:])     # World! (to end)
print(text[:])      # Hello, World! (copy of string)

# With step: string[start:end:step]
print(text[::2])    # Hlo ol! (every 2nd character)
print(text[1::2])   # el,Wrd  (every 2nd, starting from index 1)

# Reverse a string
print(text[::-1])   # !dlroW ,olleH

# Practical slicing functions
def first_n_chars(s: str, n: int) -> str:
    """Get first n characters."""
    return s[:n]

def last_n_chars(s: str, n: int) -> str:
    """Get last n characters."""
    return s[-n:]

def get_substring(s: str, start: int, end: int) -> str:
    """Get substring from start to end."""
    if end > len(s):
        return ""
    return s[start:end]

print(first_n_chars("Python", 3))     # Pyt
print(last_n_chars("Python", 3))      # hon
print(get_substring("LeetCode", 0, 4))  # Leet


# =============================================================================
# ITERATING THROUGH STRINGS
# =============================================================================

# Using for-in loop (preferred)
for char in "Hello":
    print(char)

# Using index
text = "Hello"
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

# With enumerate (best when you need both)
for index, char in enumerate("Hello"):
    print(f"{index}: {char}")


# =============================================================================
# STRING CONCATENATION
# =============================================================================

# Using + operator
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # Hello World

# ⚠️ Can only concatenate strings with strings
name = "Alice"
age = 25
# print(name + age)  # ❌ TypeError
print(name + str(age))  # ✅ Alice25

# Using join() for multiple strings
words = ["Hello", "World", "!"]
sentence = " ".join(words)
print(sentence)  # Hello World !

# Join with different separators
print("-".join(["a", "b", "c"]))  # a-b-c
print("".join(["a", "b", "c"]))   # abc


# =============================================================================
# STRING FORMATTING
# =============================================================================

name = "Alice"
age = 28

# Method 1: f-strings (Python 3.6+, recommended)
message = f"Hi {name}, you are {age} years old"
print(message)  # Hi Alice, you are 28 years old

# Expressions in f-strings
print(f"Next year you'll be {age + 1}")  # Next year you'll be 29

# Method 2: .format() method
message = "Hi {}, you are {} years old".format(name, age)
print(message)

# With positional indices
message = "Hi {1}, you are {0} years old".format(age, name)
print(message)  # Hi Alice, you are 28 years old

# With named placeholders
message = "Hi {n}, you are {a} years old".format(n=name, a=age)
print(message)

# Method 3: % formatting (old style, less common now)
message = "Hi %s, you are %d years old" % (name, age)
print(message)


# =============================================================================
# STRING METHODS
# =============================================================================

text = "  Hello, World!  "

# Case methods
print("hello".upper())      # HELLO
print("HELLO".lower())      # hello
print("hello".capitalize()) # Hello
print("hello world".title()) # Hello World
print("HeLLo".swapcase())   # hEllO

# Whitespace methods
print(text.strip())         # "Hello, World!" (remove both sides)
print(text.lstrip())        # "Hello, World!  " (remove left)
print(text.rstrip())        # "  Hello, World!" (remove right)

# Search methods
print("Hello".find("l"))     # 2 (first occurrence)
print("Hello".find("x"))     # -1 (not found)
print("Hello".index("l"))    # 2 (same as find, but raises error if not found)
print("Hello".count("l"))    # 2 (count occurrences)

# Check methods (return boolean)
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True
print("Hello".isalpha())         # True (only letters)
print("12345".isdigit())         # True (only digits)
print("Hello123".isalnum())      # True (letters or digits)
print("   ".isspace())           # True (only whitespace)

# Replace
print("Hello".replace("l", "L"))      # HeLLo
print("Hello".replace("l", "L", 1))   # HeLlo (replace only first)

# Split
print("a,b,c".split(","))             # ['a', 'b', 'c']
print("Hello World".split())          # ['Hello', 'World'] (splits on whitespace)
print("a-b-c-d".split("-", 2))        # ['a', 'b', 'c-d'] (max 2 splits)


# =============================================================================
# STRINGS ARE IMMUTABLE
# =============================================================================

text = "Hello"
# text[0] = "J"  # ❌ TypeError: 'str' object does not support item assignment

# To "modify" a string, create a new one
text = "J" + text[1:]
print(text)  # Jello

# Practical example: remove character at index
def remove_char_at(s: str, index: int) -> str:
    """Remove character at given index."""
    return s[:index] + s[index + 1:]

print(remove_char_at("Hello", 1))  # Hllo


# =============================================================================
# REVERSE A STRING
# =============================================================================

# Using slicing (most Pythonic)
text = "Hello"
reversed_text = text[::-1]
print(reversed_text)  # olleH

# Using reversed() and join()
reversed_text = "".join(reversed(text))
print(reversed_text)  # olleH

def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("Python"))  # nohtyP


# =============================================================================
# STRING COMPARISON
# =============================================================================

# Strings are compared lexicographically (dictionary order)
print("apple" < "banana")  # True
print("Apple" < "apple")   # True (uppercase < lowercase in ASCII)

# Case-insensitive comparison
s1 = "Hello"
s2 = "hello"
print(s1 == s2)                   # False
print(s1.lower() == s2.lower())   # True


# =============================================================================
# SPECIAL CHARACTERS (ESCAPE SEQUENCES)
# =============================================================================

# \n - newline
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote

print("Line1\nLine2")  # Two lines
print("Tab\tSpace")    # Tab Space
print("Quote: \"Hi\"") # Quote: "Hi"

# Raw strings (ignore escape sequences)
print(r"C:\new\folder")  # C:\new\folder (no newline)


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Get longer word
def get_longer_word(word1: str, word2: str) -> str:
    """Return the longer of two words."""
    return word1 if len(word1) >= len(word2) else word2

print(get_longer_word("yellow", "orange"))  # yellow

# Check palindrome
def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome."""
    s = s.lower().replace(" ", "")  # Normalize
    return s == s[::-1]

print(is_palindrome("radar"))       # True
print(is_palindrome("A man a plan")) # False (spaces matter without full cleanup)

# Count vowels
def count_vowels(s: str) -> int:
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # 3


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Strings are immutable - can't modify in place
# s = "hello"
# s[0] = "H"  # ❌ TypeError

# 2. Using 'str' as variable name shadows built-in
# str = "hello"  # ❌ Now str() function won't work!
# text = "hello"  # ✅ Use descriptive names

# 3. Concatenation in loops is slow
# Instead of:
result = ""
for i in range(100):
    result += str(i)  # ❌ Creates new string each time

# Do:
parts = []
for i in range(100):
    parts.append(str(i))
result = "".join(parts)  # ✅ Much faster

# 4. Index out of range
text = "Hi"
# print(text[5])  # ❌ IndexError


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use f-strings for formatting (cleaner and faster)
# 2. Use join() for concatenating many strings
# 3. Use slicing for substrings and reversing
# 4. Remember: strings are immutable
# 5. Use in operator to check for substrings: "lo" in "Hello"  # True
