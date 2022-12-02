with open("data.txt") as f:
    lines = f.read().splitlines()

prevSum = None
counterIncrease = 0
counterIndex = 0

for oldLine in lines:
    line = int(oldLine)
    try:
        if prevSum is None:
            prevSum = line + int(lines[counterIndex + 1]) + int(lines[counterIndex + 2])
        elif prevSum < line + int(lines[counterIndex + 1]) + int(lines[counterIndex + 2]):
            counterIncrease += 1
        prevSum = line + int(lines[counterIndex + 1]) + int(lines[counterIndex + 2])
        counterIndex += 1
    except Exception as e:
        print(e)


print(counterIncrease)