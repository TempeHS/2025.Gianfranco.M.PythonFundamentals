monthList = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    userDate = input("give date: ").title()
    try:
        if "/" in userDate:
            mm, dd, yyyy = userDate.split("/")
        elif "," in userDate:
            mmdd, yyyy = userDate.split(", ")
            mm, dd = mmdd.split(" ")
            mm = (monthList.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break
