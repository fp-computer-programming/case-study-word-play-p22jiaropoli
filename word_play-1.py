# Author JRI 3/25/22


x = open("/Users/p22jiaropoli/Desktop/Labs/case-study-word-play-p22jiaropoli/words.txt","r") # opening text file

greater_than_20 = open("/Users/p22jiaropoli/Desktop/Labs/case-study-word-play-p22jiaropoli/greater_than_20.txt","a") # opening new file


while True: 
    y = x.readline()
    if len(y) > 19: # writes word on seperate file while the length of the word is 20 or greater
        greater_than_20.write(y)
        continue
    if len(y) == 0: # breaks if the length of the word is 0
        break

x.close() #closes both files
greater_than_20.close()