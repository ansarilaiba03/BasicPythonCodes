'''
bank manager project
1. bank account
2. deposit money
3. withdraw money
4. details
5. update details 
6. detele account
'''
import json
import random
import string
from pathlib import Path

class Bank:

    database = 'OOPS/data.json'
    data = [] #dummy database
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
                    
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def CreateBankAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter you pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("Sorry, your account cannot be created")
        else:
            print("Your account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account no.")

            Bank.data.append(info)
            Bank.__update()


    def DepositeMoney(self):
        accnum = input("Enter you account no.: ")
        pin = int(input("enter you pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry, no data found")

        else:
            amount = int(input("enter the ammount you want to deposite: "))
            if amount > 10000 and amount<0:
                print("you cannot deposit greater then 10000 and less than 0")

            else:
                #print(f"userdata: {userdata}")
                userdata[0]['balance'] += amount #[0] because it is a list then inside a list there is a dictionary so to access the dictiorany you need to access the 0th index with is the dictionaary, open data.json and see [{}]
                Bank.__update()
                print("Amount updated")
        

    def WithdrawMoney(self):
        accnum = input("enter your account no.: ")
        pin = int(input("enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("Sorry, not found")

        else:
            amount = int(input("enter the amount you want to deposit: "))
            if userdata[0]['balance'] < amount:
                print("sorry, you don't have that much amount")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("amount withdrawn")

    def Details(self):
        accnum = input("Enter you account no.: ")
        pin = int(input("enter you pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry, cant print you details")
        else:
            print("your details are: \n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
        

    def UpdateDetails(self):
        accnum = input("enter you account no.: ")
        pin = int(input("enter you pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("No such account exists")
        else:
            print("you cannot change the age, account nummber, balance")
            print("fill the details for change or leave it empty if no chnage")

            newdata = {
                'name' : input("enter new name or press enter: "),
                'email' : input('enter new email or press enter: '),
                'pin' : input('enter new pin or press enter: ')
            }

            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']
            if newdata['email'] == "":
                newdata['email'] = userdata[0]['email']
            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] =userdata[0]['age']
            newdata['accountNo.'] =userdata[0]['accountNo.']
            newdata['balance'] =userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            Bank.__update()
            print("updated")
                        

    def DeleteAccount(self):
        accnum = input("enter yout account number: ")
        pin = int(input("enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False :
            print("does not exist")
        else:
            check = input("press y or yes and n for no")
            if check == 'n' or check == "N":
                pass
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("deleted")
                Bank.__update()
                

obj = Bank()

print("1.create bank account\n2.deposite money\n3.withdraw money\n4.detials\n5.update details\n6.delete account\n")
choice = int(input("Enter your choice: "))

if choice == 1:
    obj.CreateBankAccount()

elif choice == 2:
    obj.DepositeMoney()

elif choice == 3:
    obj.WithdrawMoney()

elif choice == 4:
    obj.Details()

elif choice == 5:
    obj.UpdateDetails()

elif choice == 6:
    obj.DeleteAccount()

else:
    print("Incorrect choice")