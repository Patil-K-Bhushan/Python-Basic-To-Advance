num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  

operation = input("Enter operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"The sum is: {result}")
    case '-':
        result = num1 - num2
        print(f"The difference is: {result}")
    case '*':
        result = num1 * num2
        print(f"The product is: {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The quotient is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation entered.")
        