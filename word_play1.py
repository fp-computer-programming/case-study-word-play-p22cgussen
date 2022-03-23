# Charlie CCG 3/24/2022

words = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/words.txt","r")
greater = open("/Users/p22cgussen/Desktop/Labs/case-study-word-play-p22cgussen/greater_than_20.txt","a")
while True:
    line = words.readline()
    if len(line) > 19:
        greater.write(line)
        continue
    if len(line) == 0:
        break

words.close()
greater.close()