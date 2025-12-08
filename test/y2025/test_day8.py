from src.y2025.day8 import parse, shortest_distances, solve_a, solve_b

example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


def test_parse():
    assert parse("12,34,56") == (12, 34, 56)


def test_shortest_distances_example():
    dists = shortest_distances(example.strip().splitlines())[:2]
    assert dists[0] == ((162, 817, 812), (425, 690, 689))
    assert dists[1] == ((162, 817, 812), (431, 825, 988))


def test_solve_a_example():
    lines = example.strip().splitlines()

    assert solve_a(lines, 10) == 40


def test_solve_a():
    lines = open("resources/y2025/day8.txt").read().strip().splitlines()

    assert solve_a(lines, 1000) == 57970


def test_solve_b_example():
    lines = example.strip().splitlines()

    assert solve_b(lines) == 25272


def test_solve_b():
    lines = open("resources/y2025/day8.txt").read().strip().splitlines()

    assert solve_b(lines) == 8520040659
