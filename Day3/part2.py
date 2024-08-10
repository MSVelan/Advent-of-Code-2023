with open("./Day3/input.txt") as f:
    data = f.readlines()

with open("./Day3/input.txt") as f:
    whole_data = f.read()

star_positions = []

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "*":
            star_positions.append((i, j))

adj_del_pos = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
total_gear_ratio = 0

for pos in star_positions:
    x, y = pos[0], pos[1]
    temp_number_positions = set()
    for del_pos in adj_del_pos:
        new_x = x + del_pos[0]
        new_y = y + del_pos[1]
        if 0 <= new_x < len(data) and 0 <= new_y < len(data[new_x]):
            if data[new_x][new_y].isdigit():  # means its a number
                temp_y = new_y
                while 0 <= temp_y < len(data[new_x]) and data[new_x][temp_y].isdigit():
                    temp_y -= 1
                temp_y += 1
                temp_number_positions.add((new_x, temp_y))

    if len(temp_number_positions) != 2:
        continue

    temp_number_positions = list(temp_number_positions)

    first_no_x, first_no_y = (
        temp_number_positions[0][0],
        temp_number_positions[0][1],
    )
    second_no_x, second_no_y = (
        temp_number_positions[1][0],
        temp_number_positions[1][1],
    )

    s1 = ""
    while (
        0 <= first_no_y < len(data[first_no_x])
        and data[first_no_x][first_no_y].isdigit()
    ):
        s1 += data[first_no_x][first_no_y]
        first_no_y += 1
    s1 = int(s1)

    s2 = ""
    while (
        0 <= second_no_y < len(data[second_no_x])
        and data[second_no_x][second_no_y].isdigit()
    ):
        s2 += data[second_no_x][second_no_y]
        second_no_y += 1

    s2 = int(s2)

    total_gear_ratio += s1 * s2

print(total_gear_ratio)
