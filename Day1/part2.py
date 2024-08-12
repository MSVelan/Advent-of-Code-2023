with open("./Day1/input.txt") as f:
    data = f.read().strip().split("\n")

num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}
sum = 0
for line in data:
    n = len(line)
    start_dig = 0
    end_dig = 0
    for i in range(n):
        if line[i] in "0123456789":
            start_dig = int(line[i])
            break
        elif line[i : i + 3] in num_map:
            start_dig = num_map[line[i : i + 3]]
            break
        elif line[i : i + 4] in num_map:
            start_dig = num_map[line[i : i + 4]]
            break
        elif line[i : i + 5] in num_map:
            start_dig = num_map[line[i : i + 5]]
            break

    for i in range(n - 1, -1, -1):
        if line[i] in "0123456789":
            end_dig = int(line[i])
            break
        elif line[i - 2 : i + 1] in num_map:
            end_dig = num_map[line[i - 2 : i + 1]]
            break
        elif line[i - 3 : i + 1] in num_map:
            end_dig = num_map[line[i - 3 : i + 1]]
            break
        elif line[i - 4 : i + 1] in num_map:
            end_dig = num_map[line[i - 4 : i + 1]]
            break

    sum += start_dig * 10 + end_dig

print(sum)
