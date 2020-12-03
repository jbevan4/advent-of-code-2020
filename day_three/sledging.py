world_map = []
with open("map.txt") as raw_world_map:
    world_map = raw_world_map.read().splitlines()

trees = 0
row, column = 0, 0
while row + 1 < len(world_map):
    row += 1
    column += 3

    location = world_map[row][column % len(world_map[row])]
    if location == "#":
        trees += 1
print(trees)
