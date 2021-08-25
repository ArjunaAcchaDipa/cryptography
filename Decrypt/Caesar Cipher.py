# The ciphertext variable is used to get the sentence that will be decrypted
ciphertext = "Mjqqt ymjwj snhj yt rjjy Dtz :I"
key = 5 # You can change this as you wish

# The listchar variable is used to compare whether the character to be decrypted can be decrypted or not
listchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# The result variable is used to get the sentence that will be decrypted
result = ""

# For loops used to loop through every character that is inputted in ciphertext
for character in ciphertext:
    # If the character is in the listchar variable then the character will be decrypted
    if character in listchar:
        # find the index of the character to be summed later
        index = listchar.find(character)
        # The index will be modded by lengthchar, so the index won't be out of range
        index = (index - key) % len(listchar)
        # memasukkan karakter yang baru ke dalam variabel result
        result += listchar[index]
    else:
        # If the character is not in listchar variable, it won't be decrypted and put
        # in variable result immediately
        result += character

print (result)