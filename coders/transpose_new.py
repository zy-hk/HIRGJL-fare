print("This code works both ways for encryption and decryption using the same configuration.")

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
bloop = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

# Get text from user
text_incor = input("What is your text? ").upper()
text = text_incor.replace(" ", "")

length = int(input("How many columns are there? "))

# Input valid until length is divisible by 6
while len(text) % length != 0 or len(text) < length:
    print("Please enter text with a length (excluding spaces) that is divisible by the amount of columns.")
    text_incor = input("What is your text? ").upper()
    text = text_incor.replace(" ", "")

for i in range(length):
    text += "&"



# Initialize arrays for columns
arrays = [[] for _ in range(length)]

# Fill the arrays with characters from the text
for i in range(length):
    counter = i
    while counter < len(text):
        arrays[i].append(text[counter])
        counter += length

# Display the columns to the user
for idx, arr in enumerate(arrays):
    print(f"This is column {idx + 1}:")
    print(arr)

# Column rearrangement
dict_array = {i + 1: arrays[i] for i in range(length)}
thisdict = {i: [] for i in range(1, length + 1)}

# Rearrangement input
for i in range(1, length + 1):
    usin = int(input(f"Which column do you want to rearrange to be column {i}? (1-{length}): "))
    if usin in dict_array:
        print(dict_array[usin])
        thisdict[i] = dict_array[usin]

# Combine rearranged columns
alltext = []
for i in range(1, length + 1):
    alltext.extend(thisdict[i])

# Remove safety fillers
alltext = [i for i in alltext if i != "&"]

# Prepare for output
output = []
long = len(dict_array[1])
for i in range(long):
    for j in range(1, length + 1):
        output.append(thisdict[j][i])

# Final output
final_output = "".join([i for i in output if i in alphabet])
print("Your text is:", final_output)

