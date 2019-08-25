import array

dictionary = []
i = 0
path = "C:\\Users\\Valente\\Desktop\\Python-Training\\history.txt"
temp = ""


def checkWord(choosenWord):
    global i
    global dictionary
    global path
    global temp
    f = History.readFile(path)
    while (i < len(dictionary)):
        if (dictionary[i][0] == choosenWord.lower()):
            temp = dictionary[i][1]
            f.close()
            return True
        else:
            i += 1
            while(i == len(dictionary)):
                f.close()
                return False


def addExample(newExample, choosenWord):
    global i
    i = 0
    global temp
    temp = ""
    f = History.writeFile(path)
    while (i < len(dictionary)):
        if (dictionary[i][0] == choosenWord.lower()):
            temp = dictionary[i][1].strip()
            dictionary[i][1] = temp+" , "+newExample+"\n"
            combineWord = dictionary[i][0]+":"+dictionary[i][1]
            print(dictionary[i])
            f.write(combineWord)
        else:
            print(dictionary[i])
            j = 0
            while(j < len(dictionary[i])):
                if (j == 0):
                    firstWord = dictionary[i][j]
                elif (j == 1):
                    secondWord = dictionary[i][j]
                j += 1
            combineWord = firstWord+":"+secondWord    
            f.write(combineWord)
    
        i += 1


def newWordExample(addWord, addExample):
    f = History.appendFile(path)
    newline = "\n"+addWord + ":"+addExample
    print(newline)
    # dictionary.append(newline)
    f.write(newline)
    f.close()
    print("Added suceess")


class History:

    global dictionary

    def __init__(self, path):
        self.path = path
        self.f = open(path, "r")

    def closeFile(self, f):
        f.close()
        print("File closing")

    def readFile(self):
        f = open(path, "r")
        print("File opening")
        for x in f:
            word = x.split(":")
            dictionary.append(word)
            # print(word)
        # f.close()
        return f
    
    def writeFile(self):
        f=open(path,"w")
        print ("File opening")
        # for x in f:
        #     word = x.split(":")
        #     dictionary.append(word)
        return f

    def appendFile(self):
        f = open(path, "a")
        return f


choosenWord = input("Enter your word : ")

if (checkWord(choosenWord)) == True:
    print(temp.strip())
    addAgain = input("want to add another example?")
    if(addAgain.lower() == "yes"):
        newExample = input("Add a new example : ")
        addExample(newExample, choosenWord)
    elif(addAgain.lower() == "no"):
        print("ending")
else:
    print("no such word")
    addWord = input("Add a new word : ")
    addExample = input("Add a new example : ")
    newWordExample(addWord, addExample)

