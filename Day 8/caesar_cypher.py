alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def encrypt(original_text,shift_amount)  :
    shifted_array = []
    for char in original_text :
        original_index = alphabet.index(char)
        shifted_index = original_index + shift_amount
        if shifted_index > 26 :
            shifted_index -= 26
        new_char = alphabet[shifted_index]
        shifted_array.append(new_char)
        
    encrypted = ''.join(shifted_array)
    print(f'Your encrypted password is : {encrypted}')

def decrypt(original_text,shift_amount)  :
    shifted_array = []
    for char in original_text :
        original_index = alphabet.index(char)
        shifted_index = original_index - shift_amount
        new_char = alphabet[shifted_index]
        shifted_array.append(new_char)
        
    decrypted = ''.join(shifted_array)
    print(f'Your decrypted password is : {decrypted}')

    
        
# if direction == 'decode' :
#     decrypt(text,shift)
# elif direction == 'encode' :
#     encrypt(text,shift)
# elif direction != 'decode' and direction != 'encode' :
#     print('try again')

encrypt(text,shift)