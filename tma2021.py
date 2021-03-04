# Q2a
def getPartsInCode(productCode):
    string = 'ABCDEFGHIJKL'
    a = ''
    x = ''
    for i in productCode:
        count = productCode.count(i)
        if a != i:
            x += (str(count) + i + ' ')
        a = i
    print(x)
    return x


x = getPartsInCode('ABBBG')

# Q2b


def fullStock():
    startLevel = 2
    reorderPoint = 20
    partIds = 'ABCDEFGHIJKL'
    # for i in range(12):
    # t.append(startLevel)
    stockLevel = []
    for i in range(len(partIds)):
        stockLevel.append(startLevel)

    print(stockLevel)
    return stockLevel


# # Q2c
# option = int(input('''Menu
# 1. Add product code
# 2. List inventory
# 3. Update inventory
# 4. Make product
# 5. Get summarised data
# 0. Exit
# Enter choice: '''))

# while option != 0:
#     if 1 <= option <= 5:
#         print('Option', option,'is selected')
#     else:
#         print('Invalid')
#     option = int(input('''Menu
# 1. Add product code
# 2. List inventory
# 3. Update inventory
# 4. Make product
# 5. Get summarised data
# 0. Exit
# Enter choice: '''))

# print('End of program')


def addProductCode(existingProductCode):
    productList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    newproductcode = sorted(str(input('Enter new product code: ')).upper())
    print(newproductcode)
    add = False
    count = 1
    for i in newproductcode:
        if len(newproductcode) < 3 or i not in productList:
            print('The product code is invalid')
            break
        elif len(newproductcode) == count:
            add = True
            break
        else:
            count += 1
    a = ''
    for i in newproductcode:
        a += i
    if add == True:
        if a not in existingProductCode:
            existingProductCode.append(a)
        else:
            print('The product code already exists')


def listProductCode(stockLevel):
    # partIds= 'ABCDEFGHIJKL'
    # count = len(partIds)
    print("Part \t Stock \t Level ")
    for letter in range(len(partIds)):
        if int(stockLevel[letter]) < 20:
            indicate = "***"
        else:
            indicate = ""
        print(f"{partIds[letter]} \t {stockLevel[letter]} \t {indicate}")
    print("Lengend: *** stock level at or lower than reorder point 20")


def writeFile(content):
    f = open(r"C:\Users\Valente\Desktop\Python-Training\transcations.txt", "a")
    f.write(content)
    print(content)
    f.close()

def readFile():
    f = open(r"C:\Users\Valente\Desktop\Python-Training\transcations.txt", "r")
    summaryContent = f.readlines()
    f.close()
    return summaryContent

def checkQTY(qty):
    if qty <= 0:
        return False
    else:
        return True


def updateProductCode(stockLevel):
    while True:
        partIdentifier = input(
            "Enter part identifier or <Enter> to end: ").upper()
        print(partIdentifier)
        if partIdentifier is "":
            print("end")
            break
        elif partIdentifier not in partIds:
            print("The part identifier is invalid")
        else:
            index = partIds.index(partIdentifier)
            print(index, stockLevel[index])
            print(
                f"Current stock level for {partIdentifier} = {stockLevel[index]}")
            qty = int(input("Enter Qty to add : "))
            valid = checkQTY(qty)
            if valid == False:
                print("The QTY is invalid")
            elif valid == True:
                total = int(stockLevel[index]) + qty
                print(f"updated stock level for {partIdentifier} = {total}")
                content = f"restock {partIdentifier} {qty} \n"
                writeFile(content)


def checkStockLevel(partsUsedList, stockLevel):
    partsUsedListLen = len(partsUsedList)
    count = 0
    for parts in partsUsedList:
        partsRequired = parts[-1]
        partsQTYRequired = parts[0:-1]
        index = partIds.index(partsRequired)
        if int(stockLevel[index]) >= int(partsQTYRequired):
            count += 1
        else: break
    
    if count < partsUsedListLen:
        return False
    else : return True


def makeProduct(existingProductCode, stockLevel):
    makeProductCode = sorted(str(input("Enter product code: ")).upper())
    makeProductCode1 = ""
    for i in makeProductCode:
        makeProductCode1 += i

    if makeProductCode1 not in existingProductCode:
        print(f"Invalid product code {makeProductCode1}")
    else:
        makeQTY = int(input("Enter QTY to make: "))
        valid = checkQTY(makeQTY)
        if valid == False:
            print(f"Invalid QTY {makeQTY}")
        else:

            partsUsed = getPartsInCode(makeProductCode1)
            partsUsedList = partsUsed.strip().split(" ")
            count = 0
            while count < makeQTY:
                if checkStockLevel(partsUsedList, stockLevel) == True:
                    for parts in partsUsedList:
                        partsRequired = parts[-1]
                        partsQTYRequired = parts[0:-1]
                        index = partIds.index(partsRequired)
                        stockLevel[index] = int(stockLevel[index]) - (int(partsQTYRequired))
                else:
                    break
                        
                print(stockLevel)
                count += 1

            if count == makeQTY:
                content=f"make {makeProductCode1} {makeQTY}\n"
                print(f"{makeQTY} product {makeProductCode1} successfully made")
                writeFile(content)
            elif count == 0:
                content = f"outstanding {makeProductCode1} {makeQTY-count}"
                writeFile(content)
                print (f"{makeQTY-count} oustanding")
            else:
                content = f'''make {makeProductCode1} {count}
outstanding {makeProductCode1} {makeQTY-count}\n'''

                print(f"{count} product {makeProductCode1} made at the current inventory level.")
                print(f"{makeQTY-count} oustanding")
                writeFile(content)

def getSummary():
    readData = int(input("0-restock, 1-make, 2-outstanding. Enter choice : "))
    if readData == 0:
        action = "restock"
    elif readData == 1:
        action = "make"
    elif readData == 2:
        action = "outstanding"
    summaryContent = readFile()
    print(summaryContent)
    print(f"summarised data for {action.upper()}")
    for content in summaryContent:
        line = content.strip().split(" ")
        if line[0] == action:
            print(f"{line[1]} \t {line[2]}")


partIds = 'ABCDEFGHIJKL'
existingProductCode = ['ABCD']
stockLevel = fullStock()


while True:
    option = int(input('''Menu
    1. Add product code
    2. List inventory
    3. Update inventory
    4. Make product
    5. Get summarised data
    0. Exit
    Enter choice: '''))

    if option == 1:
        # print("1")
        addProductCode(existingProductCode)
        print(existingProductCode)
    elif option == 2:
        listProductCode(stockLevel)
    elif option == 3:
        updateProductCode(stockLevel)
    elif option == 4:
        makeProduct(existingProductCode, stockLevel)
    elif option == 5:
        getSummary()
    elif option == 0:
        break

print('End of program')
