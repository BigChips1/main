# while True:
#     print('Please type your name')
#     name = input()
#     if name in ['Ad', 'Bd']:
#         break
# print('Thank you')

import time
from colorama import Fore
class Calculator:
    def sum(self,*args):
        result = 0
        for num in args:
            result += num
        return result

    def sub(self,num1,num2):
        return num1 - num2

    def multi(self,num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        return num1/num2

    def power(self,num1,num2):
        return num1**num2

    def takeInput(self):
        num1 = int(input(Fore.GREEN + "enter first num = "))
        num2 = int(input(Fore.GREEN + "enter second num = "))
        return (num1,num2)
        
#taking decision of the user
calcy = Calculator()
decision = 0
while decision != 5:
    try:
        print( Fore.YELLOW +"""select from below option \n 1)Addition of 2 numbers \n 2)Subtraction of 2 number \n 3)Multiplication of 2 number \n 4)Division of two numbers \n 5)To exit \n """)
        decision = int(input("Please enter your input:"))
        if decision > 5 or decision < 0:
            print(f"{decision} is invalid.")
            time.sleep(3)
        if decision == 1:
            num1,num2 = calcy.takeInput()
            print(Fore.BLUE + str(calcy.sum(num1,num2)))
        if decision == 2:
            num1,num2 = calcy.takeInput()
            print(Fore.BLUE + str(calcy.sub(num1,num2)))
        if decision == 3:
            num1,num2 = calcy.takeInput()
            print(Fore.BLUE + str(calcy.multi(num1,num2)))
        if decision == 4:
            num1,num2 = calcy.takeInput()
            print(Fore.BLUE + str(calcy.div(num1,num2)))
    except Exception as e:
        print( Fore.RED + e.__str__())
        time.sleep(3)


print("Thank you for using")

