with open("data.txt") as f:
    lines = f.read().splitlines()

def splitString(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

backpacks = []

for line in lines:
    backpacks.append(splitString(line))

doubles = []

for backpack in backpacks:
    double = []
    for i in range(len(backpack[0])):
        if backpack[0][i] in backpack[1]:
            double.append(backpack[0][i])
    if len(double) != 0:
        doubles.append(double[0])

score = 0

for double in doubles:
    if double.islower():
        score += ord(double) - 96
    elif double.isupper():
        score += ord(double) - 38

print(score)
