# TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
with open("./input/names/invited_names.txt") as names_f:
    names = names_f.readlines()

with open("./input/letters/starting_letter.txt") as ex_letter_f:
    letter_lines = ex_letter_f.read()
for name in names:
    stripped_name = name.strip()
    with open(f"./output/ReadyToSend/{stripped_name}_letter.txt", mode="w") as out_f:
        out_f.write(letter_lines.replace(PLACEHOLDER, stripped_name))

        #for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp