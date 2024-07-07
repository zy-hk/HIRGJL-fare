alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

plaintext = ""

print("Hello! I am your little caesar decoder! :)")

while True:
    try:
        shift = int(input("By how many characters was it shifted originally? "))
        break 
    except ValueError:
        print("Please enter a valid number.")
        
if shift > 25 or shift < 1:
    print("Incorrect value.")
    shift = int(input("By how many characters should it shift? "))


ciphertext = input("What is your encrypted text? ").upper()


for i in ciphertext:
    temp_word = i
    if temp_word in alphabet:
        temp_index = alphabet.index(temp_word)
        plain_temp_index = (temp_index - shift) % len(alphabet)
        new_char = alphabet[plain_temp_index]
        plaintext += new_char
    else: 
        plaintext += temp_word

print(plaintext)


