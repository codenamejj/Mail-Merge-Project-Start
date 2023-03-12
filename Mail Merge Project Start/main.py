PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", "r") as our_names:
    names = our_names.readlines()
    # print(names)

with open("./Output/ReadyToSend/example.txt") as our_template_file:
    template = our_template_file.read()
    # print(template)

for name in names:
    name = name.strip()
    # print(name)
    with open(f"./Output/ReadyToSend/invited_{name}.txt", "w") as our_letter_file:
        new_template = template.replace(PLACEHOLDER, name)
        # print(new_template)
        our_letter_file.write(f"{new_template}")
