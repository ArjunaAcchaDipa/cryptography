# The listchar variable is used to compare whether the character to be encrypted can be encrypted or not
listchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# to count how many characters in variable listchar
lengthchar = len(listchar)

# The plaintext variable is used to get the sentence that will be encrypted
plaintext = input("The sentence you want to change: ")

# Input key will be a string, because we input it as a string.
# So when the key needed to be if the key will be used for calculations,
# then the key needs to be converted into an integer
key = input("Input the key: ")

# The result variable is used to store the result of the encryption
result = ""

# For loops used to loop through every character that is inputted by user
for character in plaintext:
    # If the character is in the listchar variable then the character will be encrypted
    if character in listchar:
        # find the index of the character to be summed later
        index = listchar.find(character)
        # The index will be modded by lengthchar, so the index won't be out of range
        index = (int(key) + index) % lengthchar
        result += listchar[index]
    else:
        # If the character is not in listchar variable, it won't be encrypted and put
        # in variable result immediately
        result += character

print("Caesar cypher result: {}".format(result))