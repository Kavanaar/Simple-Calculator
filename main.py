from calculator import Calculator


def get_number(prompt: str) -> float:
    """Safely take numeric input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    calc = Calculator()
    history = []

    while True:
        print("\n====== SIMPLE CALCULATOR ======")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. View History")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        try:
            if choice == "1":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print("Result:", result)

            elif choice == "2":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print("Result:", result)

            elif choice == "3":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print("Result:", result)

            elif choice == "4":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.divide(a, b)
                print("Result:", result)

            elif choice == "5":
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = calc.power(a, b)
                print("Result:", result)

            elif choice == "6":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.modulus(a, b)
                print("Result:", result)

            elif choice == "7":
                a = get_number("Enter number: ")
                result = calc.square_root(a)
                print("Result:", result)

            elif choice == "8":
                print("\n--- Calculation History ---")
                if not history:
                    print("No calculations yet.")
                else:
                    for item in history:
                        print(item)
                continue

            elif choice == "9":
                print("👋 Exiting Calculator. Thank you!")
                break

            else:
                print("❌ Invalid option. Please choose 1-9.")
                continue

            history.append(f"Option {choice} → Result: {result}")

        except Exception as e:
            print("⚠ Error:", e)


if __name__ == "__main__":
    main()
