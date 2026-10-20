"""
=============================================================================
 CONDITIONALS
=============================================================================
 Conditionals allow your program to make decisions and execute different
 code blocks based on conditions.
=============================================================================
"""

# =============================================================================
# COMPARISON OPERATORS
# =============================================================================

a, b = 10, 5

# Equality
print(a == b)   # False - equal to
print(a != b)   # True  - not equal to

# Relational
print(a < b)    # False - less than
print(a > b)    # True  - greater than
print(a <= b)   # False - less than or equal
print(a >= b)   # True  - greater than or equal

# Comparison functions
def check_equal(x, y):
    return x == y

def check_less_than(x, y):
    return x < y

def check_greater_than(x, y):
    return x > y


# =============================================================================
# IF STATEMENT
# =============================================================================

def check_balance(balance: int) -> None:
    """Warn if balance is low."""
    if balance <= 100:
        print("⚠️ Warning: Low balance!")

check_balance(99)   # ⚠️ Warning: Low balance!
check_balance(100)  # ⚠️ Warning: Low balance!
check_balance(101)  # (no output)


# =============================================================================
# IF-ELSE STATEMENT
# =============================================================================

def get_min(a: int, b: int) -> int:
    """Return the smaller of two numbers."""
    if a <= b:
        return a
    else:
        return b

print(get_min(10, 11))  # 10
print(get_min(5, -7))   # -7
print(get_min(20, 20))  # 20

# Pay bill example
def pay_bill(balance: int, bill: int) -> int:
    """Pay bill if sufficient balance, return remaining balance."""
    if balance >= bill:
        return balance - bill
    else:
        return balance  # Can't pay, return original balance

print(pay_bill(100, 50))   # 50
print(pay_bill(100, 100))  # 0
print(pay_bill(100, 150))  # 100 (can't pay)


# =============================================================================
# IF-ELIF-ELSE STATEMENT
# =============================================================================

def check_range(num: int) -> str:
    """Categorize a number by its range."""
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    elif num > 0 and num < 10:
        return "Positive single digit"
    elif num >= 10:
        return "Positive multi digit"

print(check_range(-10))   # Negative
print(check_range(0))     # Zero
print(check_range(9))     # Positive single digit
print(check_range(1000))  # Positive multi digit


# =============================================================================
# LOGICAL OPERATORS
# =============================================================================

# and - both conditions must be True
# or  - at least one condition must be True
# not - inverts the boolean value

x, y = 5, 10

# and
if x > 0 and y > 0:
    print("Both positive")  # Prints

# or
if x > 100 or y > 5:
    print("At least one condition met")  # Prints

# not
if not x > 100:
    print("x is NOT greater than 100")  # Prints

# Combined
def is_valid_age(age: int) -> bool:
    """Check if age is valid (between 0 and 120)."""
    return age >= 0 and age <= 120

# Better way using chained comparison
def is_valid_age_better(age: int) -> bool:
    """Check if age is valid using chained comparison."""
    return 0 <= age <= 120  # Python allows this!

print(is_valid_age(25))   # True
print(is_valid_age(-5))   # False
print(is_valid_age(150))  # False


# =============================================================================
# TRUTHY AND FALSY VALUES
# =============================================================================

# Like JavaScript, Python evaluates non-boolean values in boolean context

# ❌ FALSY values (evaluate to False):
# - False (boolean)
# - None
# - 0 (integer zero)
# - 0.0 (float zero)
# - "" (empty string)
# - [] (empty list)
# - () (empty tuple)
# - {} (empty dict)
# - set() (empty set)

# ✅ TRUTHY values (evaluate to True):
# - True (boolean)
# - Any non-zero number (positive or negative)
# - Any non-empty string (even "0" or "False")
# - Any non-empty collection

# Examples
if 1:
    print("1 is truthy")  # Prints

if "hello":
    print("Non-empty string is truthy")  # Prints

if [1, 2, 3]:
    print("Non-empty list is truthy")  # Prints

# Checking empty vs non-empty
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")  # Prints

# Common pattern: checking for None or empty
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name not provided")  # Prints


# =============================================================================
# IF STATEMENT SCOPE
# =============================================================================

# Unlike some languages, if statements DON'T create a new scope in Python
# Variables created inside if are accessible outside

message = "Hello"

if message:
    message = "Changed inside if"
    new_var = "Created inside if"

print(message)  # Changed inside if
print(new_var)  # Created inside if (accessible!)


# =============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# =============================================================================

# Syntax: value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Same as:
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Can be used inline
def get_absolute(num):
    """Return absolute value using ternary."""
    return num if num >= 0 else -num

print(get_absolute(-5))  # 5
print(get_absolute(5))   # 5


# =============================================================================
# NESTED CONDITIONALS
# =============================================================================

def categorize_person(age: int) -> str:
    """Categorize person by age group."""
    if age < 0:
        return "Invalid age"
    else:
        if age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        elif age < 60:
            return "Adult"
        else:
            return "Senior"

# Better: flatten with elif
def categorize_person_better(age: int) -> str:
    """Same logic but flattened."""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


# =============================================================================
# IDENTITY OPERATORS (is, is not)
# =============================================================================

# 'is' checks if two variables point to the SAME object
# '==' checks if two variables have the SAME value

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  - same value
print(a is b)   # False - different objects
print(a is c)   # True  - same object

# Use 'is' for None checks (preferred)
x = None
if x is None:
    print("x is None")  # ✅ Preferred

if x == None:
    print("x equals None")  # Works but not recommended


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Using = instead of ==
x = 5
# if x = 5:  # ❌ SyntaxError - assignment, not comparison
if x == 5:   # ✅ Correct
    print("x is 5")

# 2. Comparing floats for equality
a = 0.1 + 0.2
# if a == 0.3:  # ❌ May fail due to floating point precision
if abs(a - 0.3) < 0.0001:  # ✅ Check if "close enough"
    print("Approximately equal")

# 3. Empty string is falsy, but "False" string is truthy
if "False":  # This is truthy!
    print("The string 'False' is truthy!")  # Prints

# 4. Forgetting 'and' between conditions
x, y = 5, 10
# if 0 < x < 10:  # ✅ This works in Python!
# if x > 0 and x < 10:  # ✅ Also works


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use 'in' for multiple value checks
color = "red"
# Instead of:
if color == "red" or color == "green" or color == "blue":
    print("Primary color")
# Do:
if color in ("red", "green", "blue"):
    print("Primary color")  # Cleaner!

# 2. Use truthiness for None/empty checks
items = []
# Instead of: if len(items) == 0:
if not items:  # Cleaner!
    print("No items")

# 3. Guard clauses for cleaner code
def process_data(data):
    # Early return for invalid cases
    if data is None:
        return "No data"
    if len(data) == 0:
        return "Empty data"
    
    # Main logic here (less nesting)
    return f"Processing {len(data)} items"
