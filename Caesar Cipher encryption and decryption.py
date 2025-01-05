letters = 'abcdefghijklmnopqrstuvwxyz'
num = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter == ' ':
            ciphertext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter  # Preserve non-alphabet characters
            else:
                new_index = (index + key) % num  # Ensure wrapping
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter  # Preserve non-alphabet characters
            else:
                new_index = (index - key) % num  # Ensure wrapping
                plaintext += letters[new_index]
    return plaintext

user_input = input("Select mode (e for encrypt / d for decrypt): ").lower()
if user_input == 'e':
    print("ENCRYPTION MODE SELECTED")
    key = int(input('Enter a key: '))
    text = input('Enter text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f"CipherText: {ciphertext}")
elif user_input == 'd':
    print("DECRYPTION MODE SELECTED")
    key = int(input('Enter a key: '))
    text = input('Enter text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f"PlainText: {plaintext}")
else:
    print("Invalid input! Please enter 'e' for encryption or 'd' for decryption.")


