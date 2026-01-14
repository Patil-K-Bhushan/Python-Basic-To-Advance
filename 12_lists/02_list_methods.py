marks = [5, 2, 21, 5 ,7]
exxtra_marks = [53,23,32]

print(marks)
marks.append(63)
print(marks)
marks.pop()
print(marks)
marks.extend(exxtra_marks)
print(marks)

my_list = [1, 2, 3]

my_list.append(4)   # [1, 2, 3, 4]
my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
my_list.remove(2)   # [1, 99, 3, 4]
my_list.pop()       # Removes last element -> [1, 99, 3]
my_list.reverse()   # [3, 99, 1]
my_list.sort()      # [1, 3, 99]