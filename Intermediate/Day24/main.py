#MailMerge Challenge
#Insert names into the letter

PLACEHOLDER = "[name]"

with open("./Day24/Input/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Day24/Input/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Day24/Output/letter_for_{stripped_name}.docx",mode = "w") as completed_letter:
            completed_letter.write(new_letter)
