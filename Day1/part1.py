with open("./input.txt") as f:
    data = f.read().strip().split("\n")

sum = 0
for line in data:
    n = len(line)
    start_dig = 0
    end_dig = 0
    for i in range(n):
        if line[i] in "0123456789":
            start_dig = int(line[i])
            break

    for i in range(n - 1, -1, -1):
        if line[i] in "0123456789":
            end_dig = int(line[i])
            break

    sum += start_dig * 10 + end_dig

print(sum)
