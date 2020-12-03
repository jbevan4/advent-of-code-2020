from sledging_part_one import ingest_file, traverse_world
from math import prod

if __name__ == "__main__":
    world_map = ingest_file()
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(prod(traverse_world(world_map, row_adjustment=column,
                              column_adjustment=row) for row, column in movements))
