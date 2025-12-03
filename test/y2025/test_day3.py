from src.y2025.day3 import joltage

example_input = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_joltage():
    assert joltage("987654321111111") == 98
    assert joltage("811111111111119") == 89
    assert joltage("234234234234278") == 78

    assert joltage("987654321111111", 12) == 987654321111
    assert joltage("811111111111119", 12) == 811111111119
    assert joltage("234234234234278", 12) == 434234234278


def test_solve_a_example():
    lines = example_input.strip().splitlines()
    results = [joltage(line) for line in lines]
    assert sum(results) == 357


def test_solve_a():
    lines = open("resources/y2025/day3.txt").read().strip().splitlines()
    results = [joltage(line) for line in lines]
    assert sum(results) == 17229


def test_solve_b_example():
    lines = example_input.strip().splitlines()
    results = [joltage(line, 12) for line in lines]
    assert sum(results) == 3121910778619


def test_solve_b():
    lines = open("resources/y2025/day3.txt").read().strip().splitlines()
    results = [joltage(line, 12) for line in lines]
    assert sum(results) == 170520923035051
