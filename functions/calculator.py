def add(a, b):
    """Returns the sum of a and b."""
    print(f"The sum of {a} and {b} is {a + b}")
def sub(a, b):
    """Returns the difference of a and b."""
    print(f"The difference of {a} and {b} is {a - b}")
def multiply(a, b):
    """Returns the product of a and b."""
    print(f"The product of {a} and {b} is {a * b}")
def divide(a, b):
    """Returns the quotient of a and b."""
    while b == 0:
        print("Cannot divide by zero.")
        b = float(input("Enter a non-zero second number: "))
    print(f"The quotient of {a} and {b} is {(a / b):.4f}")
def main():
    print("This is a calculator module. It provides basic arithmetic operations.")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            print("Thank You for Using Our Service")
            break
        elif choice in {'1', '2', '3', '4'}:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                add(num1, num2)
            elif choice == '2':
                sub(num1, num2)
            elif choice == '3':
                multiply(num1, num2)
            elif choice == '4':
                divide(num1, num2)
                
if __name__ == "__main__":
    main()