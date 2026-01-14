class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


result = MathUtils.add(10, 5)
print("Result of addition is: ", result)

MathUtils.description()