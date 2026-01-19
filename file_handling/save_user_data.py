def save_user_to_file(user_data, filename,i):
    """Saves user data dictionary to a text file."""
    try:
        with open(filename, 'a') as file:
            file.write("User {}:\n".format(i))
            for key, value in user_data.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving data: {e}")

def main():
    i=1
    while True:
        print("Enter User Details:")
        name = input("Name: ")
        age = input("Age: ")
        email = input("Email: ")
        user_data = {
            "Name": name,
            "Age": age,
            "Email": email
        }
        save_user_to_file(user_data, "text_files/user_data.txt",i)
        i+=1
        ch=input("Do you want to add another user? (y/n): ")
        if ch.lower() != 'y':
            break
    
if __name__ == "__main__":
    main()
