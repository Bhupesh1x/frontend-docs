"""
=============================================================================
 VARIABLES & BASIC TYPES
=============================================================================
 Variables are containers for storing data values.
 Python is dynamically typed - no need to declare variable types explicitly.
=============================================================================
"""

# =============================================================================
# BASIC VARIABLE ASSIGNMENT
# =============================================================================

# Strings - text enclosed in quotes (single or double)
message = "Hello world"
greeting = 'Hi there'

# Integers - whole numbers
count = 42
age = 25
negative_num = -10

# Floats - decimal numbers
price = 19.99
temperature = 36.6
pi = 3.14159

# Booleans - True or False (note the capital T and F)
is_valid = True
is_empty = False

# None - represents absence of value (like null in other languages)
result = None


# =============================================================================
# MULTIPLE ASSIGNMENT
# =============================================================================

# Assign multiple variables in one line
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")  # x=1, y=2, z=3

# Assign same value to multiple variables
a = b = c = 0
print(f"a={a}, b={b}, c={c}")  # a=0, b=0, c=0

# Swap variables (Python makes this easy!)
first, second = 10, 20
first, second = second, first
print(f"first={first}, second={second}")  # first=20, second=10


# =============================================================================
# CHECKING TYPES
# =============================================================================

# Use type() to check the type of a variable
print(type(message))      # <class 'str'>
print(type(count))        # <class 'int'>
print(type(price))        # <class 'float'>
print(type(is_valid))     # <class 'bool'>
print(type(result))       # <class 'NoneType'>


# =============================================================================
# TYPE CONVERSION (CASTING)
# =============================================================================

# Convert between types
num_str = "42"
num_int = int(num_str)      # String to Integer: 42
num_float = float(num_str)  # String to Float: 42.0

price_int = int(19.99)      # Float to Integer: 19 (truncates, doesn't round)
price_str = str(19.99)      # Float to String: "19.99"

print(f"int('42') = {num_int}")
print(f"float('42') = {num_float}")
print(f"int(19.99) = {price_int}")
print(f"str(19.99) = {price_str}")


# =============================================================================
# ARITHMETIC OPERATORS
# =============================================================================

a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")           # 13
print(f"Subtraction: {a} - {b} = {a - b}")        # 7
print(f"Multiplication: {a} * {b} = {a * b}")    # 30
print(f"Division: {a} / {b} = {a / b}")           # 3.333... (always float)
print(f"Floor Division: {a} // {b} = {a // b}")   # 3 (rounds down)
print(f"Modulus: {a} % {b} = {a % b}")            # 1 (remainder)
print(f"Exponent: {a} ** {b} = {a ** b}")         # 1000 (10^3)


# =============================================================================
# ASSIGNMENT OPERATORS (SHORTCUTS)
# =============================================================================

n = 10

n += 5   # Same as: n = n + 5  → 15
n -= 3   # Same as: n = n - 3  → 12
n *= 2   # Same as: n = n * 2  → 24
n /= 4   # Same as: n = n / 4  → 6.0
n //= 2  # Same as: n = n // 2 → 3.0
n %= 2   # Same as: n = n % 2  → 1.0

# ⚠️ PITFALL: Python does NOT support ++ or --
# n++  # ❌ SyntaxError
# n--  # ❌ SyntaxError
# Use n += 1 or n -= 1 instead


# =============================================================================
# NAMING CONVENTIONS
# =============================================================================

# ✅ Good variable names (snake_case is Python convention)
user_name = "Alice"
total_count = 100
is_logged_in = True
MAX_SIZE = 1000  # UPPERCASE for constants

# ❌ Avoid these
# 2fast = "value"      # Can't start with number
# my-var = "value"     # Can't use hyphens
# class = "value"      # Can't use reserved keywords
# str = "hello"        # Avoid shadowing built-in names


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Variables are case-sensitive
Name = "Alice"
name = "Bob"
print(Name, name)  # Alice Bob (different variables)

# 2. Check if variable exists with 'in' and locals()/globals()
my_var = 10
print('my_var' in locals())  # True

# 3. Delete a variable with 'del'
temp = 100
del temp
# print(temp)  # ❌ NameError: name 'temp' is not defined


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Integer division in Python 3 returns float
print(10 / 5)   # 2.0 (not 2)
print(10 // 5)  # 2 (use // for integer result)

# 2. Floating point precision issues
print(0.1 + 0.2)  # 0.30000000000000004 (not exactly 0.3)
# Use round() for display or decimal module for precision

# 3. None is not the same as 0, False, or ""
print(None == 0)      # False
print(None == False)  # False
print(None == "")     # False
