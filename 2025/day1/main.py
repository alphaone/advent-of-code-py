import re


def solve_A(lines):
    current = 50
    zeros = 0
    for line in lines:
        current = turn(line, current)
        if current == 0:
            zeros += 1

    return zeros


def turn(line, current):
    match = re.match(r"([LR])(\d+)", line)
    if not match:
        return current

    parts = match.groups()
    dir, dist = parts[0], int(parts[1])

    if dir == "L":
        dist = -dist

    return (current + dist) % 100


def solve_B(lines):
    current = 50
    passed_zeros = 0
    for line in lines:
        count, current = turn_and_count_passed_zeros(line, current)
        passed_zeros += count

    return passed_zeros


def turn_and_count_passed_zeros(line, current):
    match = re.match(r"([LR])(\d+)", line)
    if not match:
        return 0, current

    parts = match.groups()
    dir, dist = parts[0], int(parts[1])

    passed_zeros = dist // 100  # full cycles
    dist = dist % 100

    if dir == "L":
        dist = -dist

    new_current = current + dist
    if (new_current <= 0 or new_current >= 100) and current != 0:
        passed_zeros += 1

    return passed_zeros, new_current % 100
