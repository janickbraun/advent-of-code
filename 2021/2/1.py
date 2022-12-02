with open("D:/Development/Python/Advent/2021/2/data.txt") as f:
    lines = f.read().splitlines()

depth = 0 # down ++
horizontal = 0
for oldLine in lines:
    command = oldLine.split(" ")[0]
    units = int(oldLine.split(" ")[1])
    if command == "forward":
        horizontal += units
    elif command == "down":
        depth += units
    elif command == "up":
        depth -= units

print(depth * horizontal)