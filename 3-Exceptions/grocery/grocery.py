groceryDict = {}
while True:
    try:
        item = input("what u buy ").upper().strip()
        if item not in groceryDict:
            groceryDict[item] = 1
        else:
            groceryDict[item] = groceryDict[item] + 1
    except EOFError:
        sortedDict = dict(sorted(list(groceryDict.items())))
        for item in sortedDict:
            print()
            print(sortedDict[item], item, sep=" ")
        break
    except KeyError:
        pass
