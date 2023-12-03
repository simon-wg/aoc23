

with open("./day2/input.txt") as f:
  text = f.readlines()



sum = 0
def checker(line):
  max_vals = {
  "blue": 14,
  "green": 13,
  "red": 12,
  }
  game, sets = line.split(": ")
  game = game.split(" ")[1]
  sets = sets.split("; ")
  for set in sets:
    colors_count = {cv[1].strip(): int(cv[0].strip()) for cv in [pairs.split(" ") for pairs in set.split(", ")]}
    if not all(colors_count.get(color) <= max_vals.get(color) for color in colors_count):
      return 0
  return int(game)

for line in text:
  sum += checker(line)

print(sum)

def max_checker(line):
  max_vals = {
    "blue": 0,
    "green": 0,
    "red": 0,
  }
  game, sets = line.split(": ")
  game = game.split(" ")[1]
  sets = sets.split("; ")
  for set in sets:
    colors_count = {cv[1].strip(): int(cv[0].strip()) for cv in [pairs.split(" ") for pairs in set.split(", ")]}
    for color in colors_count:
      if colors_count[color] > max_vals[color]:
        max_vals[color] = colors_count[color]
    product = 1
  for color in max_vals:
    product *= max_vals[color]
  return product


power = 0

for line in text:
  test_vals = max_checker(line)
  power += test_vals



print(power)





