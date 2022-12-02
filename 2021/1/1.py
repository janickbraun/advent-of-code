with open("data.txt") as f:
    lines = f.read().splitlines()

prevNum = None
counter = 0
for line in lines:
    if prevNum is None:
        prevNum = int(line)
    elif prevNum < int(line):
        counter += 1
    prevNum = int(line)

print(counter)