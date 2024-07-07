print("transposition is a bitch and i am a idiot ")
print("this code works boths ways for encryption and decryption use the same config")
print("omg imagine making an enigma encoder one day")

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

bloop = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

alltext = []
allatext = []

#gets text from user
text_incor = input("What is your text? ").upper()
text_incor = text_incor + "&&&&"
text = text_incor.replace(" ","")

#input valid until i get smarter
while len(text) % 4 != 0 or len(text) < 4:
    print("sorry but transposition and python are just being annoying so can you reenter the text which has a length (barring spaces) that is diviable by 4. some methods you can use is via adidng x to the end of it or cutting some letters")
    text_incor = input("What is your text? ").upper()
    text_incor = text_incor + "&&&&"
    text = text_incor.replace(" ","")




length = 4

array_1 = []
array_2 = []
array_3 = []
array_4 = []

#removes spaces
text = text_incor.replace(" ","")
        
#puts text in columns from the cat to the other
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
print("this is column 1") 
print(array_1)
print("this is column 2") 
print(array_2)
print("this is column 3") 
print(array_3)
print("this is column 4") 
print(array_4)

#richard_array
dict_array =  {1:array_1, 2:array_2, 3:array_3, 4:array_4}
    
thisdict = {1:[], 2:[], 3:[], 4:[]}

#from the annoyed face to the other gets the rearrangment of columns from user
#\>.</
usin1 = int(input("which column do you want to rearange to be column 1? (type a number only please i beg of you:  "))
for i in range(1,5):
    if usin1 == i:
        print(dict_array[usin1])
        #copies from dict to string and dict to other dict
        for i in dict_array[usin1]:
            alltext.append(i)
        thisdict[1].append(dict_array[usin1])
    
        
usin2 = int(input("which column do you want to rearange to be column 2? (type a number only please i beg of you:  "))
for i in range(1,5):
    if usin2 == i:
        print(dict_array[usin2])
        for x in dict_array[usin2]:
            alltext.append(x)
        thisdict[2].append(dict_array[usin2])
        
usin3 = int(input("which column do you want to rearange to be column 3? (type a number only please i beg of you:  "))
for i in range(1,5):
    if usin3 == i:
        print(dict_array[usin3])
        for x in dict_array[usin3]:
            alltext.append(x)
        thisdict[3].append(dict_array[usin3])

usin4 = int(input("which column do you want to rearange to be column 4? (type a number only please i beg of you:  "))

for i in range(1,5):
    if usin4 == i:
        print(dict_array[usin4])
        for x in dict_array[usin4]:
            alltext.append(x)
        thisdict[4].append(dict_array[usin4])
        
#\>.</

#removes safety fillers
for i in alltext:
    if i == "&":
        x = alltext.index(i)
        alltext.pop(x)
        

long = len(dict_array[1])


spit = ["!"]

output = []

#adds things to the other string (yes there are a lot of variables)
for i in alltext:
    spit.append(i)
    

#separating columns in string    
spit.insert(long,"!!")
spit.insert(long + long,"!!!")
spit.insert(long + long + long, "!!!!")


#safety padders
spit.append("&")
spit.append("&")
spit.append("&")
spit.append("&")


print(spit)

#gets the things to output by reading by rows
numbs = 1
while numbs < long + 1:
    x = spit.index("!") + numbs
    output.append(spit[x])
    x = spit.index("!!") + numbs
    output.append(spit[x])
    x = spit.index("!!!") + numbs
    output.append(spit[x])
    x = spit.index("!!!!") + numbs
    output.append(spit[x])
    numbs += 1

final_output = ""

for i in output:
    if i in alphabet:
        final_output += i

#YES OUTPUT        
final_final_output = "Your text is: " + final_output
        
print(final_final_output)





