#alphabet
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

reverso = []

print("I am an atbash cipher encoder")
print("And, correct me if I'm wrong, but atbash probably doesn't need a separate one?")
#gets plaintext from user
plaintext_incor = input("wow zoe you NEED to stop getting screwed over by uppercase. hah. plaintext? ").upper()

plaintext = plaintext_incor.replace(" ","")

ciphertext = ""

counter = 1

#creates the revsersed alphabet
for i in range(1,27):
    reverso.append(alphabet[-counter])
    counter += 1

#wooshy
for i in plaintext:
    if i in alphabet:
        temp = i
        #gets index of word
        temp_index = alphabet.index(temp)
        #gets the reverse of that word
        new_char = reverso[temp_index]
        ciphertext += new_char
    else: 
        ciphertext += temp

#SUCCESS IS SO SWEET        
print(ciphertext)


