"""Demonstrates the use of type hints in Python code."""

def add(a_f: int, b_c: int) -> int:
    """Adds two integers."""
    return a_f + b_c


def greet(name: str) -> str:
    """Greets the person with the provided name."""
    return f"Hello, {name}!"


def divide(abc: int, bcd: int) -> float:
    """Divides a by b and returns a float."""
    if bcd == 0:
        raise ValueError("Cannot divide by zero.")
    return abc / bcd


# Function calls
print(add(3, 5))  # Expected output: 8
print(greet("Alice"))  # Expected output: "Hello, Alice!"
print(divide(10, 2))  # Expected output: 5.0

# print(add(3, "five"))  # This will raise an error
# print(greet(123))  # This will raise an error
# print(divide(10, "two"))  # This will raise an error
