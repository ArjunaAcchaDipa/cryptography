import detectEnglish

def gcd(a, b):
    # Return the Greatest Common Divisor of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def affineCipher(symbol, ciphertext):
    for key in range (len(symbol) ** 2):
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

        for character in ciphertext:
            if character in symbol:
                # Decrypt the symbol.
                symbolIndex = symbol.find(character)
                plaintext += symbol[(symbolIndex - keyB) * modInverse % len(symbol)]
            else:
                # Append the symbol without decrypting.
                plaintext += character

        if detectEnglish.isEnglish(plaintext):
                # waiting for input from the user, is the result of the plaintext correct or not?
                # if it is correct, the user can input Y or y which will stop the bruteforce loop
                print("Is this right?\n", plaintext)
                print("Press Y or y to end the brute-force")
                response = input("> ")
                if response.lower() == "y":
                    # return the correct result
                    return (plaintext)
                else:
                    # continue brute-force
                    continue

def main():
    affineCiphertext = input("Affine ciphertext: ")
    affineSymbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    affinePlaintext = affineCipher(affineSymbol, affineCiphertext)

    if affinePlaintext is None:
        print("Failed to hack!")
    else:
        print("plaintext: {}".format(affinePlaintext))

if __name__ == "__main__":
    main()