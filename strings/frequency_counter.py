def frequency_counter(lst):
    """
    Counts the frequency of each element in the given list.
    """
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

def main():
    sample_list = input("Enter a list of elements separated by spaces: ").split()
    frequencies = frequency_counter(sample_list)
    for item, count in frequencies.items():
        print(f"{item}: {count}")

if __name__ == "__main__":
    print(frequency_counter.__doc__)
    main()