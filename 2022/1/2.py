with open("data.txt") as f:
    lines = f.read().splitlines()

elves = []
elf = []
for line in lines:
    if line != "":
        elf.append(int(line))
    elif line == "":
        elves.append(elf)
        elf = []

elves.append(elf)

checksums = []

for elf in elves:
    checksums.append(sum(elf))

checksums.sort(reverse=True)

total = 0

for i in range(3):
    total += checksums[i]

print(total)