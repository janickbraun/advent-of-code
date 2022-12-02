with open("data.txt") as f:
    lines = f.read().splitlines()

rockOpponent = "A"
paperOpponent = "B"
scissorsOpponent = "C"

rockMe = "X"
paperMe = "Y"
scissorsMe = "Z"

rockPoints = 1
paperPoints = 2
scissorsPoints = 3

drawPoints = 3
winPoints = 6

games = []

for line in lines:
    games.append(line.split(" "))

finalScore = 0

for game in games:
    opponent = game[0]
    me = game[1]

    #genaral points
    if me is rockMe:
        finalScore += rockPoints
    elif me is paperMe:
        finalScore += paperPoints
    elif me is scissorsMe:
        finalScore += scissorsPoints

    #draw points
    if me is rockMe and opponent is rockOpponent:
        finalScore += 3
    elif me is paperMe and opponent is paperOpponent:
        finalScore += 3
    elif me is scissorsMe and opponent is scissorsOpponent:
        finalScore += 3

    #win points
    if me is rockMe and opponent is scissorsOpponent:
        finalScore += 6
    elif me is paperMe and opponent is rockOpponent:
        finalScore += 6
    elif me is scissorsMe and opponent is paperOpponent:
        finalScore += 6

print(finalScore)
