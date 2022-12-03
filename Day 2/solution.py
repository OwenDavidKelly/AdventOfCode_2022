f = open("C:/Users/owenk/Documents/AdventOfCode/Day 2/input.txt", "r")
score = 0
part2 = 0
for line in f:
    # Work out the winner
    opponent = line[0]
    you = line[2]
    # Opponent Chooses Rock
    if opponent == "A":
        # You choose paper
        if you == "Y":
            score += 8 #
            # Draw
            part2 += 3 + 1 
        # You choose Rock
        elif you == "X":
            score += 4
            # Lose
            part2 += 0 + 3
        # You choose Scissors
        elif you == "Z":
            score += 3
            # Win
            part2 += 6 + 2 
    # Opponent Chooses Paper
    elif opponent == "B":
        if you == "Y":
            score += 5
            # Draw
            part2 += 3 + 2 
        elif you == "X":
            score += 1
            # Lose
            part2 += 0 + 1 
        elif you == "Z":
            score += 9
            # Win
            part2 += 6 + 3 
    # Opponent Chooses Scissors 
    elif opponent == "C":
        if you == "Y":
            score += 2
            # Draw
            part2 += 3 + 3 
        if you == "X":
            score += 7
            # Lose
            part2 += 0 + 2 
        if you == "Z":
            score += 6 #
            # Win
            part2 += 6 + 1 
print(score)
print(part2)