def file_count_words(file_path):
    """
    Counts the number of words in a given text file.
    """
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
def main():
    file_path = input("Enter the path to the text file: ")
    word_count = file_count_words(file_path)
    print(f"The number of words in the file is: {word_count}")

if __name__ == "__main__":
    print(file_count_words.__doc__)
    main()
