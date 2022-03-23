# Charlie CCG 3/24/2022

# open files and two variables for lines
wordfile = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/words.txt")
noefile = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/words_without_e.txt", "r+")
line = wordfile.readline().strip()
eline = noefile.readline().strip()

noe = 0 # set variables for the percentage
total = 0
def no_e(word): # function to filter out "e"
    if "e" not in word:
        noefile.write(word)
        return True

no_e(line) # call function

for line in wordfile: # count number of words
    total += 1
for eline in noefile: # count number of words without e
    noe += 1

percentage = (noe / total) * 100 # calculate percentage and print
print("{0}% of words do not contain e.".format((percentage)))
