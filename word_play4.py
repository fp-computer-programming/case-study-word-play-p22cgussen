# Charlie CCG 3/24/2022

words = open("words.txt") # open file
word = words.readlines() # read file

def uses_only(word, letters): # function with  for loop and if statement to check if it meets criteria
    letters = list(letters)
    wlist = list(word)
    for value in letters:
        if value not in wlist:
            return False
    return True

count = 0 # variable to count for the output statement
input = input("Enter the only letters that can be used: ") # user input

for value2 in word: # for loop  and function to check each character in each word
    value2 = value2.strip()
    if uses_only(value2, input) == True:
        count += 1

print("{0} words use only the given letters.".format(count)) # output statement

words.close()
