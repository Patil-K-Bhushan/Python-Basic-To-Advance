# f = open("harry.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("harry.txt", "r") as f:
    content = f.read()
    print(content)