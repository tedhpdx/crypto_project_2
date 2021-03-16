from key_gen import key_gen
from encrypt import encrypt
from decrypt import decrypt

if __name__ == "__main__":
    d = 1007
    choice = None
    print("Welcome to the asymmetric crypto project!")
    while choice is not '4':
        print("Please choose an option")
        print("1: Key generation")
        print("2: Encryption")
        print("3: Decryption")
        print("4: Exit")
        choice = input("Please enter your choice: ")
        if choice is '1':
            print("You have chosen key generation")
            seed = input("Please enter a number: ")
            d = 1007
            p, g, e_2 = key_gen(seed, d)
            pubkey = str(p) + ' ' + str(g) + ' ' + str(e_2)
            f = open("pubkey.txt", 'w')
            f.write(pubkey)
            f.close()
            prikey = str(p) + ' ' + str(g) + ' ' + str(d)
            f = open('prikey.txt', 'w')
            f.write(prikey)
            f.close()
            choice = None
            continue
        elif choice is '2':
            print("You have chosen encryption, the program will now open ptext.txt and pubkey.txt then output ciphertext pairs in file ctext.txt")
            plaintext = ''
            f = open('ptext.txt', encoding='utf8')
            for line in f:
                plaintext += line
            f.close()
            f = open('pubkey.txt', 'r')
            pubkey = f.readline()
            split_pub = pubkey.split(' ')
            p = int(split_pub[0])
            g = int(split_pub[1])
            e_2 = int(split_pub[2])
            cipher_pairs = encrypt(p, g, e_2, plaintext)
            print(cipher_pairs)
            with open ('ctext.txt', 'w') as ctext:
                for pair in cipher_pairs:
                    string = str(pair[0]) + ' ' + str(pair[1]) + '\n'
                    ctext.write(string)
            choice = None
            continue
        elif choice is '3':
            print("You have chosen decryption, the program will now open ctext.txt and prikey.txt and output dtext.txt")
            cipher_pairs = []
            with open ('ctext.txt', 'r') as ctext:
                for line in ctext:
                    line = line.rstrip()
                    pair_list = line.split(' ')
                    for i in range(len(pair_list)):
                        pair_list[i] = int(pair_list[i])
                    cipher_pairs.append(tuple(pair_list))
                    pair_list = []
            f = open('prikey.txt', 'r')
            prikey = f.readline()
            prikey_list = prikey.split(' ')
            p = int(prikey_list[0])
            g = int(prikey_list[1])
            d = int(prikey_list[2])
            plaintext = decrypt(cipher_pairs, p, g, d)
            print(plaintext)
            f = open('dtext.txt', 'w')
            f.write(plaintext)
            f.close()
            choice = None
            continue
        elif choice is '4':
            print("Exiting, thank you for using my program!")
            continue
        else:
            "input not recognized please try again"
