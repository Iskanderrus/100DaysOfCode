import string

REVERSE_SHIFT = -1
alphabet = list(string.ascii_lowercase)
alphabet_size = len(alphabet)


def progress_check():
    message = input('Type "yes" if you want to go again. Otherwise, type "no": ').lower().strip()
    if message == 'yes':
        return True
    elif message == 'no':
        print('Thank you! See you next time.')
        return False
    else:
        print('Your response is not clear. Try again.')
        return progress_check()


def shift_letter(letter, shift):
    letter_index = alphabet.index(letter)
    shifted_index = (letter_index + shift) % alphabet_size
    return alphabet[shifted_index]


def encrypt(text, shift):
    output_list = []
    for letter in text:
        if letter in alphabet:
            new_letter = shift_letter(letter, shift)
            output_list.append(new_letter)
        else:
            output_list.append(letter)
    return ''.join(output_list)


def main():
    in_progress = True
    while in_progress:
        try:
            direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower().strip()
            if direction == 'encode' or direction == 'decode':
                text = input('Type your message:\n').lower().strip()
                shift_num = int(input('Type the shift number:\n'))
                if direction == 'encode':
                    print(f'Encoded word is: {encrypt(text, shift_num)}')
                else:
                    print(f'Decoded word is: {encrypt(text, shift_num * REVERSE_SHIFT)}')
                in_progress = progress_check()
            else:
                print('Your instruction is not clear. Try again.')
        except ValueError:
            print('Invalid shift number. Please enter a valid integer.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
    main()
