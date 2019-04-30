import string

def rot13(message):
    return message.encode('rot13')
    alphabets = [string.ascii_lowercase, string.ascii_uppercase]
    result = ''
    OFFSET = 13
    ALPHABET_LENGHT = len(alphabets[0])

    for char in message:
        is_added = False
        for alphabet in alphabets:
            pos = alphabet.find(char)
            if pos != -1:
                result += alphabet[(pos + OFFSET) % ALPHABET_LENGHT]
                is_added = True
        if not is_added:
            result += char

    return result

print (rot13('EBG13 rknzcyr.'))
