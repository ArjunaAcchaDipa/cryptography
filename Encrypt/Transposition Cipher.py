# The plaintext variable is used to get the sentence that will be encrypted
plaintext = input("The sentence you want to change: ")

# Input key will be a string, because we input it as a string.
# So when the key needed to be if the key will be used for calculations,
# then the key needs to be converted into an integer
key = input("Input the key: ")

# This part of the code are used to determine how many row that will be used.
# If the length of the plaintext mod key is more than 0, that means the length of the plaintext
# can not be divided by the key. That is why we need to add 1 more row.
if (len(plaintext)%int(key) > 0):
    row = len(plaintext)//int(key) + 1
else:
    row = len(plaintext)//int(key)

# The result variable is used to store the result of the encryption
result = ""

# This double loops used to get the character by the row. Variable "i" is used to represent the column
# and variable j is used to represent the row.
for i in range (int(key)):
    # To get every index in the row, we need to increment the index of j by the key
    for j in range (0, len(plaintext), int(key)):
        if (i+j > len(plaintext)-1):
            break
        else:
            result += plaintext[i+j]

print (result)