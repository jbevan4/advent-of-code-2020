def ingest_file():
    with open("map.txt") as raw_world_map:
        return raw_world_map.read().splitlines()


def traverse_world(world_map, row_adjustment=1, column_adjustment=3):
    trees = 0
    row, column = 0, 0
    while row + 1 < len(world_map):
        row += row_adjustment
        column += column_adjustment
        location = world_map[row][column % len(world_map[row])]
        if location == "#":
            trees += 1
    return trees


if __name__ == "__main__":
    world_map = ingest_file()
    print(traverse_world(world_map))
