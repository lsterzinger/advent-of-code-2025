def find_joltage_part1(battery: str) -> int:

    val1, i = find_largest_digit_pair(battery[:-1])
    val2, _ = find_largest_digit_pair(battery[i+1:])
    return int(val1 + val2)


def find_largest_digit_pair(series: str) -> tuple[str, int]:

    # get first value
    reference_val = 0
    reference_i = 0
    for i, val in enumerate(series):
        if int(val) > reference_val:
            reference_val = int(val)
            reference_i = i
    return str(reference_val), reference_i


if __name__ == '__main__':
    with open('sample_input.txt') as inf:
        batteries = inf.read().splitlines()

    total_joltage_p1 = 0

    for battery in batteries:
        joltage_p1 = find_joltage_part1(battery)
        total_joltage_p1 += joltage_p1

    print(total_joltage_p1)
