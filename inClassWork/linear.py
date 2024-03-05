findThis = "water"
findList = ["poland", "water", "japan"]
location = findList.index(findThis)
for key in findList:
    if findThis == key:
        print(f"found {findThis} in {key}")
    else:
        print("cannot find ur stupid thing")
