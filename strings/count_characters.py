def count_charcters(s):
    """Count of each character in a string.
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    print("Enter a string to count characters: ")
    test_string = input().strip()
    character_count = count_charcters(test_string)
    for char, count in character_count.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    print(count_charcters.__doc__)
    main()