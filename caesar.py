def alphabet_position(letter):
    if letter == letter.lower():
        return ord(letter) - 97
    elif letter == letter.upper():
        return ord(letter) -65



def rotate_character(char,rot):
    if char.isalpha():
        if char == char.lower():
            return chr((alphabet_position(char)+ rot) % 26 + 97)
        else:
            if char == char.upper():
                return chr((alphabet_position(char) + rot) % 26 + 65)
    else:
        return char



def encrypt(text,rot):
    encryptedMsg = ""
    for char in text:
        encryptedMsg = encryptedMsg + rotate_character(char,int(rot))
    return encryptedMsg
