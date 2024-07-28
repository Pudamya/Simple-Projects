import random
import string

def generate_password(length):
    """
    Generate a random password of specified length.
    """
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    """
    Main function to interact with the user.
    """
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()

