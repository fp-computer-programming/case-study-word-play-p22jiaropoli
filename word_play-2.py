# Author JRI 3/25/22

# open files and two variables for lines
word_list = open("/Users/p22jiaropoli/Desktop/Labs/case-study-word-play-p22jiaropoli/words.txt")

no_e_text = open("/Users/p22jiaropoli/Desktop/Labs/case-study-word-play-p22jiaropoli/words_without_e.txt", "r")

line = word_list.readline().strip()
e_line = no_e_text.readline().strip()

x = 0 # variables to use for percentage
total = 0

def no_e(word): # function that finds words with no e
    if "e" not in word:
        no_e.write(word) # writes the word in the no e text file
        return True


no_e(line) # calling function

for line in word_list:
    total += 1
for e_line in no_e: # count number of words without e
    x += 1


percentage = (x / total) * 100 # calculate percentage and print
print("{0}% of words do not contain e.".format((percentage)))



word_list.close() # closes words file