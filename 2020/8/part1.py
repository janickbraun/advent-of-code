with open("data.txt") as f:
    linesOld = f.readlines()

lines = []
lineIndex = 0
accCount = 0
usedIndexes = [0]
for line in linesOld:
    lines.append(line.replace("\n", ""))

while len(lines) > lineIndex:
    if lines[lineIndex].startswith("nop"):
        lineIndex += 1
        if lineIndex in usedIndexes:
            print(accCount)
            break
        else:
            usedIndexes.append(lineIndex)

    elif lines[lineIndex].startswith("acc"):
        if lines[lineIndex][4] == "+":
            num = lines[lineIndex].split("+")
            accCount += int(num[1])
        elif lines[lineIndex][4] == "-":
            num = lines[lineIndex].split("-")
            accCount -= int(num[1])
        lineIndex += 1
        if lineIndex in usedIndexes:
            print(accCount)
            break
        else:
            usedIndexes.append(lineIndex)
    elif lines[lineIndex].startswith("jmp"):
        if lines[lineIndex][4] == "+":
            num = lines[lineIndex].split("+")
            lineIndex += int(num[1])
            if lineIndex in usedIndexes:
                print(accCount)
                break
            else:
                usedIndexes.append(lineIndex)
        elif lines[lineIndex][4] == "-":
            num = lines[lineIndex].split("-")
            lineIndex -= int(num[1])
            if lineIndex in usedIndexes:
                print(accCount)
                break
            else:
                usedIndexes.append(lineIndex)

