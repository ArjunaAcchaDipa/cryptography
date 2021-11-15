def affineCipher(symbol, plaintext, keyA, keyB):
    ciphertext = ""
    for i in plaintext:
        # This if is used to check whether the character in the plaintext is also in the symbol. If there is, it will be calculated/encrypted
        # However, if not, then the character will be directly inserted into the result (ciphertext).
        if i in symbol:
            # Affine Cipher has the formula (keyA * index_dari_character + keyB) % total_character_symbol
            # The result will be stored in the ciphertext variable. Where the stored character comes from the symbol variable,
            # from the formula above
            ciphertext += symbol[(keyA * symbol.find(i) + keyB) % len(symbol)]
        else:
            ciphertext += i
    
    return ciphertext

def main():
    # define variables yang akan digunakan untuk Affine Cipher
    affinePlaintext = input("Affine plaintext: ")
    affineKeyA = int(input("Affine key A: "))
    affineKeyB = int(input("Affine key B: "))
    affineSymbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    print(affineCipher(affineSymbol, affinePlaintext, affineKeyA, affineKeyB))

if __name__ == "__main__":
    main()