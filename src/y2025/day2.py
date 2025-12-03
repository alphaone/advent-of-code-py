def solve_a(id_ranges):
    invalid = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        start = int(start)
        end = int(end)

        for id in range(start, end + 1):
            if is_invalid_a(str(id)):
                invalid += id
    return invalid


def is_invalid_a(part):
    length = len(part)
    first_half = part[: length // 2]
    last_half = part[length // 2 :]
    return first_half == last_half


def solve_b(id_ranges):
    invalid = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        start = int(start)
        end = int(end)

        for id in range(start, end + 1):
            if is_invalid_b(str(id)):
                invalid += id
    return invalid


def is_invalid_b(part):
    for chunk_length in range(len(part) // 2, 0, -1):
        if (len(part) % chunk_length) != 0:
            continue

        if inner(part, chunk_length):
            return True

    return False


def inner(part, chunk_length):
    first_chunk = part[:chunk_length]
    for i in range(chunk_length, len(part), chunk_length):
        if part[i : i + chunk_length] != first_chunk:
            return False

    return True
