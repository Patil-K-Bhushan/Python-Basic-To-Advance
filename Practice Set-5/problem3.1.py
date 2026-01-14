coordinates = (10, 20)

print(coordinates)
# coordinates[0] = 50 # Error Occurs as tuples object doesn't support item assignment

list1 = list(coordinates)
list1[0] = 50
t = tuple(list1)
print(t)