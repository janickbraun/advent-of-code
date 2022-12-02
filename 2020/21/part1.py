from colorama import Fore

with open("data.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    unknownOld = line.split("(")[0]
    unknown = unknownOld.split(" ")
    unknown.pop()
    knownOld = line.split("contains ")[1]
    knownOld = knownOld.replace(")", "")
    known = knownOld.split(", ")

    print(unknown, known)

print(f"{Fore.RED}coded by Janick")
