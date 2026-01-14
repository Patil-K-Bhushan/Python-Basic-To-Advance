password = "Y2K123"
entered_pass = input("Enter your password: ")

while(entered_pass != password):
    print("Incorrect password. Try again.")
    entered_pass = input("Enter your password: ")

print("Access granted.")