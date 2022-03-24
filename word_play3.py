# Charlie CCG 3/24/2022

words = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/words.txt")
line = words.readline().strip()

def avoid(text): # define function
    count = 0
    for line in words: # for loop to count each word that meets criteria
        if text not in line:
            count += 1
    return count
            

forbidden = input("Enter the charaters to exclude: ") # input statement for user

print("{0} words found.".format(avoid(forbidden))) # print statement and call function

words.close()