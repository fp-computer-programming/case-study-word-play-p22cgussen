# Charlie CCG 3/24/2022

wordfile = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/words.txt")
line = wordfile.readline().strip()

# defined the function
def avoid(text):
    counter = 0
    # checks if the line meets the requirements
    for line in wordfile:
        if text not in line:
            counter += 1
    return counter
            

forbidden = input('Please enter the string to exclude: ')

# calling the function within the print statement for a value
print('{0} words found.'.format(avoid(forbidden)))
