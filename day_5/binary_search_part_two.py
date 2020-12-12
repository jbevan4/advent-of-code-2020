from binary_search_part_one import ingest_file, extract_position_from_id

if __name__ == "__main__":
    seat_ids = ingest_file()
    ids = []
    curr_max = 0
    curr_min = float("inf")
    for seat_id in seat_ids:
        row = extract_position_from_id(
            seat_id=seat_id[:7], upper_bound_character="F", lower_bound_character="B", range_to_search=range(128))
        column = extract_position_from_id(
            seat_id=seat_id[7:], upper_bound_character="L", lower_bound_character="R", range_to_search=range(8))
        ids.append(row * 8 + column)
        curr_max = max(curr_max, row * 8 + column)
        curr_min = min(curr_min, row * 8 + column)
    set_of_ids_over_range = set(range(curr_min, curr_max + 1))
    missing = set_of_ids_over_range - set(ids)
    print(missing)
