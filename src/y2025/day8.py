import math

type coord = tuple[int, int, int]


def parse(line: str) -> coord:
    x, y, z = line.split(",")
    return int(x), int(y), int(z)


def dist(c1: coord, c2: coord) -> float:
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


def shortest_distances(lines: list[str]) -> list[tuple[coord, coord]]:
    coords: list[coord] = []
    for line in lines:
        c = parse(line)
        coords.append(c)

    distances: list[tuple[float, coord, coord]] = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            c1 = coords[i]
            c2 = coords[j]
            d = dist(c1, c2)
            distances.append((d, c1, c2))

    sorted_distances = sorted(distances, key=lambda x: x[0])

    return [(coord1, coord2) for _, coord1, coord2 in sorted_distances]


def solve_a(lines: list[str], n: int) -> int:
    dists = shortest_distances(lines)[:n]

    circuits: list[set[coord]] = []
    for coord1, coord2 in dists:
        if {coord1} not in circuits:
            circuits.append({coord1})
        if {coord2} not in circuits:
            circuits.append({coord2})

    for coord1, coord2 in dists:
        circuit1 = next((x for x in circuits if coord1 in x), None)
        circuit2 = next((x for x in circuits if coord2 in x), None)

        if circuit1 and circuit2 and circuit1 == circuit2:
            continue
        if circuit1 and circuit2 and circuit1 != circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

    lengths = [len(circuit) for circuit in circuits]
    return math.prod(sorted(lengths, reverse=True)[:3])


def solve_b(lines: list[str]) -> int:
    dists = shortest_distances(lines)

    circuits: list[set[coord]] = []
    for coord1, coord2 in dists:
        if {coord1} not in circuits:
            circuits.append({coord1})
        if {coord2} not in circuits:
            circuits.append({coord2})

    for coord1, coord2 in dists:
        circuit1 = next((x for x in circuits if coord1 in x), None)
        circuit2 = next((x for x in circuits if coord2 in x), None)

        if circuit1 and circuit2 and circuit1 == circuit2:
            continue
        if circuit1 and circuit2 and circuit1 != circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

        if len(circuits) == 1:
            print(coord1, coord2)
            return coord1[0] * coord2[0]

    raise ValueError("Could not connect all circuits")
