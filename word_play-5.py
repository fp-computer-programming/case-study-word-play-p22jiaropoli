# Author JRI 3/25/22

words = open("words.txt") # open file and set variable
x = words.readlines()




def is_abecedarian(y): # function that makes list
    list2 = list(y)
    count1 = 1
    while count1 < len(y): # while loop to make sure word is aplhabetical
        if not list2[count1] >= list2[count1-1]:
            return False
        count1 += 1
    return True


count2 = 0 #second count variable

for z in x: # for loop that repeats function
    z = z.strip()
    if is_abecedarian(z) == True:
        count2 += 1

print("{0} words are in alphabetical order.".format(count2)) # print statement for the number of words in alphabetical order

words.close() # closes words file