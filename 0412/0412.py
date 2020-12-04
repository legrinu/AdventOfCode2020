import re

#Get Input
file = "0412/0412"
input_list = []
with open(file, "r") as input_file:
    input_list = input_file.readlines()

#Puzzle 1
valid_passports = 0
passport = []
pattern = r"(\bbyr\b|\biyr\b|\beyr\b|\bhgt\b|\bhcl\b|\becl\b|\bpid\b)"
for line in input_list:    
    if line == "\n":
        valid_count = 0
        for entry in passport:            
            if re.search(pattern=pattern, string=entry):
                valid_count += 1

        if valid_count == 7:
            valid_passports += 1
        passport = []

    else:
        entrys = line.split(" ")
        for entry in entrys:
            passport.append(entry.split(":")[0])

print("Puzzle 1:", valid_passports)


#Puzzle 2
valid_passports = 0
passport = []
#RegEx Stuff
byr_pattern = r"(byr:)(19[2-9][0-9]|200[0-2])"
iyr_pattern = r"(iyr:)(201[0-9]|2020)"
eyr_pattern = r"(eyr:)(202[0-9]|2030)"
hgt_pattern = r"(hgt:)((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)"
hcl_pattern = r"(hcl:#)(\b[0-9a-f]{6}\b)"
ecl_pattern = r"(ecl:)(amb|blu|brn|gry|grn|hzl|oth)"
pid_pattern = r"(pid:)(\b\d{9}\b)"
pattern = r"((byr:)(19[2-9][0-9]|200[0-2]))|((iyr:)(201[0-9]|2020))|((eyr:)(202[0-9]|2030))|((hgt:)((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in))|((hcl:#)(\b[0-9a-f]{6}\b))|((ecl:)(amb|blu|brn|gry|grn|hzl|oth))|((pid:)(\b\d{9}\b))"

for line in input_list:    
    if line == "\n":
        valid_count = 0
        for entry in passport:            
            if re.search(pattern=pattern, string=entry):
                valid_count += 1

        if valid_count == 7:
            valid_passports += 1
        passport = []

    else:
        entrys = line.split(" ")
        for entry in entrys:
            passport.append(entry)

print("Puzzle 2:", valid_passports)