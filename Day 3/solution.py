f = open("C:/Users/owenk/Documents/AdventOfCode/Day 3/input.txt", "r")
alpha = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
for line in f:
    items = line[:-1]
    first = items[:int(len(items)/2)]
    second = items[int(len(items)/2):]
    shared = ""
    for ind in first:
        if ind in second:
            shared = ind
    sum += alpha.index(shared)
print(sum)
f.close()

# Part 2

f = open("C:/Users/owenk/Documents/AdventOfCode/Day 3/input.txt", "r")
sum = 0
ruck_list = []
i = 0
for line in f:
    ruck_list.append(line[:-1])
    if i % 3 == 2:
        shared12 = ""
        for ind in ruck_list[0]:
            if ind in ruck_list[1]:
                shared12 = shared12 + ind
        shared123 = ""
        for ind in shared12:
            if ind in ruck_list[2]:
                shared123 = ind
        sum += alpha.index(shared123)
        ruck_list = []
    i += 1
print(sum)
    