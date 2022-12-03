with open("data.txt") as f:
    lines = f.read().splitlines()

rockOpponent = "A"
paperOpponent = "B"
scissorsOpponent = "C"

loseMe = "X"
drawMe = "Y"
winMe = "Z"

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

    #win me
    if me is winMe:
        finalScore += winPoints
        if opponent is rockOpponent:
            finalScore += paperPoints
        elif opponent is paperOpponent:
            finalScore += scissorsPoints
        elif opponent is scissorsOpponent:
            finalScore += rockPoints

    #draw me
    elif me is drawMe:
        finalScore += drawPoints
        if opponent is rockOpponent:
            finalScore += rockPoints
        elif opponent is paperOpponent:
            finalScore += paperPoints
        elif opponent is scissorsOpponent:
            finalScore += scissorsPoints

    #lose me
    elif me is loseMe:
        if opponent is rockOpponent:
            finalScore += scissorsPoints
        elif opponent is paperOpponent:
            finalScore += rockPoints
        elif opponent is scissorsOpponent:
            finalScore += paperPoints

print(finalScore)
