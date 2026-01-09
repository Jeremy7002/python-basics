
def multiplication_table(number):
    """Multiplication table of the given integer number from 1 to 10"""
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def main():
    num = int(input("Enter an integer to see its multiplication table: "))
    multiplication_table(num)

if __name__=="__main__":
    print(multiplication_table.__doc__)
    main()