def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char  # Non-alphabet characters remain the same
    return result

def brute_force_decrypt(text):
    print("\nBrute Force Decryption:")
    for i in range(1, 27):
        print(f"Shift {i}: {caesar_cipher(text, i, 'decrypt')}")

def main():
    print("Welcome to the Advanced Caesar Cipher Program!")
    print("Options:\n1. Encrypt\n2. Decrypt\n3. Brute Force Decrypt\n")
    
    choice = input("Enter the number of your choice: ")
    message = input("Enter your message: ")
    
    if choice == '1':
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"\nEncrypted Message: {encrypted_message}")
        
    elif choice == '2':
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print(f"\nDecrypted Message: {decrypted_message}")
        
    elif choice == '3':
        brute_force_decrypt(message)
        
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
