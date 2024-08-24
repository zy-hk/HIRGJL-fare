alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def result(key1,key2,pla1,pla2):
    x = key1*pla1
    y = key2*pla2
    z = x + y
    while z > 25:
        z -= 26
    return(z)


modulo = 26 

ciphertext = []
ciphertext_result = []


keyword = input("What is keyword? no longer than 4 words: ").upper()

keyword_index = []
key_numbers = {"lvl1":[],"lvl2":[]}
   

for i in keyword:
    x = alphabet.index(i)
    keyword_index.append(x)


det = keyword_index[0]*keyword_index[3]-keyword_index[1]*keyword_index[2] 

print(det)

det_inverse = pow(det, -1, modulo)

print(det_inverse)

invert_1 = (det_inverse * keyword_index[3])
invert_2 = (det_inverse * (26 - keyword_index[1]))
invert_3 = (det_inverse * (26 - keyword_index[2]))
invert_4 = (det_inverse * keyword_index[0])


invert = [invert_1, invert_2, invert_3, invert_4,]

invert = [i % 26 for i in invert]
   
print(invert)

key_numbers["lvl1"].append(invert[0])
key_numbers["lvl1"].append(invert[1])
key_numbers["lvl2"].append(invert[2])
key_numbers["lvl2"].append(invert[3])

print(key_numbers)

plain = input("what is plaintext, no more than 4: ").upper()
plain_index = []

for i in plain:
    x = alphabet.index(i)
    plain_index.append(x)

print(plain_index)


cipher_1 = result(key_numbers["lvl1"][0],key_numbers["lvl1"][1],plain_index[0],plain_index[1])
cipher_2 = result(key_numbers["lvl2"][0],key_numbers["lvl2"][1],plain_index[0],plain_index[1])
cipher_3 = result(key_numbers["lvl1"][0],key_numbers["lvl1"][1],plain_index[2],plain_index[3])
cipher_4 = result(key_numbers["lvl2"][0],key_numbers["lvl2"][1],plain_index[2],plain_index[3])

ciphertext.append(cipher_1)
ciphertext.append(cipher_2)
ciphertext.append(cipher_3)
ciphertext.append(cipher_4)

print(ciphertext)

for i in ciphertext:
    ciphertext_result.append(alphabet[i])

print(ciphertext_result)