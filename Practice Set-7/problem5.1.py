class NegativeNumberError(Exception):
    pass

try:
    num = float(input("Enter a number: "))

    if(num<0):
        raise NegativeNumberError("Negative numbers are not allowed.")
    
    result = 10 / num
    print("Result: ", result)

except ValueError:
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero!")

except NegativeNumberError as e:
    print("Negative", e)

else:
    print("Program executed successfully.")

finally:
    print("Execution finshed.")