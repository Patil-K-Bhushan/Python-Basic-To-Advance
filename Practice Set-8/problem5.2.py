import os

current_dir = os.getcwd()

# Loop through all files in the current directory
for file in os.listdir(current_dir):
    if file.endswith(".tmp"):
        file_path = os.path.join(current_dir, file)
        os.remove(file_path)
        print(f"Deleted: {file}")

print("All .tmp files deleted (if any existed).")