import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej!")
        return math.sqrt(a)

    def log(self, a, base):
        if a <= 0 or base <= 0:
            raise ValueError("Argumenty logarytmu muszą być dodatnie!")
        return math.log(a, base)



