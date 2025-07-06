import random
import string

def generate_password(length):
    if length < 4:
        return None, " Password length should be at least 4 for good security."

    # Define character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = upper + lower + digits + symbols

    # Ensure at least one character from each category
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result
    random.shuffle(password)

    return ''.join(password), None

# Get user input
try:
    length = int(input("Enter the desired password length (min 4): "))
    password, error = generate_password(length)
    if error:
        print(error)
    else:
        print("✅ Generated Password:", password)
except ValueError:
    print(" Please enter a valid number.")

