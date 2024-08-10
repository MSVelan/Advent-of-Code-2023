with open("./Day3/input.txt") as f:
    data = f.readlines()

with open("./Day3/input.txt") as f:
    whole_data = f.read()

special_char_positions = []

special_chars = set()
for c in whole_data:
    if c not in ".0123456789":
        if c != "\n":
            special_chars.add(c)

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in special_chars:
            special_char_positions.append((i, j))

adj_del_pos = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
number_positions_start = set()
for pos in special_char_positions:
    x, y = pos[0], pos[1]
    for del_pos in adj_del_pos:
        new_x = x + del_pos[0]
        new_y = y + del_pos[1]
        if 0 <= new_x < len(data) and 0 <= new_y < len(data[new_x]):
            if data[new_x][new_y].isdigit():  # means its a number
                temp_y = new_y
                while 0 <= temp_y < len(data[new_x]) and data[new_x][temp_y].isdigit():
                    temp_y -= 1
                temp_y += 1
                number_positions_start.add((new_x, temp_y))

part_sum = 0
for pos in number_positions_start:
    s = ""
    x, y = pos[0], pos[1]
    while 0 <= y < len(data[x]) and data[x][y].isdigit():
        s += data[x][y]
        y += 1
    part_sum += int(s)

print(part_sum)
