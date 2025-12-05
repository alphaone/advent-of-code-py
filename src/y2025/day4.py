def neighbors(map: list[str], row: int, col: int) -> list[tuple[int, int]]:
    deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    result = []
    for dx, dy in deltas:
        nx, ny = row + dx, col + dy
        if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
            result.append((nx, ny))
    return result


def count_paperrolls(map: list[str], row: int, col: int) -> int:
    return sum(1 for nx, ny in neighbors(map, row, col) if map[nx][ny] == "@")


def is_accessible(map: list[str], row: int, col: int) -> bool:
    return count_paperrolls(map, row, col) < 4


def remove_paperrolls(map: list[str]) -> tuple[list[str], int]:
    removed = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == "@" and is_accessible(map, row, col):
                removed.append([row, col])

    for row, col in removed:
        map[row] = map[row][:col] + "x" + map[row][col + 1 :]

    return map, len(removed)


def solve_a(map: list[str]) -> int:
    _, no_accessible = remove_paperrolls(map)
    return no_accessible


def solve_b(map: list[str]) -> int:
    no_removed = 0
    while True:
        map, removed = remove_paperrolls(map)
        no_removed += removed
        if removed == 0:
            break

    return no_removed
