"""COFFEE MACHINE"""
from machine_data import *

def report():
    print("Our resource: ")
    for i in resource:
        print(f"{i}: {resource[i]}")
    print("Money: ",money)

def receive(quarters,dimes,nickles,pennies):
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

def resource_exist():
    global money
    for i in data[type]['ingredients']:
        if(resource[i] < data[type]['ingredients'][i]):
            print("Sorry! We dont have enough",i)
            return False
    return True

def produce():
    for i in data[type]['ingredients']:
        resource[i] = resource[i] - data[type]['ingredients'][i]
    return resource

money = 0
report()
answer = 'yes'
while answer == 'yes':
    type = input("What would u like (espresso/latte/cappuccino)?")
    quarters = int(input("Quarter: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    price = data[type]['cost']
    print("You give me: ",receive(quarters,dimes,nickles,pennies))
    if receive(quarters,dimes,nickles,pennies) < price:
        print("It is not enough money")
        break
    else:
        money = money + price
        print("Here is the charge: ",receive(quarters,dimes,nickles,pennies) - price)
        print("Please wait! It will be producing")
        if(resource_exist() == True):
            produce()
        else:
            print("Here is your money back!!")
            money = money - price
            break
    answer = input("Do u want buy another drinks (yes/no)?")
report()
input("Press Enter to exist")