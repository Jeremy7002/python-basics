def find_duplicates(input_list):
    """
    Returns a list of duplicate elements from the input list.
    """
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

def main():
    print("Enter elements of the list separated by spaces: ")
    input_list = input().strip().split()
    duplicates = find_duplicates(input_list)
    
    if duplicates:
        print("Duplicate elements found:", duplicates)
    else:
        print("No duplicate elements found.")

if __name__ == "__main__":
    print(find_duplicates.__doc__)
    main()