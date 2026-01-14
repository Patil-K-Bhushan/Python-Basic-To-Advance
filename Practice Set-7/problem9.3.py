import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class InvalidInputError(Exception):
    pass


def get_positive_number():
    user_input = input("Enter a positive number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        return None

    try:
        num = float(user_input)
        if num <= 0:
            raise InvalidInputError("Number must be positive.")
        return num

    except ValueError:
        raise InvalidInputError("Input is not a valid number.")


while True:
    try:
        result = get_positive_number()

        if result is None:
            print("Goodbye")
            break

        print("You entered:", result)

    except InvalidInputError as e:
        print("⚠️ Invalid input. Please try again.")
        logging.error(e)
