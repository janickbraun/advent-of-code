with open("data.txt") as f:
    lines = f.read().splitlines()

pairsOld = []

for line in lines:
    pairsOld.append(line.split(","))

pairs = []

for pair in pairsOld:
    par = []
    for elf in pair:
        par.append(elf.split("-"))
    pairs.append(par)

count = 0

for pair in pairs:
    pair = list(map(int, pair[0])), list(map(int, pair[1]))
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] or pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
        count += 1

print(count)