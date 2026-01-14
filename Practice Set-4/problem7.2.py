def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test examples
print(safe_divide(10, 2))   # 5.0
print(safe_divide(5, 0))    # Cannot divide by zero

