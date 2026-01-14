def calculate_area(length, width=10):
    return length * width


area1 = calculate_area(5, 4)
print("Area with length and width:", area1)


area2 = calculate_area(5)
print("Area with only length (default width):", area2)
