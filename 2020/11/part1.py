with open("data.txt") as f:
    linesOld = f.readlines()

lines = []

for line in linesOld:
    lines.append(line.replace("\n", ""))

floor = "."
freeSeat = "#"
usedSeat = "L"

print(lines)

lineIndex = 0
letterIndex = 0

for line in lines:
    if len(lines) < lineIndex:
        break
    for letter in line:
        if len(lines[lineIndex]) < letterIndex:
            break
        if letter == freeSeat:
            try:
                if lines[lineIndex + 1] != usedSeat and lines[lineIndex - 1] != usedSeat and lines[lineIndex][letterIndex + 1] != usedSeat and lines[lineIndex][letterIndex - 1] != usedSeat:
                    print("setzen")
            except IndexError:
                pass
        letterIndex += 1

    lineIndex += 1
