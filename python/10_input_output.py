"""
=============================================================================
 INPUT & OUTPUT
=============================================================================
 Reading user input and displaying output is fundamental to interactive programs.
 This covers input(), print(), type conversion, and parsing.
=============================================================================
"""

# =============================================================================
# BASIC OUTPUT (PRINT)
# =============================================================================

# Simple print
print("Hello, World!")

# Print multiple items (space-separated by default)
print("Hello", "World", "!")  # Hello World !

# Custom separator
print("a", "b", "c", sep="-")  # a-b-c
print("a", "b", "c", sep="")   # abc

# Custom end (default is newline)
print("Hello", end=" ")
print("World")  # Hello World (on same line)

# Print without newline at end
print("Processing", end="...")
print("Done!")  # Processing...Done!


# =============================================================================
# BASIC INPUT
# =============================================================================

# input() always returns a string
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Example function
def get_and_print_input():
    """Read input and print it."""
    line = input("Enter something: ")
    print(f"You entered: {line}")

# Uncomment to test:
# get_and_print_input()


# =============================================================================
# TYPE CONVERSION WITH INPUT
# =============================================================================

# ⚠️ input() ALWAYS returns a string
# You must convert it to other types

# Integer input
def get_integer():
    """Read an integer from user."""
    value = input("Enter an integer: ")
    return int(value)

# Float input
def get_float():
    """Read a float from user."""
    value = input("Enter a decimal: ")
    return float(value)

# Example usage:
# age = int(input("Enter your age: "))
# price = float(input("Enter price: "))

# Inline conversion
# num = int(input("Enter number: "))


# =============================================================================
# PARSING INPUT
# =============================================================================

# split() - split string into list
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Default split (whitespace)
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Reading comma-separated numbers
def read_integers():
    """Read comma-separated integers."""
    line = input("Enter integers (comma-separated): ")
    parts = line.split(",")
    
    numbers = []
    for part in parts:
        numbers.append(int(part.strip()))  # strip() removes whitespace
    return numbers

# Uncomment to test:
# nums = read_integers()
# print(nums)

# One-liner version
# nums = [int(x.strip()) for x in input("Numbers: ").split(",")]


# =============================================================================
# READING MULTIPLE VALUES
# =============================================================================

# Space-separated values
def read_two_numbers():
    """Read two space-separated numbers."""
    line = input("Enter two numbers (space-separated): ")
    parts = line.split()
    return int(parts[0]), int(parts[1])

# Using unpacking
# x, y = input("Enter x y: ").split()
# x, y = int(x), int(y)

# Or with map()
# x, y = map(int, input("Enter x y: ").split())


# =============================================================================
# MULTIPLE ASSIGNMENT
# =============================================================================

# Assign multiple variables at once
a, b = 10, 20
print(a, b)  # 10 20

x, y, z = 1, "hello", True
print(x, y, z)  # 1 hello True

# Swapping values
a, b = b, a
print(a, b)  # 20 10


# =============================================================================
# FORMATTED OUTPUT
# =============================================================================

name = "Alice"
age = 25
score = 95.5

# f-strings (recommended)
print(f"Name: {name}, Age: {age}")

# Format specifiers
print(f"Score: {score:.2f}")           # 95.50 (2 decimal places)
print(f"Score: {score:.0f}")           # 96 (rounded, no decimals)
print(f"Percentage: {score/100:.1%}")  # 95.5%

# Padding and alignment
print(f"|{name:10}|")   # |Alice     | (left, 10 chars)
print(f"|{name:>10}|")  # |     Alice| (right, 10 chars)
print(f"|{name:^10}|")  # |  Alice   | (center, 10 chars)

# Numbers with padding
print(f"{42:05d}")      # 00042 (pad with zeros)
print(f"{42:5d}")       # "   42" (pad with spaces)


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Simple calculator
def add_two_numbers():
    """Add two numbers from user input."""
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"{a} + {b} = {a + b}")
    except ValueError:
        print("Invalid input! Please enter integers.")

# Temperature converter
def celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit."""
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Read until empty
def read_until_empty():
    """Keep reading until empty input."""
    items = []
    while True:
        line = input("Enter item (empty to stop): ")
        if line == "":
            break
        items.append(line)
    return items

# Simple menu
def show_menu():
    """Display a simple menu."""
    print("\n=== Menu ===")
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    return choice


# =============================================================================
# READING SPECIFIC FORMATS
# =============================================================================

# Reading a list of integers
def read_int_list():
    """Read space-separated integers."""
    line = input("Enter integers: ")
    return [int(x) for x in line.split()]

# Reading key-value pairs
def read_key_value():
    """Read key=value format."""
    line = input("Enter key=value: ")  # e.g., "name=Alice"
    key, value = line.split("=")
    return key.strip(), value.strip()

# Reading CSV-style data
def read_csv_line():
    """Read comma-separated values."""
    line = input("Enter CSV: ")  # e.g., "Alice,25,NYC"
    return line.split(",")


# =============================================================================
# STRING TO OTHER TYPES
# =============================================================================

# String to int
num_str = "42"
num_int = int(num_str)       # 42

# String to float
price_str = "19.99"
price_float = float(price_str)  # 19.99

# String to bool (⚠️ be careful!)
# bool("False") is True! (non-empty string)
# Use explicit check instead:
def str_to_bool(s):
    """Convert string to boolean."""
    return s.lower() in ("true", "1", "yes", "y")

print(str_to_bool("True"))   # True
print(str_to_bool("False"))  # False

# List of strings to list of ints
str_list = ["1", "2", "3"]
int_list = [int(x) for x in str_list]  # [1, 2, 3]
# Or: int_list = list(map(int, str_list))


# =============================================================================
# VALIDATION
# =============================================================================

# Validate integer input
def get_valid_int(prompt):
    """Keep asking until valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Please enter an integer.")

# Validate range
def get_int_in_range(prompt, min_val, max_val):
    """Get integer within specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid! Please enter an integer.")

# Uncomment to test:
# age = get_int_in_range("Enter age (0-120): ", 0, 120)


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. input() always returns string
age = input("Age: ")  # "25" (string, not int!)
# age + 1  # ❌ TypeError
age = int(input("Age: "))  # ✅ Now it's an int

# 2. Empty input
line = input("Enter: ")
if line:  # Check if not empty
    print(f"You entered: {line}")
else:
    print("Nothing entered")

# 3. Whitespace issues
line = input("Enter: ")  # User enters "  hello  "
line = line.strip()      # Remove leading/trailing whitespace

# 4. int() fails on invalid input
# int("hello")  # ❌ ValueError
# int("12.5")   # ❌ ValueError (use float first)
# int(float("12.5"))  # ✅ 12


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Always convert input() result to appropriate type
# 2. Use try/except for robust input handling
# 3. Use .strip() to remove extra whitespace
# 4. Use .split() to parse structured input
# 5. Use f-strings for formatted output
# 6. Validate user input before using it

# 7. Common input patterns:
#    - Single int: int(input())
#    - Single float: float(input())
#    - Space-separated ints: list(map(int, input().split()))
#    - Comma-separated: input().split(",")
