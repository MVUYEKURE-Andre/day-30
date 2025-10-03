"""
Day 30 - Exception Handling Examples
This file demonstrates various exception handling techniques in Python
"""


# Example 1: Basic try/except
def example_file_not_found():
    """Demonstrate FileNotFoundError handling"""
    print("\n=== Example 1: FileNotFoundError ===")
    try:
        with open("non_existent_file.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Error: The file was not found!")
        print("Creating a new file instead...")
        with open("non_existent_file.txt", "w") as file:
            file.write("This file was created after catching an error!")


# Example 2: try/except/else
def example_try_except_else():
    """Demonstrate try/except/else"""
    print("\n=== Example 2: try/except/else ===")
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Division successful! Result: {result}")


# Example 3: try/except/finally
def example_try_except_finally():
    """Demonstrate try/except/finally"""
    print("\n=== Example 3: try/except/finally ===")
    try:
        file = open("test.txt", "w")
        file.write("Test content")
    except IOError:
        print("Error: Could not write to file!")
    finally:
        print("Closing file (this always runs)")
        try:
            file.close()
        except:
            pass


# Example 4: Multiple exceptions
def example_multiple_exceptions():
    """Demonstrate handling multiple exception types"""
    print("\n=== Example 4: Multiple Exceptions ===")
    data = {"name": "John", "age": 30}
    
    try:
        # This will raise KeyError
        print(f"Email: {data['email']}")
    except KeyError:
        print("Error: Key not found in dictionary!")
    except TypeError:
        print("Error: Type mismatch!")


# Example 5: Raising exceptions
def example_raising_exceptions(age):
    """Demonstrate raising custom exceptions"""
    print("\n=== Example 5: Raising Exceptions ===")
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")
        if age < 18:
            raise ValueError("Must be 18 or older!")
        print(f"Age {age} is valid!")
    except ValueError as e:
        print(f"Error: {e}")


# Example 6: Exception with else and finally
def divide_numbers(a, b):
    """Demonstrate complete try/except/else/finally structure"""
    print("\n=== Example 6: Complete try/except/else/finally ===")
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid type for division!")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed")


def main():
    """Run all exception handling examples"""
    print("=" * 60)
    print("DAY 30 - EXCEPTION HANDLING EXAMPLES")
    print("=" * 60)
    
    # Run all examples
    example_file_not_found()
    example_try_except_else()
    example_try_except_finally()
    example_multiple_exceptions()
    example_raising_exceptions(25)
    example_raising_exceptions(15)
    example_raising_exceptions(-5)
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers("10", 2)
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
