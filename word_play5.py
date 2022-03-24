# Charlie CCG 3/24/2022

words = open("words.txt") # open file and set variable
word = words.readlines()

def is_abecedarian(w): # make list for word and set a count variable
    wlist = list(w)
    count = 1
    while count < len(w): # while loop to make sure word is aplhabetical
        if not wlist[count] >= wlist[count-1]:
            return False
        count += 1
    return True

count2 = 0 # set second count variable to count number of alphabetical words

for value in word: # for loop to count and use function
    value = value.strip()
    if is_abecedarian(value) == True:
        count2 += 1

print("{0} words are in alphabetical order.".format(count2)) # output statement

words.close()
