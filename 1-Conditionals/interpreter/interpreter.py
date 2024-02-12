def calculate():
    operation = input("what operator? (+ , - , *, /) ")

    number_1 = int(input("first number: "))
    number_2 = int(input("second number: "))

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)


calculate()
