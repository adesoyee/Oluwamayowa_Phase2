message= "hello"
k=3
encrypted_message= ""
for letters in message:
    letters_numbers=ord (letters)
    letters_shift= letters_numbers+k
    encrypted_letter= chr(letters_shift)
    encrypted_message= encrypted_message+ encrypted_letter

 
print(encrypted_message)

