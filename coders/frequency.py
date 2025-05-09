alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

frequency = {"A":0,"B":0,"C":0,"D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

#gets text from user
text_incor = input("What is your text? ").upper()
text = text_incor.replace(" ","")



for i in text:
    tempwrd = i
    if tempwrd in alphabet:
        for x in alphabet:
            if x == tempwrd:
                frequency[x] += 1

print(frequency)

