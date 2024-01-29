import sys

def encrypt(message, k):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + k
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, k):
    return encrypt(message, -k)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <message> <key>")
        sys.exit(1)
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
