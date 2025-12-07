from src.y2025.day7 import beams_step, solve_a, solve_b

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def test_beams():
    assert beams_step("......^.^......", [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]) == (
        [0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0],
        2,
    )
    assert beams_step(".....^.^.^.....", [0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0]) == (
        [0, 0, 0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 0, 0, 0],
        3,
    )


def test_solve_a_example():
    lines = example.splitlines()
    assert solve_a(lines) == 21


def test_solve_a():
    lines = open("resources/y2025/day7.txt").read().splitlines()
    assert solve_a(lines) == 1579


def test_solve_b_example():
    lines = example.splitlines()
    assert solve_b(lines) == 40


def test_solve_b():
    lines = open("resources/y2025/day7.txt").read().splitlines()
    assert solve_b(lines) == 13418215871354
