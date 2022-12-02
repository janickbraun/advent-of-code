import itertools

with open("data.txt") as f:
    linesOld = f.readlines()

lines = []
lastNum = []
goBack = 5
lineIndex = 0
found = False
invalidNum = None

for line in linesOld:
    lines.append(int(line.replace("\n", "")))

for item in lines:
    if lineIndex <= goBack and not lineIndex == 0:
        lastNum.append(int(lines[lineIndex - 1]))
    elif not lineIndex == 0 and len(lastNum) >= goBack:
        lastNum.pop(0)
        lastNum.append(int(lines[lineIndex - 1]))

    if found:
        break
    valid = False
    if len(lastNum) == goBack:
        for num1 in lastNum:
            for num2 in lastNum:
                if not num1 == num2:
                    if num1 + num2 == item:
                        valid = True
        if not valid:
            invalidNum = item
            found = True

    lineIndex += 1

# ------



print(invalidNum)
