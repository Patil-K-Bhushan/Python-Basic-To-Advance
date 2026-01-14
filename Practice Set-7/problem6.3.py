from functools import reduce


nums3 = [1, 2, 3, 4]

product = reduce(lambda a, b: a * b, nums3)
print("Product: ",product)