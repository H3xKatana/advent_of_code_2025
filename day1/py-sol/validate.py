
dial = 50 
rotations = []
password = 0 
with open("validate.aoc") as f : 
    for line in f :
        rotations.append(line.strip())
        
for r in rotations :
    #print(r[0]) 
    if r[0] == "R":
        print(f"[Dial] {dial} Rotating right by {int(r[1:])}")
        dial += int(r[1:])
        dial = dial % 100
    else: 
        print(f"[Dial] {dial}  Rotating left by {int(r[1:])}")
        dial -= int(r[1:])
        dial = dial % 100
    print(f"[UPDATED DIAL] {dial}")
    if dial == 0 : 
            password +=1
print(dial)
print(password)
#print(rotations)