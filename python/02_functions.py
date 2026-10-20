"""
=============================================================================
 FUNCTIONS
=============================================================================
 Functions are reusable blocks of code that perform a specific task.
 They help organize code, reduce repetition, and improve readability.
=============================================================================
"""

# =============================================================================
# BASIC FUNCTION DEFINITION
# =============================================================================

def greet():
    """A simple function with no parameters."""
    print("Hello world!")

def say_goodbye():
    """Another simple function."""
    print("Goodbye!")

# Calling functions
greet()        # Hello world!
say_goodbye()  # Goodbye!


# =============================================================================
# FUNCTION PARAMETERS & ARGUMENTS
# =============================================================================

# Parameter: variable in function definition (name)
# Argument: actual value passed when calling (Alice)

def farewell(name):
    """Function with one parameter."""
    print(f"Goodbye, {name}!")

farewell("Alice")  # Goodbye, Alice!
farewell("Bob")    # Goodbye, Bob!


# Multiple parameters
def add_two(a, b):
    """Function with two parameters."""
    print(a + b)

def add_three(a, b, c):
    """Function with three parameters."""
    print(a + b + c)

add_two(1, 2)       # 3
add_three(1, 2, 5)  # 8


# =============================================================================
# RETURN STATEMENT
# =============================================================================

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

result = multiply(5, 3)
print(result)           # 15
print(multiply(8, 2))   # 16

# Function without return statement returns None implicitly
def no_return():
    x = 10

print(no_return())  # None


# =============================================================================
# TYPE HINTS
# =============================================================================

# Type hints are optional annotations that help with code readability
# Python does NOT enforce them - they're just for developer reference

def product(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b

print(product(4, 2))  # 8

def print_value(value: str) -> None:
    """Print a value. Returns nothing (None)."""
    print(value)

# ⚠️ Type hints are NOT enforced!
print_value(4)        # Works! Prints: 4
print_value("Hello")  # Prints: Hello


# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================

def greet_user(name, punctuation="!"):
    """Greet with optional punctuation. Default is '!'"""
    print(f"Hello, {name}{punctuation}")

greet_user("World", "!")   # Hello, World!
greet_user("World")        # Hello, World! (uses default)
greet_user("World", "?")   # Hello, World?
greet_user("World", "...")  # Hello, World...

# ⚠️ PITFALL: Default parameters with mutable objects
# Don't do this:
def bad_append(item, items=[]):  # ❌ Shared across calls!
    items.append(item)
    return items

# Do this instead:
def good_append(item, items=None):  # ✅
    if items is None:
        items = []
    items.append(item)
    return items


# =============================================================================
# KEYWORD ARGUMENTS
# =============================================================================

def describe_person(name, age, city):
    """Describe a person with their details."""
    print(f"{name} is {age} years old and lives in {city}")

# Positional arguments (order matters)
describe_person("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
describe_person(city="LA", name="Bob", age=30)

# Mix of both (positional must come first)
describe_person("Charlie", city="Chicago", age=35)


# =============================================================================
# *ARGS AND **KWARGS
# =============================================================================

# *args - accept any number of positional arguments (as tuple)
def sum_all(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)

print(sum_all(1, 2))           # 3
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - accept any number of keyword arguments (as dict)
def print_info(**info):
    """Print all keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC


# =============================================================================
# FUNCTION SCOPE
# =============================================================================

global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(global_var)  # Can access global variables
    print(local_var)   # Can access local variables

demonstrate_scope()
print(global_var)  # Works
# print(local_var)  # ❌ NameError - local_var not accessible outside

# Modifying global variables inside function
counter = 0

def increment():
    global counter  # Must declare 'global' to modify
    counter += 1

increment()
increment()
print(counter)  # 2


# =============================================================================
# EARLY RETURN
# =============================================================================

def check_positive(num):
    """Check if number is positive with early return."""
    if num <= 0:
        return "Not positive"  # Early exit
    
    # Only reaches here if num > 0
    return "Positive"

print(check_positive(-5))  # Not positive
print(check_positive(10))  # Positive


# =============================================================================
# RETURNING MULTIPLE VALUES
# =============================================================================

def get_min_max(numbers):
    """Return both min and max as a tuple."""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9


# =============================================================================
# DOCSTRINGS
# =============================================================================

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area of the rectangle.
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Function must be defined before it's called
# print_hello()  # ❌ NameError if called before definition
def print_hello():
    print("Hello")
print_hello()  # ✅ Works

# 2. Forgetting to return a value
def bad_add(a, b):
    result = a + b
    # Forgot to return! Returns None

print(bad_add(1, 2))  # None (probably not what you wanted)

# 3. Modifying parameter doesn't affect original (for immutable types)
def try_modify(x):
    x = x + 10
    print(f"Inside: {x}")

num = 5
try_modify(num)
print(f"Outside: {num}")  # Still 5! Integers are immutable


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Use descriptive function names (verb + noun)
# ✅ calculate_total(), get_user(), validate_input()
# ❌ calc(), data(), process()

# 2. Keep functions small and focused (single responsibility)

# 3. Use type hints for better code documentation
def greet_typed(name: str) -> str:
    return f"Hello, {name}!"

# 4. Functions are first-class objects (can be passed around)
def apply_operation(func, a, b):
    return func(a, b)

def add(x, y):
    return x + y

print(apply_operation(add, 3, 4))  # 7
