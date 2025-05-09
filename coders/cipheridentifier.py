import matplotlib.pyplot as plt
import numpy as np

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

frequency = {"A":0,"B":0,"C":0,"D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

engpercent = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074]

nmfreq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
freqpercent = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def freq(text):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in text:
        for j in alphabet:
            if i == j:
                num = alphabet.index(j)
                frequency[num] += 1
    return frequency
    
def ioc(length, frequency):
    total = 0
    for i in frequency:
        var1 = i * (i-1)
        var2 = length * (length - 1)
        var3 = var1/var2
        total += var3

    total = round(total, 4)
    return total

#gets text from user
text_incor = input("What is your text? ").upper()
text = text_incor.replace(" ","")

if len(text) < 100:
    print("text is quite short, may not result in the correct result")

totaltextlength = len(text)

for i in text:
    tempwrd = i
    if tempwrd in alphabet:
        b = alphabet.index(tempwrd)
        nmfreq[b] += 1
        for x in alphabet:
            if x == tempwrd:
                frequency[x] += 1

print(frequency)

for i in range(25):
    b = ((nmfreq[i])/totaltextlength) * 100
    a = round(b,2)
    freqpercent[i] += a

#graph LOOK HANA I PUT IN A COMMENT THAT ISNT USER INPUT BE PROUD
xpoints = np.array(alphabet)
ypoints1 = np.array(freqpercent)
ypoints2 = np.array(engpercent)


plt.plot(xpoints, ypoints2, c = "r", label=" english")
plt.plot(xpoints, ypoints1, label=" ciphertext")

plt.title("FREQUENCY ANALYSIS")
plt.xlabel("alphabet")
plt.ylabel("frequency in text (%)")
plt.legend(loc="upper left")

plt.grid()

plt.show()

length = len(text)

total = 0
for i in range(0,26):
    var1 = nmfreq[i] * (nmfreq[i] - 1)
    var2 = length * (length - 1)
    var3 = var1 / var2
    total += var3

total = round(total, 4)
total = str(total)
print("index of coincidence is " + total)
total = float(total)

if total >= 0.06:
    print("usually transposition or monalphabetic")
elif total >= 0.03:
    print("probably polyalphabetic")
    vigyes = True
else:
    print("ha you're screwed!")


if vigyes == True:
    key_iocs = []

    for keylen in range(1,10):
        arrays = [[] for _ in range(keylen)]

        for i, j in enumerate(text):
            arrays[i % keylen].append(i)

        frequencies = [[] for _ in range(keylen)]
        iocs = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        texts = []

        for i in range(keylen):
            texts.append("".join(text[j] for j in arrays[i]))

        for i in range(keylen):
            lengthy = len(texts[i])
            frequencies[i] = freq(texts[i])
            iocs[i] += ioc(lengthy, frequencies[i])


        average = 0
        for i in iocs:
            average += i
        average = average/keylen
            
        key_iocs.append(average)

    print(key_iocs)

    largest = max(key_iocs)
    keylength = key_iocs.index(largest)
    keylength += 1
    keylength = str(keylength)

    print("your most likely vigniere key length is " + keylength)
else:
    print("goodlucky!")