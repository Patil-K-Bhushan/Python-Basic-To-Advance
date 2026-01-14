input_file = "input.txt"
output_file = "output.txt"

try:
    with open(input_file, "r") as fin:
        content = fin.read()

    upper_content = content.upper()

    with open(output_file, "w") as fout:
        fout.write(upper_content)

    print("File successfully converted to uppercase and saved to", output_file)

except FileNotFoundError:
    print("Input file not found. Please check the file name.")
except Exception as e:
    print("An error occurred:", e)