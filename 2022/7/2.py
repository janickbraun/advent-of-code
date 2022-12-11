with open("data.txt", "r") as f:
    terminal = f.read().split("\n")

current_dir = ""
size_of_dirs = []
for i in terminal:
    if i.startswith("$ cd"):
        if i.rsplit(" ", 1)[1] != "..":
            current_dir = current_dir + i.rsplit(" ", 1)[1].strip() + " "
        else:
            current_dir = current_dir[:-(len(current_dir.rstrip().rsplit(" ", 1)[1]) + 1)]
    elif not i.startswith("$ ls"):
        index = [j for j, e in enumerate(size_of_dirs) if e[0] == current_dir.rstrip()]
        if i.startswith("dir"):
            if len(index) == 0:
                size_of_dirs.append((current_dir.rstrip(), ["size_" + current_dir + i.rsplit(" ", 1)[1]]))
            else:
                size_of_dirs[index[0]][1].append("size_" + current_dir + i.rsplit(" ", 1)[1])
        else:
            if len(index) == 0:
                size_of_dirs.append((current_dir.rstrip(), [i.split(" ", 1)[0]]))
            else:
                size_of_dirs[index[0]][1].append(i.split(" ", 1)[0])

size_of_dirs = list(reversed(size_of_dirs))

while True:
    ind = [j for j, e in enumerate(size_of_dirs) if isinstance(e[1], list)]
    if len(ind) == 0:
        break

    for index, i in enumerate(size_of_dirs):
        if isinstance(i[1], list) and not any("size" in s for s in i[1]):
            size_of_dirs[index] = (i[0], sum(list(map(int, i[1]))))
        elif isinstance(i[1], list):
            indices = [j for j, e in enumerate(i[1]) if e.split("_", 1)[0] == "size"]
            for k in indices:
                index2 = [j for j, e in enumerate(size_of_dirs) if e[0] == i[1][k].split("_", 1)[1]][0]
                if isinstance(size_of_dirs[index2][1], list):
                    if not any("size" in s for s in size_of_dirs[index2][1]):
                        i[1][k] = str(sum(list(map(int, size_of_dirs[index2][1]))))
                else:
                    i[1][k] = str(size_of_dirs[index2][1])

for index, i in enumerate(size_of_dirs):
    if isinstance(i[1], list):
        size_of_dirs[index] = (i[0], sum(list(map(int, i[1]))))

to_delete = 30_000_000 - (70_000_000 - int(size_of_dirs[-1][1]))

smallest_file = 0
for i in size_of_dirs:
    if to_delete <= int(i[1]):
        if smallest_file == 0 or smallest_file > int(i[1]):
            smallest_file = i[1]

print(smallest_file)