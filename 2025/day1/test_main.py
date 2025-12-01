from main import turn_and_count_passed_zeros, solve_B, solve_A


def test_turn_and_count_passed_zeros():
    assert turn_and_count_passed_zeros("L68", 50) == (1, 82)
    assert turn_and_count_passed_zeros("L30", 82) == (0, 52)
    assert turn_and_count_passed_zeros("R48", 52) == (1, 0)
    assert turn_and_count_passed_zeros("L5", 0) == (0, 95)
    assert turn_and_count_passed_zeros("R60", 95) == (1, 55)
    assert turn_and_count_passed_zeros("L55", 55) == (1, 0)
    assert turn_and_count_passed_zeros("L1", 0) == (0, 99)
    assert turn_and_count_passed_zeros("L99", 99) == (1, 0)
    assert turn_and_count_passed_zeros("R14", 0) == (0, 14)
    assert turn_and_count_passed_zeros("L82", 14) == (1, 32)


example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_solve_A_example():
    zeros = solve_A(example_input.splitlines())
    assert zeros == 3


def test_solve_A():
    zeros = solve_A(open("2025/day1/input.txt").read().splitlines())
    assert zeros == 1147


def test_solve_B_example():
    passed_zeros = solve_B(example_input.splitlines())
    assert passed_zeros == 6


def test_solve_B():
    passed_zeros = solve_B(open("2025/day1/input.txt").read().splitlines())
    assert passed_zeros == 6789
