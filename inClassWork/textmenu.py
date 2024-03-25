import os

while True:
    print(
        """
        text menu!
        1. play gmae
        2. say funny word
        3. do third option
        4. exit and leave
        """
    )
    userInput = input("WHICH ONE YOU WANT? ")
    if userInput == "1":
        os.system("python rps.py")
    elif userInput == "2":
        print("FUNNN NN YOWRD GHAHAHAHAHAHAA")
    elif userInput == "3":
        print("third option")
    else:
        break
