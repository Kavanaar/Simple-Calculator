import sys

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f"Addition of given two numbers: {self.a + self.b}")

    def subtraction(self):
        print(f"Subtraction of given two numbers: {self.a - self.b}")

    def multiplication(self):
        print(f"Multiplication of given two numbers: {self.a * self.b}")  

    def division(self):
        try:
            print(f"division of given two numbers: {self.a / self.b}")
        except ZeroDivisionError as e:
            print(f"Can't divide by zero {e}")


while(True):

    print("========Simple Calculator=========")
    print("1. Addition \n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    try:
        choice = int(input("Enter your choice:"))
    except ValueError as e:
        print(f"Enter the valid number {e}")
        continue

    if 1<=choice<5:

        try:
            a = int(input("Enter the First number:"))
            b = int(input("Enter the Second number:"))
        except ValueError as e:
            print(f"Enter the valid number {e}")
            continue
            
        calculate = Calculator(a, b)
        match choice:
            case 1: 
                calculate.addition()
            case 2:
                calculate.subtraction()
            case 3:
                calculate.multiplication()
            case 4:
                calculate.division()
                
    elif choice==5:
        print("Exiting from Calculator")
        sys.exit(0)