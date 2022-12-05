import re

with open("data.txt") as f:
    lines = f.read().splitlines()

chests = []
moves = []
box = []

for line in lines:
    if line.startswith("move"):
        moves.append(list(map(int, re.findall(r'\d+', line))))


def goHigher(lineIndex, letterIndex):
    try:
        if lines[lineIndex - 1][letterIndex] != " " and lines[lineIndex - 1][letterIndex].isnumeric() == False and lines[lineIndex - 1][letterIndex] != "o":
            box.append(lines[lineIndex - 1][letterIndex])
            goHigher(lineIndex - 1, letterIndex)
    except IndexError:
        pass


for lineIndex, line in enumerate(lines):
    if line.startswith(" 1"):
        for letterIndex, letter in enumerate(line):
            if letter != " ":
                goHigher(lineIndex, letterIndex)
                chests.append(box)
                box = []

for chest in chests:
    chest = chest.reverse()

for move in moves:
    upe = chests[move[1] - 1][0:move[0]]
    for i in range(move[0]):
        chests[move[1] - 1].pop(0)
    upe = list(reversed(upe))
    chests[move[2] - 1] = upe + chests[move[2] - 1]

print(chests)
print(moves)

for chest in chests:
    print(chest[0], end="")
