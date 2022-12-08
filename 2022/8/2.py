with open("data.txt") as f:
    lines = f.read().splitlines()

forest = []
forestLine = []
visible = 0

for line in lines:
    row = []
    for letter in line:
        row.append(int(letter))
    forest.append(row)

for i in range(len(forest[0])):
    line = []
    for row in forest:
        line.append(row[i])
    forestLine.append(line)

print("normal", forest)
print("line", forestLine)

for indexRow, row in enumerate(forest):
    for indexNumber, number in enumerate(row):
        left = row[:indexNumber]
        right = row[indexNumber + 1:]
        top = forestLine[indexNumber][:indexRow]
        bottom = forestLine[indexNumber][indexRow + 1:]
        count = 0
        top.reverse()
        left.reverse()
        distanceLeft = 1
        for i in range(len(left) - 1):
            if left[i] < number:
                distanceLeft += 1
            elif left[i] >= number:
                break
        distanceRight = 1
        for i in range(len(right) - 1):
            if right[i] < number:
                distanceRight += 1
            elif right[i] >= number:
                break
        distanceTop = 1
        for i in range(len(top) - 1):
            if top[i] < number:
                distanceTop += 1
            elif top[i] >= number:
                break
        distanceBottom = 1
        for i in range(len(bottom) - 1):
            if bottom[i] < number:
                distanceBottom += 1
            elif bottom[i] >= number:
                break

        count = distanceTop * distanceBottom * distanceLeft * distanceRight
        #print(indexRow, left, right, top, bottom, count)
        if count > visible:
            visible = count

print(visible)
