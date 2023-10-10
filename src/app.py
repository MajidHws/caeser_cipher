LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# TEST_TEXT = 'KRPH'
TEST_TEXT = 'GNDO DO L ODEFYK KRLEFYK CA L HDFNKIGKRG. XKYY BCWK ZCS WCX MWCX GNLG OCYJDWQ HNLYYKWQKO XDYY QDJK ZCS KRGIL OHCIK LO OCCW LO ZCS FCOG ZCSI OCYSGDCW KRFYLDWDWQ NCX ZCS BDB DG'
CHARS = ' .!'
def get_letter_position(text):
    position = LETTERS.rfind(text)
    # print(f'letter: {text}, posiiton: {position}')
    return position if position != -1 else text


def convert_letters_to_positions(text, shift):
    new_text = ''
   
    for i in range(len(text)):
        position = get_letter_position(text[i])
        is_position_int = isinstance(position, int)
        if is_position_int:
            new_position = position+shift
            shifting_value = new_position if new_position <= len(LETTERS) else new_position - len(LETTERS)

            # new_position = position-shift
            # shifting_value = new_position if new_position <= len(LETTERS) else len(LETTERS) - new_position

            # print(f'shifting_value: {shifting_value}')
            new_text += str(shifting_value)+' '
        else:
            new_text += position
    
    return new_text

def convert_positions_to_letters(text):
    new_text = ''

    for i in range(len(text)):

        position = text[i]

        if position not in CHARS:
            new_text += LETTERS[int(position)-1]
        else:
            new_text += " "

    return new_text


def decrypt(text, shift):
    return convert_letters_to_positions(text, shift)

def main():
    for i in range(len(LETTERS)):
        text = decrypt(TEST_TEXT, shift=i+1)
        # print(f'positions: {text}')
        new_value = convert_positions_to_letters(text.split(' '))
        print(f'{i+1}. sentence: {new_value}')


if __name__ == '__main__':
    main()