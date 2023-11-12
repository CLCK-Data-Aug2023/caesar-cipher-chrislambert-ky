# add your code here
#This assignment specifically mentions shift.  I need to figure this out.

def create_shift_dict(shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return dict(zip(alphabet, shifted_alphabet)), dict(zip(shifted_alphabet, alphabet))

encrypt_key, decrypt_key = create_shift_dict(5)

ed = input("Would you like to encrypt or decrypt a message (not case sensitive)? ")

if ed.lower() == "encrypt":
    decrypted_input = input("Please enter a message to encrypt: ")
    encrypted_output = ""

    for char in decrypted_input:
        lower_char = char.lower()
        if lower_char in encrypt_key:
            # Preserve the case of the original character
            encrypted_char = encrypt_key[lower_char]
            encrypted_output += encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            encrypted_output += char

    print("Your decrypted message: ", decrypted_input)
    print("Your encrypted message: ", encrypted_output)

elif ed.lower() == "decrypt":
    encrypted_input = input("Please enter a message to decrypt: ")
    decrypted_output = ""

    for char in encrypted_input:
        lower_char = char.lower()
        if lower_char in decrypt_key:
            # Preserve the case of the original character
            decrypted_char = decrypt_key[lower_char]
            decrypted_output += decrypted_char.upper() if char.isupper() else decrypted_char
        else:
            decrypted_output += char
    
    print("Your encrypted message: ", encrypted_input)
    print("Your decrypted message: ", decrypted_output)

else:
    print("Invalid option chosen. Please type 'encrypt' or 'decrypt'. Input is forced into lower case and is not case sensitive.")
