import random
import string

def get_user_preferences():
    """Get password requirements from user with validation"""
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Password must be at least 8 characters long.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    return length, use_uppercase, use_numbers, use_symbols

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    """Generate a secure password based on user preferences"""
    
    # Build character pool
    characters = string.ascii_lowercase  # Always include lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one character type is selected
    if len(characters) == len(string.ascii_lowercase):
        print("Warning: Only lowercase letters selected. Consider adding more character types for better security.")
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Secure Password Generator")
    print("-" * 30)
    
    length, use_uppercase, use_numbers, use_symbols = get_user_preferences()
    
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    
    print(f"\nGenerated Password: {password}")
    print(f"Length: {len(password)} characters")
    print(f"Complexity: {'Strong' if len(set(password)) > 6 else 'Weak'}")

if __name__ == "__main__":
    main()
