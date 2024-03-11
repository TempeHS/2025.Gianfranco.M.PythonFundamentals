dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

money = float(0)
try:
    while money < 100:
        userInput = input("what ur order man? ")
        userInput = userInput.title()
        if userInput in dict:
            price = float(dict.get(userInput))
            money = price + money
            txt = "total: ${:.2f}"
            print(txt.format(money))
except EOFError:
    txt = "total: ${:.2f}"
    print(txt.format(money))
