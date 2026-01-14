def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("🔹 Function is about to run...")
        result = func(*args, **kwargs)
        print("🔹 Function has finished running.")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, city="Unknown"):
    print(f"Hello {name} from {city}!")


print(add(3, 4))
greet("Alice", city="Delhi")