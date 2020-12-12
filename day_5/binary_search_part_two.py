from binary_search_part_one import ingest_file, extract_position_from_id

if __name__ == "__main__":
    seat_ids = ingest_file()
    ids = []
    for seat_id in seat_ids:
        row = extract_position_from_id(
            seat_id=seat_id[:7], upper_bound_character="F", lower_bound_character="B", range_to_search=range(128))
        column = extract_position_from_id(
            seat_id=seat_id[7:], upper_bound_character="L", lower_bound_character="R", range_to_search=range(8))
        ids.append(row * 8 + column)
    for id in ids:
        if id + 1 not in ids and id + 2 in ids:
            missing = id + 1
    print(missing)
