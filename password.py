import random
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    # Initialize an empty list to store the character types to be used
    chars_to_use = []

    # Add characters based on user preferences
    if use_lower:
        chars_to_use.append(string.ascii_lowercase)
    if use_upper:
        chars_to_use.append(string.ascii_uppercase)
    if use_digits:
        chars_to_use.append(string.digits)
    if use_special:
        chars_to_use.append(string.punctuation)

    # Check if at least one character type is selected
    if not any([use_lower, use_upper, use_digits, use_special]):
        raise ValueError("At least one character type (lowercase, uppercase, digits, special) must be selected.")

    # Create the password
    password = []
    # Ensure at least one character from each selected category
    for _ in range(length):
        # Choose a random character type from chars_to_use
        char_type = random.choice(chars_to_use)
        # Choose a random character from the selected char_type
        char = random.choice(char_type)
        password.append(char)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert list to string
    password_str = ''.join(password)
    
    return password_str

def main():
    print("Welcome to the Advanced Password Generator!")
    
    try:
        # Get desired length of the password from user input
        length = int(input("Enter the desired length of the password: "))
        
        # Get user preferences for character types
        use_lower = input("Include lowercase letters? (yes/no): ").lower() in ['yes', 'y']
        use_upper = input("Include uppercase letters? (yes/no): ").lower() in ['yes', 'y']
        use_digits = input("Include digits? (yes/no): ").lower() in ['yes', 'y']
        use_special = input("Include special characters? (yes/no): ").lower() in ['yes', 'y']
        
        # Generate the password
        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        
        # Display the generated password
        print(f"Generated password: {password}")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
