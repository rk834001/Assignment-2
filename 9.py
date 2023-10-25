class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num != 0:
            self.value /= num
        else:
            print("Division by zero is not allowed.")

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        if other != 0:
            return self.value / other
        else:
            print("Division by zero is not allowed.")

# Example usage:
calculator = Calculator(10)
calculator.add(5)
print("Addition:", calculator.value)

calculator.subtract(3)
print("Subtraction:", calculator.value)

calculator.multiply(4)
print("Multiplication:", calculator.value)

calculator.divide(2)
print("Division:", calculator.value)

# Operator overloading examples
result = calculator + 8
print("Operator Overloading - Addition:", result)

result = calculator - 2
print("Operator Overloading - Subtraction:", result)

result = calculator * 6
print("Operator Overloading - Multiplication:", result)

result = calculator / 4
print("Operator Overloading - Division:", result)
