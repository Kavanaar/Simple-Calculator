class Calculator:
    """
    A simple calculator class that supports basic and advanced operations.
    """

    def add(self, a: float, b: float) -> float:
        """Return sum of two numbers"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return difference of two numbers"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return product of two numbers"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return division of two numbers"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Return a raised to the power b"""
        return a ** b

    def modulus(self, a: float, b: float) -> float:
        """Return modulus of two numbers"""
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulus with zero")
        return a % b

    def square_root(self, a: float) -> float:
        """Return square root of a number"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5