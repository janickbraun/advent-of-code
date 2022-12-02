with open("data.txt") as f:
    lines = f.read().splitlines()

player1 = []
player2 = []
lineIndex = 0
for line in lines:
    if line == "":
        player1 = lines[1:lineIndex]
        player2 = lines[lineIndex + 2:len(lines)]
    lineIndex += 1


def game():
    if len(player1) == 0 or len(player2) == 0:
        return
    if int(player1[0]) > int(player2[0]):
        player1.append(player1[0])
        player1.append(player2[0])
        player1.pop(0)
        player2.pop(0)
    elif int(player2[0]) > int(player1[0]):
        player2.append(player2[0])
        player2.append(player1[0])
        player2.pop(0)
        player1.pop(0)


while True:
    if len(player1) == 0 or len(player2) == 0:
        break
    game()
    print(player1, player2)

senke = 0

if player1:
    print("player 1 won")
    multi = len(player1)
    for num in player1:
        senke += int(num) * multi
        multi -= 1
elif player2:
    print("player 2 won")
    multi = len(player2)
    for num in player2:
        senke += int(num) * multi
        multi -= 1

print(senke)