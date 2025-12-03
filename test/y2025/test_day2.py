from src.y2025.day2 import is_invalid_a, is_invalid_b, solve_a, solve_b

example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"  # noqa: E501


def test_invalid_a():
    assert is_invalid_a("11") is True
    assert is_invalid_a("1188511885") is True
    assert is_invalid_a("222222") is True


def test_solve_a_example():
    assert solve_a(example_input.split(",")) == 1227775554


def test_solve_a():
    assert solve_a(open("resources/y2025/day2.txt").read().strip().split(",")) == 24043483400


def test_invalid_b():
    assert is_invalid_b("123123") is True
    assert is_invalid_b("38593859") is True
    assert is_invalid_b("21212121") is True
    assert is_invalid_b("11111") is True

    assert is_invalid_b("111112") is False
    assert is_invalid_b("123124") is False


def test_solve_b_example():
    assert solve_b(example_input.split(",")) == 4174379265


def test_solve_b():
    assert solve_b(open("resources/y2025/day2.txt").read().strip().split(",")) == 38262920235
