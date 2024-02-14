def mealtime():
    meal = input("whats the time prick?! ")
    meal = convert(meal)
    if 7 <= meal <= 8:
        print("it is breakfast time !")
    elif 12 <= meal <= 13:
        print("it is lunch time !")
    elif 18 <= meal <= 19:
        print("it is dinner time !")
    else:
        print("it is nothing time !")


def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes) / 60
    return time


mealtime()
