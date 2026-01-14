numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)
