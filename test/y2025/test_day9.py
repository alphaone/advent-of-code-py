from src.y2025.day9 import largest_distances, parse, solve_a

example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_largest_distances():
    lines = example.strip().splitlines()
    coords = [parse(line) for line in lines]
    assert [
        (50, (11, 1), (2, 5)),
        (50, (11, 7), (2, 3)),
        (40, (9, 7), (2, 3)),
    ] == largest_distances(coords)[:3]


def test_solve_a_example():
    lines = example.strip().splitlines()

    assert solve_a(lines) == 50


def test_solve_a():
    lines = open("resources/y2025/day9.txt").read().strip().splitlines()

    assert solve_a(lines) == 4761736832
