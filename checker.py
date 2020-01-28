import string
import sys

filepath = './tests.txt'
try:
    fp = open('./tests.txt')
    # do stuff here

    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        sentence = line
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = line.strip()
            length = len(line)
            sentence = line
            
            separaters = [",",";",":"]
            terms = [".","?","!"]
            all_possible = [".","?","!", ",",";",":"]
            nums = ["1","2","3","4","5","6","7","8","9","0"]
            #sentence = input("Enter a sentence: ")]
            #len = len(sentence)
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
                        #sys.exit()
                        break
                if elem.isupper():
                    if x == 1:
                        #print("First character is uppercase! Passing first check")
                        pass
                    else:
                        print("Too many uppercases")
                        #sys.exit()
                        break

                if elem in nums:
                    print("No Numbers")
                    #sys.exit()
                    break
                elif elem.isalpha():
                    #print("Alpha")
                    pass
                elif elem.isspace():
                    #print("Space")
                    pass
                elif elem not in all_possible:
                    print("Invalid character")
                    #sys.exit()
                    break
                if prev.isspace():
                    if not elem.isalpha():
                        print("No double spaces allowed")
                        #sys.exit()
                        break
                

                if x == length:
                    if prev.isalpha():
                        #print(prev)
                        if elem in terms:
                            print("Sentence is valid")
                        else:
                            print("Sentence must end in a terminating mark")
                            #sys.exit()
                            break
                    else:
                        print("Terminating mark must follow a word")
                        #sys.exit()
                        break

                prev=elem
                x += 1
            line = fp.readline()
            cnt += 1
finally:
    fp.close()
