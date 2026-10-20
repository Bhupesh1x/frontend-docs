"""
=============================================================================
 ERROR HANDLING
=============================================================================
 Error handling lets your program gracefully handle unexpected situations
 instead of crashing. Python uses try/except for exception handling.
=============================================================================
"""

# =============================================================================
# BASIC TRY/EXCEPT
# =============================================================================

# Without error handling - program crashes
# result = 10 / 0  # ❌ ZeroDivisionError

# With error handling - program continues
try:
    result = 10 / 0
except:
    print("An error occurred!")
    
print("Program continues...")  # This runs


# =============================================================================
# CATCHING SPECIFIC EXCEPTIONS
# =============================================================================

# Catch specific exception types
def divide(a, b):
    """Divide two numbers with error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Error message, then None


# Multiple exception types
def convert_to_int(value):
    """Convert string to int with error handling."""
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid integer")
        return None
    except TypeError:
        print(f"Error: Cannot convert {type(value)} to int")
        return None

print(convert_to_int("42"))     # 42
print(convert_to_int("hello"))  # Error message, None
print(convert_to_int(None))     # Error message, None


# =============================================================================
# CATCHING MULTIPLE EXCEPTIONS
# =============================================================================

# Method 1: Separate except blocks
def process_data(data, index):
    try:
        return int(data[index])
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Cannot convert to integer")
    except TypeError:
        print("Error: Invalid data type")

# Method 2: Tuple of exceptions
def process_data_v2(data, index):
    try:
        return int(data[index])
    except (IndexError, ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


# =============================================================================
# ACCESSING EXCEPTION INFORMATION
# =============================================================================

def safe_divide(a, b):
    """Divide with detailed error info."""
    try:
        return a / b
    except ZeroDivisionError as error:
        print(f"Error type: {type(error).__name__}")
        print(f"Error message: {error}")
        return None

safe_divide(10, 0)
# Error type: ZeroDivisionError
# Error message: division by zero


# =============================================================================
# TRY/EXCEPT/ELSE
# =============================================================================

# 'else' runs only if NO exception occurred
def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        # Only runs if try block succeeds
        print(f"Result: {result}")
        return result

divide_with_else(10, 2)  # Result: 5.0
divide_with_else(10, 0)  # Cannot divide by zero!


# =============================================================================
# TRY/EXCEPT/FINALLY
# =============================================================================

# 'finally' ALWAYS runs (cleanup code)
def example_finally():
    try:
        print("Trying...")
        result = 10 / 0
    except ZeroDivisionError:
        print("Error occurred!")
    finally:
        print("This always runs!")  # Always executes

example_finally()
# Trying...
# Error occurred!
# This always runs!

# Common use: cleanup resources
def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    finally:
        if file:
            file.close()  # Always close the file


# =============================================================================
# COMMON EXCEPTION TYPES
# =============================================================================

# ValueError - wrong value for type
# int("hello")  # ValueError

# TypeError - wrong type
# "hello" + 5  # TypeError

# IndexError - index out of range
# [1, 2, 3][10]  # IndexError

# KeyError - key not in dict
# {"a": 1}["b"]  # KeyError

# ZeroDivisionError - division by zero
# 10 / 0  # ZeroDivisionError

# FileNotFoundError - file doesn't exist
# open("nonexistent.txt")  # FileNotFoundError

# AttributeError - attribute doesn't exist
# None.something  # AttributeError

# NameError - name not defined
# print(undefined_variable)  # NameError


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Safe division function
def divide_numbers(a: str, b: str) -> None:
    """Divide two numbers from string inputs."""
    try:
        a_int = int(a)
        b_int = int(b)
        result = a_int / b_int
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid number: {e}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

divide_numbers("10", "2")            # Result: 5.0
divide_numbers("12", "0")            # Cannot divide by zero!
divide_numbers("hello", "2")         # Invalid number

# Safe list access
def get_element(lst, index, default=None):
    """Safely get element from list."""
    try:
        return lst[index]
    except (IndexError, TypeError):
        return default

print(get_element([1, 2, 3], 0))     # 1
print(get_element([1, 2, 3], 10))    # None
print(get_element([1, 2, 3], 10, -1)) # -1 (custom default)

# Safe dict access (though .get() is preferred)
def get_dict_value(d, key, default=None):
    """Safely get dict value."""
    try:
        return d[key]
    except KeyError:
        return default

# Input validation
def get_integer_input(prompt, min_val=None, max_val=None):
    """Get validated integer input."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer!")


# =============================================================================
# RAISING EXCEPTIONS
# =============================================================================

# Use 'raise' to throw an exception
def validate_age(age):
    """Validate age is positive."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")


# Re-raising exceptions
def process_item(item):
    try:
        # ... some processing ...
        if item is None:
            raise ValueError("Item cannot be None")
    except ValueError:
        print("Logging error...")
        raise  # Re-raise the same exception


# =============================================================================
# CATCH-ALL EXCEPTION HANDLER
# =============================================================================

# Use Exception to catch most exceptions
def safe_operation(func, *args):
    """Execute function safely."""
    try:
        return func(*args)
    except Exception as e:
        print(f"Error ({type(e).__name__}): {e}")
        return None

# ⚠️ Avoid bare except: (catches everything including KeyboardInterrupt)
# try:
#     ...
# except:  # ❌ Too broad!
#     pass

# Better:
# except Exception:  # ✅ Catches most errors but not system exits


# =============================================================================
# CONTEXT MANAGERS (SAFER APPROACH)
# =============================================================================

# 'with' statement handles cleanup automatically
# This is the preferred way to handle files

# Old way (need finally for cleanup):
# f = open("file.txt")
# try:
#     content = f.read()
# finally:
#     f.close()

# Better way (with statement):
# with open("file.txt") as f:
#     content = f.read()
# # File is automatically closed, even if exception occurs


# =============================================================================
# ⚠️ COMMON PITFALLS
# =============================================================================

# 1. Too broad exception handling
try:
    # ... lots of code ...
    pass
except Exception:
    pass  # ❌ Silently swallows ALL errors!

# Better: catch specific exceptions

# 2. Catching exceptions too early
def bad_function():
    try:
        return int("hello")
    except ValueError:
        pass  # ❌ Returns None silently
    
# 3. Not handling the exception properly
try:
    result = 10 / 0
except:
    print("Error")  # What error? No useful info!

# Better:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Division error: {e}")


# =============================================================================
# 💡 QUICK TIPS
# =============================================================================

# 1. Always catch specific exceptions when possible
# 2. Use 'as e' to access exception details
# 3. Use 'finally' for cleanup code (closing files, connections)
# 4. Don't use bare 'except:' - catch Exception at minimum
# 5. Use 'with' statement for resource management (files, connections)
# 6. Let exceptions propagate if you can't handle them meaningfully
# 7. Use 'raise' to throw exceptions when input is invalid

# Exception hierarchy (simplified):
# BaseException
# └── Exception
#     ├── ValueError
#     ├── TypeError
#     ├── KeyError
#     ├── IndexError
#     ├── ZeroDivisionError
#     ├── FileNotFoundError
#     └── ... many more
