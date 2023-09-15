class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero is not supported")
        return round(self.value / other.value, 1)




num1 = Calculator(5)
num2 = Calculator(3)

result_add = num1 + num2
print("Addition:", result_add)

result_sub = num1 - num2
print("Subtraction:", result_sub)

result_mul = num1 * num2
print("Multiplication:", result_mul)

result_div = num1 / num2
print("Division:", result_div)
