with open("data.txt") as f:
    linesOld = f.readlines()

lines = []

for line in linesOld:
    lines.append(line.replace("\n", ""))

earlyTime = int(lines[0])
OldBusIDs = [lines[1].split(",")]

busIDs = []
for item in OldBusIDs:
    for letter in item:
        if not letter == "x":
            busIDs.append(letter)
lowesWait = None
lowesId = None
for ID in busIDs:
    rhythm = 0
    while rhythm < earlyTime:
        rhythm += int(ID)

    if lowesWait is None or rhythm - earlyTime < lowesWait:
        lowesWait = rhythm - earlyTime
        lowesId = ID

print("senke:", int(lowesId) * lowesWait)
