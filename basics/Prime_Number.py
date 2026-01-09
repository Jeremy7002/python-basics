def is_prime(number):
    """Check if a number is prime."""
    import math as m  
    if number <= 1:
        return False
    for i in range(2, int(m.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print("Prime")
    else:
        print("Not Prime")

if __name__ == "__main__":
    print(is_prime.__doc__)  
    main()
