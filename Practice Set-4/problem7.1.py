def fibonacci_term(n):
    if n <= 1:
        return n
    return fibonacci_term(n-1) + fibonacci_term(n-2)

def fibonacci(n):
    for i in range(n):
        print(fibonacci_term(i), end=" ")

# Test
fibonacci(10)
