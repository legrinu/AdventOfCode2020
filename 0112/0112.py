#Get Input
file = "0112/Input_0112"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

for i in range(0, len(input_list)): 
    input_list[i] = int(input_list[i]) 


#Puzzle 1
breaker = False
for num in input_list:
    for num2 in input_list:
        result = num + num2
        if result == 2020:
            print("Solution Puzzle 1:", num * num2)
            breaker = True
    if breaker:
        break
       

#Puzzle 2
breaker = False
for num in input_list:
    for num2 in input_list:
        for num3 in input_list:
            result = num + num2 + num3
            if result == 2020:                
                breaker = True
                print("Solution Puzzle 2:", num * num2 * num3)
        if breaker:
            break    