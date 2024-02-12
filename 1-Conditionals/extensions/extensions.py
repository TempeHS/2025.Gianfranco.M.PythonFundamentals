word = input("what ur file name? ")

if word.endswith(".jpg") or word.endswith(".jpeg"):
    print("image/jpg")
elif word.endswith(".png"):
    print("image/png")
elif word.endswith(".pdf"):
    print("documents/pdf")
elif word.endswith(".txt"):
    print("text/txt")
elif word.endswith(".zip"):
    print("compressed/zip")
elif word.endswith(".exe"):
    print("application/exe")
else:
    print("application/octet-stream")
