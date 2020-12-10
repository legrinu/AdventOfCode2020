file = "0812/0812"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

stripped_list = []
for item in input_list:
    stripped_list.append(str.strip(item))

def cmd_exec(cmd_line, acc, lne):
    cmd_split = cmd_line.split(" ")
    cmd = cmd_split[0]
    sig = cmd_split[1][0]
    val = int(cmd_split[1][1:])

    if cmd == "acc":
        if sig == "+":
            acc += val
            lne += 1
        elif sig == "-":
            acc -= val            
            lne += 1
    elif cmd == "jmp":
        if sig == "+":
            lne += val
        elif sig == "-":
            lne -= val
    elif cmd == "nop":
        lne += 1
    else:
        print ("UnknownInputException(Command not found)")
    
    return acc, lne

accumulator = 0
line = 0
known_lines = []
stop = False
while not stop:
    act_cmd = stripped_list[line]
    known_lines.append(line)
    accumulator, line = cmd_exec(cmd_line=act_cmd, acc=accumulator, lne=line)
    if line in known_lines:
        print("Puzzle 1:", accumulator)
        stop = True

