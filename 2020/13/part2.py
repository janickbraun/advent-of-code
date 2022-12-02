with open("data.txt") as f:
    linesOld = f.readlines()

lines = []

for line in linesOld:
    lines.append(line.replace("\n", ""))

OldBusIDs = [lines[1].split(",")]

busIDs = []
for item in OldBusIDs:
    for letter in item:
        busIDs.append(letter)

# beginning

print(busIDs)
