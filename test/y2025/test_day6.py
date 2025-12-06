from src.y2025.day6 import calc, col_transpose, solve_a, solve_b, transpose

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_transpose():
    matrix = [
        ["123", "328", "51", "64"],
        ["45", "64", "387", "23"],
        ["6", "98", "215", "314"],
        ["*", "+", "*", "+"],
    ]

    expected = [
        ["123", "45", "6", "*"],
        ["328", "64", "98", "+"],
        ["51", "387", "215", "*"],
        ["64", "23", "314", "+"],
    ]

    actual = transpose(matrix)
    assert actual == expected


def test_col_transpose():
    input = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]
    expected = [
        ["4", "431", "623", "+"],
        ["175", "581", "32", "*"],
        ["8", "248", "369", "+"],
        ["356", "24", "1", "*"],
    ]
    actual = col_transpose(input)
    assert actual == expected


def test_calc():
    assert calc(["123", "45", "6", "*"]) == 33210
    assert calc(["328", "64", "98", "+"]) == 490
    assert calc(["51", "387", "215", "*"]) == 4243455
    assert calc(["64", "23", "314", "+"]) == 401


def test_solve_a_example():
    assert solve_a(example.strip().splitlines()) == 4277556


def test_solve_a():
    assert solve_a(open("resources/y2025/day6.txt").read().strip().splitlines()) == 4387670995909


def test_solve_b_example():
    assert solve_b(example.splitlines()) == 3263827


def test_solve_b():
    assert solve_b(open("resources/y2025/day6.txt").read().splitlines()) == 9625320374409
