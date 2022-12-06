with open("data.txt") as f:
    data = f.read()

doubles = []

for i, letter in enumerate(data):
    if i > 13:
        arr = data[i - 1] + data[i - 2] + data[i - 3] + letter + data[i - 4] + data[i - 5] + data[i - 6] + data[i - 7] + data[i - 8] + data[i - 9] + data[i - 10] + data[i - 11] + data[i - 12] + data[i - 13]
        right = 0
        for item in arr:
            if arr.count(item) == 1:
                right += 1
        if right == 14:
            print(i + 1, letter)
            break

