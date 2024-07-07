#Alphabet array
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

ciphertext = ""

print("Hello! I am your little caesar encoder! :)")

#input validation for value type
while True:
    try:
        #get shift
        shift = int(input("By how many characters should it shift? "))
        break 
    except ValueError:
        print("Please enter a valid number.")

#input validation for numbers        
if shift > 25 or shift < 1:
    print("Incorrect value.")
    shift = int(input("By how many characters should it shift? "))

#get plaintext for user
plaintext = input("What is your plaintext? ").upper()

#encoder
for i in plaintext:
    temp_word = i
    if temp_word in alphabet:
        temp_index = alphabet.index(temp_word)
        cipher_temp_index = (temp_index + shift) % len(alphabet)
        new_char = alphabet[cipher_temp_index]
        ciphertext += new_char
    else: 
        ciphertext += temp_word

#display ciphertext
print("Your encrypted ciphertext")
print(ciphertext)

