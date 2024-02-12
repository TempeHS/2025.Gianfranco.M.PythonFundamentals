# assign input to var
var = input("what is the answer to life, the universe and everything? ")

# strip and lower var
var = var.strip(" ").lower()

# list of values
lst = ["42", "forty two", "forty-two"]

if var in lst:
    print("YES !!!")

else:
    print("NO !")
