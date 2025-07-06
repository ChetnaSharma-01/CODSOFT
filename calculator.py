class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error! Division by zero."
        return self.num1 / self.num2


# User input
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    calc = Calculator(number1, number2)

    if operation == '+':
        result = calc.add()
    elif operation == '-':
        result = calc.subtract()
    elif operation == '*':
        result = calc.multiply()
    elif operation == '/':
        result = calc.divide()
    else:
        result = "Invalid operation selected!"

    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")
