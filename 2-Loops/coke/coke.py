myList = [5, 10, 25]
moneyNeed = 50

while moneyNeed > 0:
    print("YOU NEED ", moneyNeed)
    money = int(input("put in moeny !! (cents) "))
    if money in myList:
        moneyNeed -= money

change = moneyNeed

print("change i give ", change)
if change == 0:
    print("COKE DISEPNDED !")
