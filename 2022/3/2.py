with open("data.txt") as f:
    lines = f.read().splitlines()

groups = []
group = []

for line in lines:
    group.append(line)
    if len(group) == 3:
        groups.append(group)
        group = []

doubles = []

for group in groups:
    double = []
    for i in range(len(group[0])):
        if group[0][i] in group[1] and group[0][i] in group[2]:
            double.append(group[0][i])
    for i in range(len(group[1])):
        if group[1][i] in group[0] and group[1][i] in group[2]:
            double.append(group[1][i])
    if len(double) != 0:
        doubles.append(double[0])

score = 0

for double in doubles:
    if double.islower():
        score += ord(double) - 96
    elif double.isupper():
        score += ord(double) - 38

print(score)
