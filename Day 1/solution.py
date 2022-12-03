f = open("C:/Users/owenk/Documents/AdventOfCode/Day 1/input.txt", "r")
cals = [0]
for line in f:
    if len(line) > 2:
        cals[-1] = cals[-1] + int(line)
    else:
        cals.append(0)
cals.sort()
print(cals[-1])
print(sum(cals[-3:]))