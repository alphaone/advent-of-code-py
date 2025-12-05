def parse_lists(lines) -> tuple[list[tuple[int, int]], list[int]]:
    parts = lines.split("\n\n")
    ranges = [parse_range(line.strip()) for line in parts[0].splitlines()]

    return ranges, [int(x) for x in parts[1].splitlines()]


def parse_range(line: str) -> tuple[int, int]:
    start, end = line.split("-")
    return int(start), int(end)


def fresh(ingredient: int, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    fresh_ranges = []

    for start, end in ranges:
        if start <= ingredient <= end:
            fresh_ranges.append((start, end))

    return fresh_ranges


def solve_a(input: str) -> int:
    ranges, ingredients = parse_lists(input)

    return sum(1 for ingredient in ingredients if len(fresh(ingredient, ranges)) > 0)


def solve_b(input: str) -> int:
    ranges, _ = parse_lists(input)
    return sum(end - start + 1 for start, end in merge_ranges(ranges))


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return merged
