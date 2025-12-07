def beams_step(line: str, beams: list[int]) -> tuple[list[int], int]:
    splits = 0

    new_beams = beams.copy()
    for i, (c, b) in enumerate(zip(line, beams)):
        if c == "^" and b > 0:
            splits += 1
            new_beams[i - 1] += new_beams[i]
            new_beams[i + 1] += new_beams[i]
            new_beams[i] = 0

    return new_beams, splits


def solve_a(lines: list[str]) -> int:
    beams = [0] * len(lines[0])
    beams[lines[0].index("S")] = 1
    total_splits = 0

    for line in lines[1:]:
        beams, splits = beams_step(line, beams)
        total_splits += splits

    return total_splits


def solve_b(lines: list[str]) -> int:
    beams = [0] * len(lines[0])
    beams[lines[0].index("S")] = 1

    for line in lines[1:]:
        beams, _ = beams_step(line, beams)

    return sum(beams)
