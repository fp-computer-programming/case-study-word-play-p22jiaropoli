# Author JRI 3/25/22

words = open("/Users/p22jiaropoli/Desktop/Labs/case-study-word-play-p22jiaropoli/words.txt") # opening file
line = words.readline().strip()


def avoid(x): #defining function
    count = 0
    for line in words: 
        if x not in line:
            count += 1
    return count
            

forbiddenletters = input("Enter the forbidden letters: ") # input statement for user

print("{0} words found without those letters.".format(avoid(forbiddenletters))) # print statement of number of words found

words.close() # closes file