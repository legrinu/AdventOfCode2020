#Get Input
file = "0512/0512"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

#Puzzle 1
seat_ids = []
highest_count = 0
for line in input_list:
    row_range = [0, 127]
    seat_range = [0, 7]
    row_count = 0
    seat_count = 0
    row = 0
    seat = 0

    for char in line:
        row_mid = round((row_range[0] + row_range[1]) / 2)
        seat_mid = round((seat_range[0] + seat_range[1]) / 2)

        if char == 'F':
            if row_count == 6:
                row = row_range[0]
            else:
                row_range[1] = row_mid - 1
                row_count += 1           
        if char == 'B':
            if row_count == 6:
                row = row_range[1]
            else:
                row_range[0] = row_mid            
                row_count += 1 
        if char == 'L':
            if seat_count == 2:
                seat = seat_range[0]
            else:
                seat_range[1] = seat_mid - 1
                seat_count += 1  
        if char == 'R':
            if seat_count == 2:
                seat = seat_range[1]
            else:
                seat_range[0] = seat_mid
                seat_count += 1  

    seat_id = (row * 8) + seat
    seat_ids.append(seat_id)
    if seat_id > highest_count:
        highest_count = seat_id

print("Puzzle 1:", highest_count)


#Puzzle 2
seat_ids.sort()
print("Puzzle 2:", sorted(set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids))[0])
