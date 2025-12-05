from src.y2025.day5 import fresh, merge_ranges, parse_lists, solve_a, solve_b

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_parse_lists():
    assert parse_lists(example) == (
        [
            (3, 5),
            (10, 14),
            (16, 20),
            (12, 18),
        ],
        [1, 5, 8, 11, 17, 32],
    )


def test_fresh():
    ranges, _ = parse_lists(example)

    assert fresh(1, ranges) == []
    assert fresh(5, ranges) == [(3, 5)]
    assert fresh(8, ranges) == []
    assert fresh(11, ranges) == [(10, 14)]
    assert fresh(17, ranges) == [(16, 20), (12, 18)]
    assert fresh(32, ranges) == []


def test_merge_ranges():
    ranges = [(3, 5), (10, 14), (12, 18), (16, 20)]
    assert merge_ranges(ranges) == [(3, 5), (10, 20)]

    assert merge_ranges([(10, 30), (50, 80)]) == [(10, 30), (50, 80)]
    assert merge_ranges([(10, 90), (20, 80)]) == [(10, 90)]
    assert merge_ranges([(10, 50), (20, 80)]) == [(10, 80)]
    assert merge_ranges([(30, 50), (20, 80)]) == [(20, 80)]
    assert merge_ranges([(30, 90), (20, 80)]) == [(20, 90)]


def test_solve_a_example():
    assert solve_a(example) == 3


def test_solve_a():
    assert solve_a(open("resources/y2025/day5.txt").read()) == 664


def test_solve_b_example():
    assert solve_b(example) == 14


def test_solve_b():
    assert solve_b(open("resources/y2025/day5.txt").read()) == 350780324308385
