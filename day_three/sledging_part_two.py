world_map = []
with open("map.txt") as raw_world_map:
    world_map = raw_world_map.read().splitlines()


movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total = 1
for move in movements:
    trees = 0
    row, column = 0, 0
    while row + 1 < len(world_map):
        row += move[1]
        column += move[0]

        location = world_map[row][column % len(world_map[row])]
        if location == "#":
            trees += 1
    total *= trees
print(total)
