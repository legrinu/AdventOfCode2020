#Input
file = "0612/0612"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

#Format
stripped_list = []
for item in input_list:
    stripped_list.append(str.strip(item))

#Puzzle 1
count_per_group = []
sum_count = 0
letters = []
for line in stripped_list:
    if line == "":
        count_per_group.append(len(letters))
        sum_count += len(letters)
        letters = []
    else:
        for char in line:
            if not char == "\n":
                if char not in letters:
                    letters.append(char)
print("Puzzle 1:", sum_count)


#Puzzle 2
count_per_group = []
sum_count = 0
letters = []
count = 0
run = 0
for line in stripped_list:
    run += 1
    if line == "":
        letter_set = set([x for x in letters if letters.count(x) >= run-1])
        count_per_group.append(len(letter_set))
        sum_count += len(letter_set)
        letters = []
        run = 0
    else:
        for char in line:
            letters.append(char)    
print("Puzzle 2:", sum_count)