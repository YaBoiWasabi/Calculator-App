import random
import string

def generate_password(length=12):
    # Define character sets for the password
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = letters + digits + special_characters

    # Generate a random password by selecting characters randomly from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example: Generate a password of length 16
generated_password = generate_password(16)
print("Generated Password:", generated_password)
