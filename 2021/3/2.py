def byte_to_int(str):
    result = 0
    for i in range(0, len(str)):
        if str[i] == "0":
            result += 0
        elif str[i] == "1":
            result += pow(2, len(str) - 1 - i)

    return result

numbers = []
numbers2 = []
with open("D:/Development/Python/Advent/2021/3/data.txt") as f:
    numbers = f.readlines()
    numbers2 = numbers

for i in range(0, 12):
    counter0 = 0
    counter1 = 0
    zeros = []
    ones = []
    for j in numbers:
        if j[i] == "1":
            ones.append(j)
            counter1 += 1
        elif j[i] == "0":
            zeros.append(j)
            counter0 += 1

    if counter0 > counter1:
        numbers = zeros
    elif counter1 > counter0:
        numbers = ones
    else:
        numbers = ones

for i in range(0, 12):

    if(len(numbers2) == 1):
        break;

    counter0 = 0
    counter1 = 0
    zeros = []
    ones = []
    for j in numbers2:
        if j[i] == "1":
            ones.append(j)
            counter1 += 1
        elif j[i] == "0":
            zeros.append(j)
            counter0 += 1


    if counter0 < counter1:
        numbers2 = zeros
    elif counter1 < counter0:
        numbers2 = ones
    else:
        numbers2 = zeros


print(byte_to_int(numbers[0].split("\n")[0]) * byte_to_int(numbers2[0].split("\n")[0]))