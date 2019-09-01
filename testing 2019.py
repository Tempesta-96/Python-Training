import array
# my_age = 35
# my_height = 74
# my_weight = 180
# my_eyes = "Blue"
# my_hair = "Brown"


# print (f"He's {my_height} ")
# total =  my_age + my_height + my_weight

# print (f"my {total}")

# hiliarious = False
# print ("isnt that joke funny {}".format(hiliarious))
# print (" {}".format('snow'))

# print ("jan \nFeb")
# print ("i am 6\'2 \" tall.")
# print ("i am 6\'2 \\\" tall")

# print ("\\")
# print ('don\'t')
# print ("'he said, \'hi\' ")
# print ("its fun", "Dont you think")
# print ("\\n is the newline char")
# print ("this \n is the new line")

# print (float('-9.9'))
# print (int('9.9'))
# weight = input("weight?")

# try:
#     float(weight)
# except:
#     print ("Error")
# finally:
#     print ("finally")

choosenWord = input("Enter your word : ")
dictionary = []
gotWord = True
f = open("C:\\Users\\Valente\\Desktop\\Python-Training\\history.txt", "r")
for x in f:
    word = x.split(":")
    dictionary.append(word)
    # print(word)
f.close()

i = 0
# dictonary_length = len(dictionary)
while (i < len(dictionary)):
    # print(dictionary[i][0])
    if (dictionary[i][0] == choosenWord.lower()):
        print(dictionary[i][1], end='')
        addAgain = input("want to add another example?")
        if(addAgain.lower() == "yes"):
            addExample = input("Add a new example : ")
        elif(addAgain.lower() == "no"):
            break
        break
    i += 1

while(i == len(dictionary)):
    print("no such word")
    f = open("C:\\Users\\Valente\\Desktop\\Python-Training\\history.txt", "a")
    addWord = input("Add a new word : ")
    addExample = input("Add a new example : ")
    newline = "\n"+addWord + ":"+addExample
    dictionary.append(newline)
    f.write(newline)
    f.close()
    print("Added suceess")
    i = 0
