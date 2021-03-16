from square_and_multiply import fast_exp

def decrypt(cipher_pairs, p, g, d):
    plaintext = ''
    for i in range(len(cipher_pairs)):
        c_1, c_2 = cipher_pairs[i]
        P = fast_exp(c_1, p-1-d, p)
        P = P * (c_2 % p)
        P = P % p
        plaintext += chr(P)
    return plaintext
