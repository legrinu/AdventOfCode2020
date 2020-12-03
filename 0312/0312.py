#Get Input
file = "0312/0312"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

#Puzzle 1
start_value = 0
tree_counter = 0
for line in input_list:
    if start_value >= 31:
        start_value = start_value - 31
    act_pos = line[start_value]
    if act_pos == '#':
        tree_counter = tree_counter + 1
    start_value = start_value + 3

print("Puzzle 1:", tree_counter)


#Puzzle 2

#Slope 1
start_value = 0
tree_counter_1 = 0
for line in input_list:
    if start_value >= 31:
        start_value = start_value - 31
    act_pos = line[start_value]
    if act_pos == '#':
        tree_counter_1 = tree_counter_1 + 1
    start_value = start_value + 1
print("Slope 1:", tree_counter_1)

#Slope 2
tree_counter_2 = tree_counter
print("Slope 2:", tree_counter_2)

#Slope 3
start_value = 0
tree_counter_3 = 0
for line in input_list:
    if start_value >= 31:
        start_value = start_value - 31
    act_pos = line[start_value]
    if act_pos == '#':
        tree_counter_3 = tree_counter_3 + 1
    start_value = start_value + 5
print("Slope 3:", tree_counter_3)

#Slope 4
start_value = 0
tree_counter_4 = 0
for line in input_list:
    if start_value >= 31:
        start_value = start_value - 31
    act_pos = line[start_value]
    if act_pos == '#':
        tree_counter_4 = tree_counter_4 + 1
    start_value = start_value + 7
print("Slope 4:", tree_counter_4)

#Slope 4
start_value = 0
horizontal_value = 0
tree_counter_5 = 0
for line in input_list:
    if horizontal_value == 0:
        if start_value >= 31:
            start_value = start_value - 31
        act_pos = line[start_value]
        if act_pos == '#':
            tree_counter_5 = tree_counter_5 + 1
        start_value = start_value + 1
        horizontal_value = 2

    if horizontal_value >= 1:
        horizontal_value = horizontal_value - 1
print("Slope 5:", tree_counter_5)

#Multiplikation
mult = tree_counter_1 * tree_counter_2 * tree_counter_3 * tree_counter_4 * tree_counter_5
print("Puzzle 2:", mult)