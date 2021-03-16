import random
from miller_rabin import miller_rabin
from square_and_multiply import fast_exp


def key_gen(seed, d):
    random.seed(seed)
    die = random.SystemRandom()

    g = 2
    p = None
    while True:
        q = die.getrandbits(32)
        if q % 12 is 5:
            p = 2*q + 1
            if miller_rabin(p):
                break
    e_2 = fast_exp(g, d, p)
    #write files
    print('key gen:')
    print('public key:')
    print('p = ' + str(p))
    print('g = ' + str(g))
    print('e_2 = ' + str(e_2))
    print('private key:')
    print('p = ' + str(p))
    print('g = ' + str(g))
    print('d = ' + str(d))
    return p, g, e_2
