f = open("C:/Users/owenk/Documents/AdventOfCode/Day 4/input.txt", "r")
full = 0
overlap = 0
for line in f:
    pair = line[:-1]
    ranges = pair.split(",")
    first = ranges[0].split("-")
    second = ranges[1].split("-")
    first_min = int(first[0])
    first_max = int(first[1])
    second_min = int(second[0])
    second_max = int(second[1])
    if first_min >= second_min and first_max <= second_max:
        full += 1
    elif first_min <= second_min and first_max >= second_max:
        full += 1
    if first_min <= second_min and first_max >= second_min:
        overlap += 1
    elif second_min <= first_min and second_max >= first_min:
        overlap += 1
print(full)
print(overlap)