numbers = [38, 54, 68, 93, 72, 12, 33, 8, 98, 88, 21, 91, 53, 61, 26, 36, 18, 80, 73, 47, 3, 5, 55, 92, 67, 52, 25, 40,
           56, 95, 9, 62, 30, 31, 85, 65, 14, 2, 78, 75, 15, 39, 87, 27, 58, 42, 60, 32, 41, 83, 51, 77, 10, 66, 70, 4,
           37, 6, 89, 23, 16, 49, 48, 63, 94, 97, 86, 64, 74, 82, 7, 0, 11, 71, 44, 43, 50, 69, 45, 81, 20, 28, 46, 79,
           90, 34, 35, 96, 99, 59, 1, 76, 22, 24, 17, 57, 13, 19, 84, 29]

boards = []

with open("D:/Development/Python/Advent/2021/4/input.txt") as f:
    board = f.read().split("\n\n")
    board2 = []
    for i in board:
        board2.append(i.split("\n"))

    board3 = []
    for i in board2:
        b = []
        for j in i:
            b.append(j.split(" "))

        for k in b:
            for f in k:
                if f == '':
                    k.remove(f)
        board3.append(b)

    boards = board3
winning_board = []
winning_counter = 0
winning_number = 0

for board in boards:
    rows = [0, 0, 0, 0, 0]
    columns = [0, 0, 0, 0, 0]
    counter = 0
    running = True
    for i in numbers:
        if not running:
            break
        for row in range(0, len(board)):
            if not running:
                break

            for column in range(0, len(board[row])):
                if not running:
                    break

                if int(board[row][column]) == i:
                    rows[row] += 1
                    columns[column] += 1

                    for j in rows:
                        if j == 5:
                            running = False
                            if winning_counter == 0:
                                winning_counter = counter
                                winning_number = i
                            elif counter > winning_counter:
                                winning_counter = counter
                                winning_board = board
                                winning_number = i
                            break

                    for j in columns:
                        if j == 5:
                            running = False
                            if winning_counter == 0:
                                winning_counter = counter
                                winning_number = i
                            elif counter > winning_counter:
                                winning_counter = counter
                                winning_board = board
                                winning_number = i
                            break

        counter += 1

print(winning_board)
print(winning_number)
running2 = True
for k in numbers:
    if not running2:
        break
    for i in winning_board:
        if not running2:
            break
        for j in i:
            if int(j) == k:
                i.remove(j)
                if k == winning_number:
                    running2 = False
                    break

sum = 0
for i in winning_board:
    for j in i:
        sum += int(j)

print(winning_board)
print(sum)
print(sum * winning_number)
