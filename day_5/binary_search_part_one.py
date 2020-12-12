def ingest_file():
    with open("seats.txt") as seat_ids:
        return [seat_id.strip() for seat_id in seat_ids.readlines()]


def extract_position_from_id(seat_id, upper_bound_character, lower_bound_character, range_to_search):
    for letter in seat_id:
        if letter == upper_bound_character:
            range_to_search = range_to_search[:len(range_to_search) // 2]
        if letter == lower_bound_character:
            range_to_search = range_to_search[len(range_to_search) // 2:]
    return range_to_search[0]


if __name__ == "__main__":
    seat_ids = ingest_file()
    curr_max = 0
    for seat_id in seat_ids:
        row = extract_position_from_id(
            seat_id=seat_id[:7], upper_bound_character="F", lower_bound_character="B", range_to_search=range(128))
        column = extract_position_from_id(
            seat_id=seat_id[7:], upper_bound_character="L", lower_bound_character="R", range_to_search=range(8))
        curr_max = max(curr_max, row * 8 + column)
    print(curr_max)
