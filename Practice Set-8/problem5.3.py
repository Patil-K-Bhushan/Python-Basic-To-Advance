import os
import sys

if len(sys.argv) != 2:
    print("Usage: python folder_size.py <folder_path>")
    sys.exit(1)

folder_path = sys.argv[1]

if not os.path.isdir(folder_path):
    print("Error: The given path is not a valid folder.")
    sys.exit(1)

total_size = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        total_size += os.path.getsize(file_path)

print(f"Total size of files in '{folder_path}': {total_size} bytes")
