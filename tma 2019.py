from array import array
arr = []
x = 0
y = 0
user_account_balance = 0
user_salary_credit = 0
user_transaction = 0
i = 0


def checkNumber(isNumber):
    try:
        isNumber = float(isNumber)
        arr.append(isNumber)
        return True
    except:
        print("Please try again")
        return False

class User:
    def __init__(self, arr):
        self.user_account_balance = arr[0]
        self.user_salary_credit = arr[1]
        self.user_transaction = arr[2]

    def checkInterest(self):
        if (self.user_account_balance < 50000):
            if (self.user_transaction < 2):
                global x
                x = 0
            else:
                x = 1
        else:
            x = 2

        if(self.user_salary_credit < 2000):
            global y
            y = 0
        elif (self.user_salary_credit >= 2000 and self.user_salary_credit < 2500):
            y = 1
        elif (self.user_salary_credit >= 2500 and self.user_salary_credit < 5000):
            y = 2
        elif (self.user_salary_credit >= 5000 and self.user_salary_credit < 15000):
            y = 3
        elif (self.user_salary_credit >= 15000 and self.user_salary_credit < 30000):
            y = 4
        elif (user_salary_credit >= 30000):
            y = 5

    


# def user(arr):
#     global user_account_balance
#     global user_salary_credit
#     global user_salary_credit
#     user_account_balance = arr[0]
#     user_salary_credit = arr[1]
#     user_transaction = arr[2]

#     checkInterest(user_account_balance, user_salary_credit, user_transaction)




number = False
while (number == False):
    account_balance = input("Enter your account balance: ")
    isNumber = account_balance
    if (checkNumber(isNumber) == True):
        number = True

number = False
while (number == False):
    salary_credit = input("Enter your salary credit: ")
    isNumber = salary_credit
    if (checkNumber(isNumber) == True):
        number = True

number = False
while (number == False):
    number_of_transaction = input("Enter your number of transactions: ")
    isNumber = number_of_transaction
    if (checkNumber(isNumber) == True):
        number = True

user = User(arr)
user.checkInterest()

template = [[0.05, 0.05, 0.05],
            [1.55, 1.80, 2.00],
            [1.85, 2.00, 2.20],
            [1.90, 2.20, 2.40],
            [2.00, 2.30, 2.50],
            [2.08, 3.50, 3.80]]

print(template[y][x],"% p.a")
interest = (template[y][x])/100
monthly_interest = interest/12

while (i < 12):
    interest_earned = user.user_account_balance * monthly_interest
    print("Interest earned for ", i+1, "month is : ", round(interest_earned,2))
    user.user_account_balance = interest_earned + user.user_account_balance
    i = i + 1

print ("Total earning for end of the year is : " , round(user.user_account_balance,2))
