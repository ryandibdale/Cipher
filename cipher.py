tabula_recta = ' abcdefghijklmnopqrstuvwxyz.()!?"£$%^&*"'

def cipher(s, n):
    new_letters = []
    new_indices = []
    new_message = []

    for letter in s.lower():
        new_letters.append(tabula_recta.index(letter))

    for index in new_letters:
        new_indices.append(index + n)

    for index in new_indices:
        new_message.append(tabula_recta[index])

    return ''.join(new_message)

def decipher(s, n):
    new_letters = []
    new_indices = []
    new_message = []

    for letter in s.lower():
        new_letters.append(tabula_recta.index(letter))

    for index in new_letters:
        new_indices.append(index - n)

    for index in new_indices:
        new_message.append(tabula_recta[index])

    return ''.join(new_message)

if __name__ == '__main__':
    cipher()

