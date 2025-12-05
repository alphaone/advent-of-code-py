from src.y2025.day4 import is_accessible, solve_a, solve_b

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_is_accessible():
    example_map: list[str] = [line for line in example.splitlines()]

    assert is_accessible(example_map, 0, 2) is True
    assert is_accessible(example_map, 1, 0) is True
    assert is_accessible(example_map, 1, 1) is False


def test_solve_a_example():
    example_map: list[str] = [line for line in example.splitlines()]

    assert solve_a(example_map) == 13


def test_solve_a():
    map = [line for line in open("resources/y2025/day4.txt").read().splitlines()]
    assert solve_a(map) == 1569


def test_solve_b_example():
    example_map: list[str] = [line for line in example.splitlines()]
    assert solve_b(example_map) == 43


def test_solve_b():
    map = [line for line in open("resources/y2025/day4.txt").read().splitlines()]
    assert solve_b(map) == 9280
