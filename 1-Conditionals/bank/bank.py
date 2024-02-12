var = input("Greeting: ")
var = var.strip(" ").lower()

if var.startswith("h") and "hello" in var:
    print("$0")

elif var.startswith("h"):
    print("$20")

else:
    print("$100")
