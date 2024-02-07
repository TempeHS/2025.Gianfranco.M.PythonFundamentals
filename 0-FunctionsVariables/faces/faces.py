#main function
def convert(sentence):
    return sentence.replace(":)", "🙂").replace(":(", "🙁").replace(":|", "😐")

#query
sentence = input("how u feeling? ")

#conversion
final = convert(sentence)

#print
print(final)