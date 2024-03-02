try:
    fuelLevel = input("WHAT IS FUEL LEVEL IN FRACTION? ")
    a, b = map(int, fuelLevel.split("/"))
    if b == 0:
        raise ZeroDivisionError("IDIOT DONT USE ZEROR IN DIVIDOE!!! ")
    fuelFloat = a / b

    def fuelCalc():
        global fuelFloat
        if fuelFloat <= 0.1:
            print("E")
        elif 0.1 < fuelFloat < 0.99:
            fuelFloatCon = fuelFloat * 100
            print(fuelFloatCon, "%")
        elif 0.99 < fuelFloat < 1.01:
            print("F")
        else:
            print("STUPID")

    fuelCalc()

except ValueError:
    print("USE FRACITON !@!!!!!!!!!!!!!!!!!!!!!!!")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("An unexpected error occurred:", e)
