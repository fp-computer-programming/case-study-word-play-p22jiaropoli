# Author JRI 3/25/22

words= open("words.txt") # opens file
word = words.readlines() 

def uses_only(word, letters): # function to check if the word meets the criteria
    letters = list(letters)
    list2 = list(word)
    for value in letters:
        if value not in list2:
            return False
    return True

y = 0 # starting counter
input = input("Please enter the letters that can be used ") # user input for acceptable letters

for value2 in word: # for loop  and function to check each character in each word
    value2 = value2.strip()
    if uses_only(value2, input) == True:
        y += 1

print("{0} words use only those letters.".format(y)) 

words.close() # close file