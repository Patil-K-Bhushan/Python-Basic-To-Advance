def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1 # It creates a local variable z which is destroyed after function execution
    return c

def greet():
    z = 32 # z is a local variable
    print("Hello")

z = 8 # z is a global variable
print(z)
print(sum(4, 6))
print(z)
