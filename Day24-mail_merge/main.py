#TODO: Create a letter using starting_letter.txt



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
with open("Input/Names/invited_names.txt") as invited_names:
    actual_names = invited_names.readlines()

for each in actual_names:
    # strip newline from actual names
    each = each.replace("\n", "")

    with open("Input/Letters/starting_letter.txt") as starting_letter:
        letter = starting_letter.readlines()

    letter[0] = letter[0].replace("[name]", each)
    print(letter)
    # strip newline
    #letter[0] = letter[0].replace("\n", "", 1)



    with open(f"Output/ReadyToSend/letter_to_{each}.txt", mode="w") as letter_fin:
        for each in letter:
            letter_fin.write(each)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp