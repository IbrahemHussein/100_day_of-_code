from pdb import Restart
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def caesar(start_text,shift_amunt,cipher_direction):
    end_text=''
    if cipher_direction =='decode':
        shift_amunt*=-1
    for letter in start_text:
        #if user enter a number / symbol / space
        #e.g start_text="meet me in 3"
        #end_text="**** ** ** 3 "
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=position+shift_amunt
            end_text+=alphabet[new_position]
        else:
            end_text+=letter
    print(f'the {cipher_direction} text is {end_text}')
#ngwfmjr
#print the logo from art.py when the program starts.
print(logo)
#creating a while loop that continues to execute the program if the user types 'yes'.
restart='yes'
while restart =='yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift % 26
    caesar(start_text=text,shift_amunt=shift,cipher_direction=direction)
    restart=input('Type "yes" if you went to go again,Otherwise type "no " ').lower()
    if restart=='no':
        print('Goodbye')
        break

