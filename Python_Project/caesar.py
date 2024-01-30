import sys

def encrypt(message, k):
    encrypted_message= ""
    for letters in message:
        letters_numbers=ord (letters)
        letters_shift= letters_numbers+k
        encrypted_letter= chr(letters_shift)
        encrypted_message= encrypted_message+ encrypted_letter
    return encrypted_message



def decrypt(message, k):
    return encrypt(message, -k)


if __name__ == "__main__":
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
