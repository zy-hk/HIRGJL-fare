print("This program only accepts Vigenère ciphers with a keyword of 4 letters long. Sorry!")

#alphabet, bascially
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#gets plaintext from user
text_incor = input("What is your text? ")
text_incor = text_incor.upper()
text_incor = text_incor + "&&&&"

#gets keyword from user
keyword = input("input keyword: ").upper()
#input verification
if len(keyword) != 4:
    keyword = input("input keyword again. must be 4 letters long ")

#a ha restiction :p
length = 4

#declare array for columns
array_1 = []
array_2 = []
array_3 = []
array_4 = []

#removes spaces
text = text_incor.replace(" ","")
        
#the following shit (from the first cat to the second cat) organises the plaintext into columns
#~^-^

if text[0] in alphabet:
    counter_1 = length
    array_1.append(text[0])
    for i in range(1, len(text)):
        if counter_1 >= len(text):
            break
        array_1.append(text[counter_1])
        counter_1 += length
        

if text[1] in alphabet:
    counter_2 = length + 1
    array_2.append(text[1])
    for i in range(1, len(text)):
        if counter_2 >= len(text):
            break
        array_2.append(text[counter_2])
        counter_2 += length
        

if text[2] in alphabet:
    counter_3 = length + 2
    array_3.append(text[2])
    for i in range(1, len(text)):
        if counter_3 >= len(text):
            break
        array_3.append(text[counter_3])
        counter_3 += length
        

if text[3] in alphabet:
    counter_4 = length + 3
    array_4.append(text[3])
    for i in range(1, len(text)):
        if counter_4 >= len(text):
            break
        array_4.append(text[counter_4])
        counter_4 += length

#~^-^     

#displays the columns to user
print(array_1)
print(array_2)
print(array_3)
print(array_4)

#declares dictionary and shift 
thisdict = {}

shift = []

#to copy the alphabet into this dict, annoyingly
indi = 0
for i in alphabet:
    temp_char = i
    thisdict.update({temp_char: indi})
    indi += 1
    
#getting the shift
for i in keyword:
    temptemp = i
    for x in thisdict:
        if temptemp == x:
            shift.append(thisdict[temptemp])

#arrays_richard
arrays_dict = {
    1 : array_1,
    2 : array_2,
    3 : array_3,
    4 : array_4
}

ciphertext = ""


ciphertex = {
    1 : [],
    2 : [],
    3 : [],
    4 : []
}

#mini caesar ciphers
num = 1
numby = 0
for i in arrays_dict:
    x = arrays_dict[num]
    for i in x:
        temp_word = i
        #monstrosity that i coded and don't understand
        if temp_word in alphabet:
            temp_index = alphabet.index(temp_word)
            cipher_temp_index = (temp_index + (shift[numby % len(shift)])) % len(alphabet)
            new_char = alphabet[cipher_temp_index]
            ciphertex[num] += new_char
            ciphertext += new_char
        else: 
            ciphertex[num] += temp_word
    num += 1
    numby += 1

print("")

#following bullshit is to organise shit into columns
#ha
long = len(ciphertex[1]) - 1


cipher_spit = ["!"]

output = []

for i in ciphertext:
    cipher_spit.append(i)
    
cipher_spit.insert(long + 1,"!!")
cipher_spit.insert(long + 1 + long,"!!!")
cipher_spit.insert(long + 1 + long + long, "!!!!")

#yeah bascially fuck me that's what
#hana if youre reading this im sorry its a disaster but my disaster
cipher_spit.append("&&&&&&")

#separating the columns inside the string
numbs = 1
while numbs < long + 1:
    x = cipher_spit.index("!") + numbs
    output.append(cipher_spit[x])
    x = cipher_spit.index("!!") + numbs
    output.append(cipher_spit[x])
    x = cipher_spit.index("!!!") + numbs
    output.append(cipher_spit[x])
    x = cipher_spit.index("!!!!") + numbs
    output.append(cipher_spit[x])
    numbs += 1

final_output = ""

for i in output:
    if i in alphabet:
        final_output += i

#YAY OUTPUT    
final_final_output = "Your encrypted ciphertext is: " + final_output
        
print(final_final_output)

#testing
