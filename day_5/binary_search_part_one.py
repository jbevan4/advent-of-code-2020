def ingest_file():
    with open("seats.txt") as seat_ids:
        return [seat_id.strip() for seat_id in seat_ids.readlines()]


def search_seat_row_from_id(seat_id):
    range_of_rows = range(128)
    for letter in seat_id[:7]:
        if letter == "F":
            range_of_rows = range_of_rows[:len(range_of_rows) // 2]
            continue
        if letter == "B":
            range_of_rows = range_of_rows[len(range_of_rows) // 2:]
    return range_of_rows[0]


def search_seat_column_from_id(seat_id):
    range_of_columns = range(8)
    for letter in seat_id[7:]:
        if letter == "L":
            range_of_columns = range_of_columns[:len(range_of_columns) // 2]
        if letter == "R":
            range_of_columns = range_of_columns[len(range_of_columns) // 2:]
    return range_of_columns[0]


if __name__ == "__main__":
    seat_ids = ingest_file()
    result = []
    curr_max = 0
    for seat_id in seat_ids:
        row = search_seat_row_from_id(seat_id)
        column = search_seat_column_from_id(seat_id)
        curr_max = max(curr_max, row * 8 + column)
    print(curr_max)
