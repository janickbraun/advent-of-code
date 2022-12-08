with open("data.txt") as f:
    lines = f.read().splitlines()

forest = []
visible = []
forestLine = []

for line in lines:
    row = []
    for letter in line:
        row.append(int(letter))
    forest.append(row)

print("normal", forest)
for i in range(len(forest[0])):
    line = []
    for row in forest:
        line.append(row[i])
    forestLine.append(line)

print("line", forestLine)

for indexRow, row in enumerate(forest):
    if indexRow == 0 or indexRow == len(forest) - 1:
        for number in row:
            visible.append(number)
    else:
        for indexNumber, number in enumerate(row):
            if indexNumber == 0 or indexNumber == len(row) - 1:
                visible.append(number)
            else:
                left = row[:indexNumber]
                right = row[indexNumber + 1:]
                top = forestLine[indexNumber][:indexRow]
                bottom = forestLine[indexNumber][indexRow + 1:]
                if number > max(left) or number > max(right) or number > max(bottom) or number > max(top):
                    visible.append(number)

print(len(visible))

