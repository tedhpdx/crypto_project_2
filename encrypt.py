import random
from square_and_multiply import fast_exp


def encrypt(p, g, e_2, plaintext):
    die = random.SystemRandom()
    block_list = []
    for letter in plaintext:
        number = ord(letter)
        block_list.append(number)

    cipher_pairs = []
    for number in block_list:
        r = die.randrange(0, p-1)
        c_1 = fast_exp(g, r, p)
        c_2 = fast_exp(e_2, r, p)
        c_2 *= number
        cipher_pairs.append((c_1, c_2))
    return cipher_pairs

