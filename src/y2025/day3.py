def joltage(bank: str, no_of_batteries=2) -> int:
    selected_batteries = []
    search_from = 0
    for i in range(no_of_batteries):
        batteries_left = no_of_batteries - i - 1

        # search in line, but leave space for remaining batteries
        found_on_idx = -1
        battery_value = 0
        for idx, c in enumerate(bank[search_from : len(bank) - (batteries_left)]):
            digit = int(c)
            if digit > battery_value:
                battery_value = digit
                found_on_idx = idx

        search_from = search_from + found_on_idx + 1

        selected_batteries.append(battery_value)

    return total_joltage_output(selected_batteries)


def total_joltage_output(batteries: list[int]) -> int:
    return sum(bv * (10**i) for i, bv in enumerate(reversed(batteries)))
