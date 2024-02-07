# ask for name remove spaces and capitalsier
name = input("whats ur name? ").strip().title()

# split first and last names
first, last = name.split(" ")

# say hello
print("hello, " + first)

# :)
