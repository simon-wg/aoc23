with open("day4/input.txt", "r") as f:
    text = f.readlines()

help_text = []

row_map = {}

for line in text:
    day = int(line.split(":")[0].split(" ")[-1])
    right_hand_side = line.split(":")[1].strip()
    row_map[day] = right_hand_side


for row in row_map:
    left_right = {"left": [], "right": []}
    left = [x.strip() for x in row_map[row].split(" | ")[0].split(" ") if x != ""]
    right = [x.strip() for x in row_map[row].split(" | ")[1].split(" ") if x != ""]
    left_right["left"] = left
    left_right["right"] = right
    row_map[row] = left_right

points = 0

rows_left = list(row_map.keys())
rows_left.reverse()

# Part 1: 2 ** (count - 1) if count > 0 else 0
while rows_left:
    count = 0
    curr_row = rows_left.pop()
    point_cards = row_map.get(curr_row).get("left")
    owned_cards = row_map.get(curr_row).get("right")
    for point_card in point_cards:
        if point_card in owned_cards:
            count += 1
    points += 2 ** (count - 1) if count > 0 else 0

print(points)

# Part 2: Electric boogaloo
rows_left = list(row_map.keys())
rows_left.reverse()
total_added = len(rows_left)
while rows_left:
    count = 0
    curr_row = rows_left.pop()
    point_cards = row_map.get(curr_row).get("left")
    owned_cards = row_map.get(curr_row).get("right")
    for point_card in point_cards:
        if point_card in owned_cards:
            count += 1
    rows_to_add = [
        curr_row + x for x in range(1, count + 1) if curr_row + x <= len(row_map)
    ]
    rows_left += rows_to_add
    total_added += len(rows_to_add)

print(total_added)
