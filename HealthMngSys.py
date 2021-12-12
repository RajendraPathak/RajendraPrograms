"""This the program for daily intake and exercise analysis"""

import datetime

def gettime():  # function to get Time details
    return datetime.datetime.now()

def logthedata(i):  # function to take details
    if i == 1:
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            value = input("type here \n")
            with open("Raj_food.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        elif user_input3 == 2:
            value = input("type here \n")
            with open("Raj_exercise.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        else:
            print("Please enter correct value")
    elif i == 2:
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            value = input("type here \n")
            with open("Rucha_food.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        elif user_input3 == 2:
            value = input("type here \n")
            with open("Rucha_exercise.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        else:
            print("Please enter correct value")
    elif i == 3:
        n2 = input("Enter name")
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            value = input("type here \n")
            with open(n2 + "_food.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        elif user_input3 == 2:
            value = input("type here \n")
            with open(n2 + "_exercise.txt", 'a') as tx:
                tx.write(str([str(gettime())]) + ":" + value + "\n")
        else:
            print("Please enter correct value")
    else:
        print("Please enter correct value")


def retreivedata(i):  # function to take details
    if i == 1:
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            with open("Raj_food.txt") as tx:
                for k in tx:
                    print(k, end="")
        elif user_input3 == 2:
            with open("Raj_exercise.txt") as tx:
                for k in tx:
                    print(k, end="")
        else:
            print("Please enter correct value")
    elif i == 2:
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            with open("Rucha_food.txt") as tx:
                for k in tx:
                    print(k, end="")
        elif user_input3 == 2:
            with open("Rucha_exercise.txt") as tx:
                for k in tx:
                    print(k, end="")
        else:
            print("Please enter correct value")
    elif i == 3:
        n2 = input("Enter name")
        user_input3 = int(input("Enter 1 for food 2 for exercise"))
        if user_input3 == 1:
            with open(n2 + "_food.txt") as tx:
                for k in tx:
                    print(k, end="")
        elif user_input3 == 2:
            value = input("type here \n")
            with open(n2 + "_exercise.txt") as tx:
                for k in tx:
                    print(k, end="")
        else:
            print("Please enter correct value")
    else:
        print("Please enter correct value")

print("Welcome to Health management System")
t = 1
while t == 1:
    user_input1 = int(input("Select 1 for log or 2 for retrieve "))
    if user_input1 == 1:
        user_input2 = int(input("Select 1 for Rajendra, 2 for Rucha, 3 for others"))
        logthedata(user_input2)
    elif user_input1 == 2:
        user_input2 = int(input("Select 1 for Rajendra, 2 for Rucha, 3 for others"))
        retreivedata(user_input2)
    else :
        print("Enter valid value")
    try:
        t = int(input("Do you want to continue? \n 1 for continue else for exit"))
    except Exception as e:
        t = 0
print("Thank you")