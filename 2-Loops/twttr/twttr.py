text = input("WHAT IS UR TWWET????? ")

print("ur cool twt: ", end="")

for char in text:
    if not char.lower() in ["a", "e", "i", "o", "u"]:
        print(char, end="")

print()
