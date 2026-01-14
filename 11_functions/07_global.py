def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z # Please modify the global variable z
    z = 0
    return c# This will modify the global variable z and not create a local variable z

z = 3
print(z)
print(sum(3,12))
print(z)