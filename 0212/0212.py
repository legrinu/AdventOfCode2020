#Get Input
file = "0212/0212"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

#Puzzle 1
correct_passwords = 0
for input_string in input_list:
    split_string = input_string.split(" ")
    min_occurence = int(split_string[0].split("-")[0])
    max_occurence = int(split_string[0].split("-")[1])
    char_to_occure = split_string[1].split(":")[0]
    password = split_string[2]

    occurence = password.count(char_to_occure)
    if min_occurence <= occurence <= max_occurence:
        correct_passwords = correct_passwords + 1

print("Puzzle 1:", correct_passwords)


#Puzzle 2
correct_passwords = 0
for input_string in input_list:
    split_string = input_string.split(" ")
    min_position = int(split_string[0].split("-")[0])
    max_position = int(split_string[0].split("-")[1])
    char_to_occure = split_string[1].split(":")[0]
    password = split_string[2]

    occurence = []
    for index, char in enumerate(password):
        if char == char_to_occure:            
            occurence.append(index+1)

    check = 0
    for i in occurence:        
        if (i == min_position) or (i == max_position):
            check = check + 1
    if check == 1:
        correct_passwords = correct_passwords + 1

print("Puzzle 2:", correct_passwords)
