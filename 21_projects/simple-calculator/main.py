
try:
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Operations are\n1. For addition press \"+\"\n2. For subtraction press \"-\"\n3. For multiplication press \"*\"\n4. For division press \"/\"\n\nTo quit enter \"q\" or \"quit\"")
        o = input("Enter the operation: ")

        match o:
            case "+":
                print(f"The result is: {a + b}")
            case "-":
                print(f"The result is: {a - b}")
            case "*":
                print(f"The result is: {a * b}")
            case "/":
                print(f"The result is: {a / b}")

        if "q" in o or "quit" in o:
            print("Program executed successfully!")
            break

except Exception as e:
    print("Enter valid number of a and b",e)
