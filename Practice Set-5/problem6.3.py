dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 30, "d": 4, "e": 5}

merged = dict1.copy()   
merged.update(dict2)  

print(merged)


merged = {**dict1, **dict2}
print(merged)


merged = dict1 | dict2
print(merged)
