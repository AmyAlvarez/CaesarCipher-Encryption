def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

def encrypt_file(input_file, output_file, encryption_func, key):
    with open(input_file, 'r') as file:
        text = file.read()
        encrypted_text = encryption_func(text, key)
    
    with open(output_file, 'w') as file:
        file.write(encrypted_text)
    print("Encryption successful!")

def decrypt_file(input_file, output_file, decryption_func, key):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
        decrypted_text = decryption_func(encrypted_text, key)
    
    with open(output_file, 'w') as file:
        file.write(decrypted_text)
    print("Decryption successful!")

# Example usage
# Replace 'input.txt' with the path of the file you'd like to encrypt or decrypt
input_file = "input.txt"
output_file = "output.txt"
shift = 3
key = 42

encrypt_file(input_file, output_file, caesar_encrypt, shift)
decrypt_file(output_file, 'decrypted.txt', caesar_decrypt, shift)


