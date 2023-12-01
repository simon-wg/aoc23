# Description: Advent of Code - Day 1 - Part 1

# Read input from file
with open("./day1/input.txt", "r") as file:
    text = file.read()

sum = 0

for line in text.splitlines():
    left_ptr = 0
    right_ptr = len(line) - 1
    while left_ptr <= right_ptr:
        if ord(line[left_ptr]) >= 48 and ord(line[left_ptr]) <= 57:
            if ord(line[right_ptr]) >= 48 and ord(line[right_ptr]) <= 57:
                sum += int(line[left_ptr] + line[right_ptr])
                break
            else:
                right_ptr -= 1
        else:
            left_ptr += 1

print(sum)

# Description: Advent of Code - Day 1 - Part 2

dict_of_alphanumbers = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum = 0

# The lettered numbers are between 3 and 5 characters long

for line in text.splitlines():
    [left_ptr, right_ptr] = [0, len(line)]
    # Find the first lettered number or numeral
    key_number = []
    while True:
        if ord(line[left_ptr]) >= 48 and ord(line[left_ptr]) <= 57:
            key_number.append(line[left_ptr])
            break
        if line[left_ptr : left_ptr + 3] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[left_ptr : left_ptr + 3]))
            break
        if line[left_ptr : left_ptr + 4] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[left_ptr : left_ptr + 4]))
            break
        if line[left_ptr : left_ptr + 5] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[left_ptr : left_ptr + 5]))
            break
        left_ptr += 1
    # Find the right-side lettered number or numeral
    while True:
        if ord(line[right_ptr - 1]) >= 48 and ord(line[right_ptr - 1]) <= 57:
            key_number.append(line[right_ptr - 1])
            break
        if line[right_ptr - 3 : right_ptr] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[right_ptr - 3 : right_ptr]))
            break
        if line[right_ptr - 4 : right_ptr] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[right_ptr - 4 : right_ptr]))
            break
        if line[right_ptr - 5 : right_ptr] in dict_of_alphanumbers:
            key_number.append(dict_of_alphanumbers.get(line[right_ptr - 5 : right_ptr]))
            break
        right_ptr -= 1

    print(line, int("".join(key_number)))
    sum += int("".join(key_number))

print(sum)
