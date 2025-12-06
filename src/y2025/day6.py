import math


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def col_transpose(lines: list[str]) -> list[list[str]]:
    columns = []
    for col_idx in reversed(range(len(lines[0]))):
        col = []
        for row in lines:
            col.append(row[col_idx])

        columns.append(col)

    operands = []
    result = []
    for col in [*columns, [""]]:  # one extra col to flush
        number_str = "".join(col[:-1]).strip()
        operator = col[-1]
        if number_str != "":
            operands.append(number_str)
        if operator in ("+", "*"):
            operands.append(operator)

        if number_str == "":
            result.append(operands)
            operands = []

    return result


def calc(problem: list[str]) -> int:
    operation = problem[-1]
    operands = [int(x) for x in problem[:-1]]

    match operation:
        case "+":
            return sum(operands)
        case "*":
            return math.prod(operands)
        case _:
            raise ValueError(f"Unknown operation: {operation}")


def solve_a(lines: list[str]) -> int:
    matrix = [line.split() for line in lines]
    transposed = transpose(matrix)
    return sum([calc(col) for col in transposed])


def solve_b(lines: list[str]) -> int:
    transposed = col_transpose(lines)
    return sum([calc(col) for col in transposed])
