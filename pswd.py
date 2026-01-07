import random
import string

def generate_password():
    print("--- Password Generator ---")
    try:
        # User defined criteria
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        char_pool = ""
        if use_letters: char_pool += string.ascii_letters
        if use_numbers: char_pool += string.digits
        if use_symbols: char_pool += string.punctuation

        if not char_pool:
            print("Error: Select at least one character type.")
            return

        # Randomization
        password = "".join(random.choice(char_pool) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Enter a valid number for length.")

if __name__ == "__main__":
    generate_password()