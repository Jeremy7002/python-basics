def sum_of_digits(number):
    """Return the sum of the digits of the given integer number"""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10 
    return total

def main():
    num = int(input("Enter a non-negative integer: "))
    result = sum_of_digits(num)
    print(f"The sum of the digits is: {result}")

if __name__ == "__main__":
    print(sum_of_digits.__doc__)
    main()