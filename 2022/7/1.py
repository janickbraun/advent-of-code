with open("data.txt") as f:
    lines = f.read().splitlines()
    lines.pop(0)

currentDirectory = "/"
directories = []
sizes = []
deep = 0
for line in lines:
    if line.startswith("$"):
        command = line.split("$ ")[1]
        if command.startswith("cd"):
            folder = command.split(" ")[1]
            if folder == "..":
                deep -= 1
                if deep == 0:
                    currentDirectory = "/"
                else:
                    currentDirectory = directories[0][-1]
            else:
                if deep == 0:
                    directories.append([folder])
                elif deep == 1:
                    directories[-1].append([folder])
                elif deep == 2:
                    directories[-1][-1].append([folder])
                elif deep == 3:
                    directories[-1][-1][-1].append([folder])
                elif deep == 4:
                    directories[-1][-1][-1][-1].append([folder])
                elif deep == 5:
                    directories[-1][-1][-1][-1][-1].append([folder])

                currentDirectory = folder

                deep += 1
    elif line.split(" ")[0] != "dir":
        sizes.append([currentDirectory, line.split(" ")[0]])

print(directories)
print(sizes)

dirSizes = []

cache = ["/", 0]
for size in sizes:
    if cache[0] == size[0]:
        cache[1] += int(size[1])
    else:
        dirSizes.append(cache)
        cache = [size[0], int(size[1])]

dirSizes.append(cache)

for size in dirSizes:
    if round(size[1]/100000, 1) == 1.0:
        print("dsada")

for directory in directories:
    print(directory)

print(dirSizes)


