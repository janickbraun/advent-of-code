with open("data.txt") as f:
    data = f.read()

doubles = []

for i, letter in enumerate(data):
    if i > 3:
        arr = data[i - 1] + data[i - 2] + data[i - 3] + letter
        right = 0
        for item in arr:
            if arr.count(item) == 1:
                right += 1
        if right == 4:
            print(i + 1, letter)
            break

