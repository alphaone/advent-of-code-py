type coord = tuple[int, int]


def parse(line: str) -> coord:
    x, y = line.split(",")
    return int(x), int(y)


def dist(c1: coord, c2: coord) -> int:
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


def largest_distances(coords: list[coord]) -> list[tuple[int, coord, coord]]:
    distances: list[tuple[int, coord, coord]] = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            c1 = coords[i]
            c2 = coords[j]
            d = dist(c1, c2)
            distances.append((d, c1, c2))

    sorted_distances = sorted(distances, key=lambda x: x[0], reverse=True)

    return sorted_distances


def solve_a(lines: list[str]) -> int:
    coords = [parse(line) for line in lines]

    dists = largest_distances(coords)
    return dists[0][0]
