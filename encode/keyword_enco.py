alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alphabet_2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

keyword = input("Enter keyword: ").upper()


for i in keyword:
	temp_word = i
	if temp_word in keyword:
		new_index = alphabet.index(temp_word)
		alphabet.pop(new_index)
		

keyword_alpha = []

for i in keyword:
    keyword_alpha.append(i)

for i in alphabet:
    keyword_alpha.append(i)
    

print(alphabet_2)

print(keyword_alpha)

ciphertext = ""

plaintext = input("what is plaintext! ").upper()

for x in plaintext:
    if x in alphabet_2:
        index = alphabet_2.index(x)
        ciphertext += keyword_alpha[index]
    else: 
        ciphertext += x
        
print(ciphertext)
    

