number_1 = float(input("first number: "))
number_1 = round(number_1, 1)
number_2 = float(input("second number: "))
number_2 = round(number_2, 1)


def calculate():
    operation = input("what operator? (+ , - , *, /) ")

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2, 2)

    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)


calculate()
