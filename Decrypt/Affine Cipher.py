import enchant
from threading import Thread

def checkEnglish(plaintext, plaintextWord):
    englishWords = enchant.Dict("en_US")

    englishCheck = True

    if not englishWords.check(plaintextWord):
        englishCheck = False
    
    if (englishCheck):
        print (plaintext)

def gcd(a, b):
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def affineCipher(symbol, ciphertext):
    for key in range (len(symbol) ** 3):
        keyA = key // len(symbol)
        keyB = key % len(symbol)

        # Ensure that keyA and the total character of the symbol are co-prime.
        if (gcd(keyA, len(symbol))!=1):
            continue

        # Looking for mod inverse of keyA.
        u1, u2, u3 = 1, 0, keyA
        v1, v2, v3 = 0, 1, len(symbol)
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        modInverse = u1 % len(symbol)

        plaintext = ""

        for i in ciphertext:
            if i in symbol:
                # Decrypt Affine Cipher has the formula (index_dari_character - keyB) * mod_invers_keyA % total_character_symbol
                # The result will be stored in the plaintext variable. Where the stored character comes from the symbol variable,
                # in the formula index above
                plaintext += symbol[(symbol.find(i) - keyB) * modInverse % len(symbol)]
            else:
                plaintext += i

        for plaintextWord in plaintext:
            thread = Thread(target=checkEnglish, args=(plaintext, plaintextWord,))
            thread.start()
            thread.join()

def main():
    affineCiphertext = input("Affine ciphertext: ")
    affineSymbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    affinePlaintext = affineCipher(affineSymbol, affineCiphertext)

    # print("Plaintext: {}".format(affinePlaintext))

if __name__ == "__main__":
    main()