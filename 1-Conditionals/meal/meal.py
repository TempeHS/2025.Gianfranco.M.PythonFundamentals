def meal():
    time = input("whats the time prick? ")


meal()


def convert(time):
    hour, minute = time.split(":")
    time = float(hour) + float(minute) / 60
    return time


time = convert(meal)


print(time)
