def find_joltage_part1(battery_bank: str) -> int:
    val1, i = find_largest_digit(battery_bank[:-1])
    val2, _ = find_largest_digit(battery_bank[i + 1 :])
    return int(val1 + val2)


def find_joltage_part2(battery_bank: str, bank_lenth: int) -> int:
    digits = []
    cursor = 0
    for i in range(bank_lenth, 0, -1):
        print(i)
        print(battery_bank)
        start = ' ' * cursor
        end = ' ' * (i-1)
        print(start + '^' + end + '^')
        joltage, location = find_largest_digit(battery_bank[cursor:-i])
        cursor += location + 1
        digits.append(joltage)
    
    print(digits)
    return int("".join(digits))


def find_largest_digit(series: str) -> tuple[str, int]:
    # get first value
    reference_val = 0
    reference_i = 0
    for i, val in enumerate(series):
        if int(val) > reference_val:
            reference_val = int(val)
            reference_i = i
    return str(reference_val), reference_i


if __name__ == "__main__":
    with open("sample_input.txt") as inf:
        batteries = inf.read().splitlines()

    total_joltage_p1 = 0
    total_joltage_p2 = 0

    for battery in batteries:
        joltage_p1 = find_joltage_part1(battery)
        joltage_p2 = find_joltage_part2(battery, 12)
        total_joltage_p1 += joltage_p1
        total_joltage_p2 += joltage_p2

    print(total_joltage_p1)
    print(total_joltage_p2)
