# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# try:
#     c = a/b
#     print(c)

# except Exception as e:
#     print(e)

# finally:
#     print("This is always executed")


def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
    
    except Exception as e:
        print(e)
        return None
    
    finally:
        print("This is always executed")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2; "))
divide(a, b)