# add your code here
#encrypt only
encrypt_key = {
    'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K',
    'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q',
    'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W',
    'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C',
    'Y': 'D', 'Z': 'E',
    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k',
    'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q',
    'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w',
    's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c',
    'y': 'd', 'z': 'e'
}

decrypted_input = input("Please enter a message to encrypt: ")
encrypted_output = ""

for char in decrypted_input:
    if char in encrypt_key:
        encrypted_output += encrypt_key[char]
    else:
        encrypted_output += char

print("Your encrypted output: ", encrypted_output)