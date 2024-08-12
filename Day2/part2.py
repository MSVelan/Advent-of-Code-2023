with open("./Day2/input.txt") as f:
    data = f.readlines()

res = 0
for line in data:
    valid = 1
    line_split = line.split(":")
    gameNo = line_split[0]
    trials = line_split[1]
    gameNo = int(gameNo.split(" ")[1])
    trial_split = trials.split(";")
    maxr, maxb, maxg = 0, 0, 0
    for trial in trial_split:
        rgb = trial.split(",")
        r = 0
        g = 0
        b = 0
        for x in rgb:
            x = x.strip()
            color_split = x.split(" ")
            n_color = color_split[0]
            color = color_split[1]
            if color == "red":
                r = int(n_color)
            elif color == "green":
                g = int(n_color)
            elif color == "blue":
                b = int(n_color)
        maxr = max(maxr, r)
        maxb = max(maxb, b)
        maxg = max(maxg, g)
    power_of_cube = maxr * maxb * maxg
    res += power_of_cube

print(res)
