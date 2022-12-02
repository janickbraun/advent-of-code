with open("D:/Development/Python/Advent/2021/3/data.txt") as f:
    lines = f.read().splitlines()


"""
TODO: Clean up the code
"""

codeMatrix = []
for line in lines:
    code = []
    for char in line:
        code.append(int(char))
    codeMatrix.append(code)

gamma = []
epsilon = []

for bit_num in range(0, 12):
    counter1 = 0
    counter0 = 0

    for code in codeMatrix:
        if code[bit_num] == 1:
            counter1 += 1
        elif code[bit_num] == 0:
            counter0 += 1

    if counter1 > counter0:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

    print(counter0, counter1)

gamma_rate = int("".join([str(bit) for bit in gamma]), 2)
epsilon_rate = int("".join([str(bit) for bit in epsilon]), 2)

print("Power consumption:", gamma_rate*epsilon_rate)