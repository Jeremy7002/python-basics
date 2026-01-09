def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def main():
    print("Enter a string to reverse: ")
    test_string = input().strip()
    reversed_string = reverse_string(test_string)
    print(f"Original String: {test_string}")
    print(f"Reversed String: {reversed_string}")

if __name__ == "__main__":
    print(reverse_string.__doc__)
    main()