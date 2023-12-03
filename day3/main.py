# Read input file
with open("day3/input.txt", "r") as f:
    text = f.readlines()

# Remove new line characters
text = [x.strip() for x in text]


def get_surrounding_symbols(left_index, right_index, curr_row):
    above = max(curr_row - 1, 0)
    below = min(curr_row + 1, len(text) - 1)
    left = max(left_index - 1, 0)
    right = min(right_index + 1, len(text[0]) - 1)
    row_above = text[above][left:right]
    row_below = text[below][left:right]
    symbol_set = set(row_above + row_below + text[curr_row][left:right])
    symbol_set_without_number_chars = set(
        symbol_set.difference(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    )

    return symbol_set_without_number_chars


sum_of_all = 0
for index, line in enumerate(text):
    l_ptr = 0
    while l_ptr < len(line):
        while l_ptr < len(line) and not line[l_ptr].isdigit():
            l_ptr += 1
        r_ptr = l_ptr + 1
        while r_ptr < len(line) and line[r_ptr].isdigit():
            r_ptr += 1
        surrounding = get_surrounding_symbols(l_ptr, r_ptr, index)
        if len(surrounding) > 1:
            sum_of_all += int(line[l_ptr:r_ptr])
        l_ptr = r_ptr + 1

print(sum_of_all)

# Part 2


# Getting the surrounding symbols is the same as part 1, but this time we want to check if the symbol set contains numbers
def get_surrounding_numbers(index: int, curr_row: str, row_index: int) -> list[int]:
    # Check above row for numbers
    numbers = []
    if row_index > 0:
        above = text[row_index - 1][index - 1 : index + 2]
        if any(char.isdigit() for char in above):
            if not above[1].isdigit():
                # Possible split number
                if above[0].isdigit():
                    numbers += [scan_horizontal(index - 1, text[row_index - 1])]
                if above[2].isdigit():
                    numbers += [scan_horizontal(index + 1, text[row_index - 1])]
            else:
                numbers += [scan_horizontal(index, text[row_index - 1])]

    # Check below row for numbers
    if row_index < len(text) - 1:
        below = text[row_index + 1][index - 1 : index + 2]
        if any(char.isdigit() for char in below):
            if not below[1].isdigit():
                # Possible split number
                if below[0].isdigit():
                    numbers += [scan_horizontal(index - 1, text[row_index + 1])]
                if below[2].isdigit():
                    numbers += [scan_horizontal(index + 1, text[row_index + 1])]
            else:
                numbers += [scan_horizontal(index, text[row_index + 1])]

    if index > 0:
        left = curr_row[index - 1]
        if left.isdigit():
            numbers += [scan_horizontal(index - 1, curr_row)]
    if index < len(curr_row) - 1:
        right = curr_row[index + 1]
        if right.isdigit():
            numbers += [scan_horizontal(index + 1, curr_row)]
    print(numbers)
    print(above)
    print(curr_row[index - 1 : index + 2])
    print(below)
    return numbers


def scan_horizontal(index: int, curr_row: str) -> list[int]:
    right = []
    left = []
    original_index = index
    index += 1
    while index < len(curr_row) and curr_row[index].isdigit():
        right.append(curr_row[index])
        index += 1
    index = original_index - 1
    while index >= 0 and curr_row[index].isdigit():
        left.append(curr_row[index])
        index -= 1
    left.reverse()
    print(left)
    print(curr_row[original_index])
    print(right)
    return int("".join(left + [curr_row[original_index]] + right))


# If we find an * we want to check if the surrounding symbols contain numbers
sum_of_ratios = 0
for index, line in enumerate(text):
    ptr = 0
    while ptr < len(line):
        if line[ptr] == "*":
            surrounding = get_surrounding_numbers(ptr, line, index)
            if surrounding is not None and len(surrounding) > 1:
                sum_of_ratios += surrounding[0] * surrounding[1]
        ptr += 1

print(sum_of_ratios)
