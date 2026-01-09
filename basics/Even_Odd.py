def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def main():
    num = int(input("Enter a number: "))
    print("Even" if is_even(num) else "Odd")

if __name__ == "__main__":
    main()
