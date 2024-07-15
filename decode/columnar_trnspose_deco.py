
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

keyword_index = []
keyword_words = {1:"",2:"",3:"",4:""}
corespondence = {1:[],2:[],3:[],4:[]}



#get keyword from user
keyword = input("what is keyword? ").upper()
#input valid
while len(keyword) != 4:
    keyword = input("keyword can only be 4 letters long. what is keyword? ").upper()


#keyword can only be length of 4 

#gets text from user
text_incor = input("What is your text? ").upper()
text_incor = text_incor + "&&&&"
text = text_incor.replace(" ","")

#input valid until i get smarter
while len(text) % 4 != 0 or len(text) < 4:
    print("Sorry but transposition and python are just being annoying so can you reenter the text which has a length (barring spaces) that is diviable by 4. some methods you can use is via adidng x to the end of it or cutting some letters")
    text_incor = input("What is your text? ").upper()
    text_incor = text_incor + "&&&&"
    text = text_incor.replace(" ","")

regar_key = sorted(keyword)

#processes and creates index of keywords
num = 1
for i in keyword:
    keyword_words[num] += i
    x = alphabet.index(i)
    keyword_index.append(x)
    if num < 4:
        num += 1



print(keyword_words)
        
print(keyword_index)

rearranged = sorted(keyword_index)

print(rearranged)


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

#putting text into corespondence
for i in array_1:
    corespondence[1].append(i)
for i in array_2:
    corespondence[2].append(i)
for i in array_3:
    corespondence[3].append(i)
for i in array_4:
    corespondence[4].append(i)


# changing keys of dictionary
numby = 1
str(numby)
for i in regar_key:
    corespondence[i] = corespondence[numby]
    del corespondence[numby]
    numby += 1



print(corespondence)



alltext = []

#rearranges corespondence to keyword AHA FRICK U
for i in corespondence[keyword[0]]:
    alltext.append(i)
for i in corespondence[keyword[1]]:
    alltext.append(i)
for i in corespondence[keyword[2]]:
    alltext.append(i)
for i in corespondence[keyword[3]]:
    alltext.append(i)

print(alltext)


#removes safety fillers
for i in alltext:
    if i == "&":
        x = alltext.index(i)
        alltext.pop(x)
        

long = len(array_1)


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


