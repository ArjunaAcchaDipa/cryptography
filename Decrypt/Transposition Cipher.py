# Variable below is used to give an example on how this code works. You can change this as you like
ciphertext = "Cenoonommstmme oo snnio. s s c"
key = 8

# If you want the variable to be inputed by user
# # The ciphertext variable is used to get the sentence that will be encrypted
# ciphertext = input("The sentence you want to decrypt: ")

# # Input key will be a string, because we input it as a string.
# # So when the key needed to be if the key will be used for calculations,
# # then the key needs to be converted into an integer
# key = input("Input the key: ")

# To reverse / decrypt the transposition cipher, we need to get the column.
# Just like how we determine the row, we can determine the column by using mod.
# If the length of the ciphertext mod key is more than 0, that means the length of the ciphertext
# can not be divided by the key. That is why we need to add 1 more column.
if (len(ciphertext)%key > 0):
    column = len(ciphertext)//key + 1
else:
    column = len(ciphertext)//key

# If we encrypt the plaintext, there might be some parts that were null.
# That is why we need to count how many null characters that will be needed.
# To count / determine how many null characters needed, we can check how many characters that could be used
# in the table and then subtract that number with total characters in ciphertext.
null = key*column - len(ciphertext)

# This part, we will input the null character into the ciphertext, so when we use the same function to
# get every row, we could reverse the encryption.
for i in range (null):
    skip = (key*column)-(i*column)-1
    ciphertext = ciphertext[:skip] + "\0" + ciphertext[skip:]

result = ""

# This double loops used to get the character by the row. Variable "i" is used to represent the column
# and variable "j" is used to represent the row.
for i in range (column):
    # To get every index in the column in the same row, we need to increment the index of "j" by the key
    for j in range (0, (key*column), column):
        if (i+j >= len(ciphertext)):
            break
        else:
            result += ciphertext[i+j]

print (result)