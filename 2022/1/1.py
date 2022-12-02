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

print(max(checksums))
