import string
import sys

sentence = input("Enter a sentence: ")
separaters = [",",";",":"]
terms = [".","?","!"]
all_possible = [".","?","!", ",",";",":"]
nums = ["1","2","3","4","5","6","7","8","9","0"]
len = len(sentence)
#print(len)

x = 1
prev = ""
for elem in sentence:
    #print("Element: ", elem)
    #print("Previous:", prev)
    #print("X: ", x)
    if x == 1:
        if elem.islower():
            print("Sentence must start with an uppercase letter")
            sys.exit()
    if elem.isupper():
        if x == 1:
            #print("First character is uppercase! Passing first check")
            pass
        else:
            print("Too many uppercases")
            sys.exit()

    if elem in nums:
        print("No Numbers")
        sys.exit()
    elif elem.isalpha():
        #print("Alpha")
        pass
    elif elem.isspace():
        #print("Space")
        pass
    elif elem not in all_possible:
        print("Invalid character")
        sys.exit()
    if prev.isspace():
        if not elem.isalpha():
            print("No double spaces allowed")
            sys.exit()
    

    if x == len:
        if prev.isalpha():
            #print(prev)
            if elem in terms:
                print("Sentence is valid")
            else:
                print("Sentence must end in a terminating mark")
                sys.exit()
        else:
            print("Terminating mark must follow a word")
            sys.exit()

    prev=elem
    x += 1
