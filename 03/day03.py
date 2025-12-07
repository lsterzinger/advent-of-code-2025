def get_battery_largest_joltage(battery, bank_len):
    vals = []
    for b in range(bank_len):
        val, i = find_largest_value(battery[:-1])
        battery = battery[i+1:]

def find_largest_value(series):
    # get first value
    reference_val = 0
    reference_i = 0 
    for i, val in enumerate(series):
        if int(val) > reference_val:
            reference_val = int(val)
            reference_i = i
    return str(reference_val), reference_i


if __name__ == '__main__':
    with open('input.txt') as inf:
        batteries = inf.read().splitlines()

    total_joltage = 0
    for battery in batteries:
        joltage = get_battery_largest_joltage(battery)
        total_joltage += joltage
    print(total_joltage)