def invalid_sum(r):
    ids = [int(i) for i in r.split('-')]

    sum_p1 = 0
    sum_p2 = 0 
    for i in range(ids[0], ids[-1]+1):
        if check_invalid_part1(i):
           sum_p1 += i
        if check_invalid_part2(i):
            sum_p2 += i

    return sum_p1, sum_p2

def check_invalid_part1(i):
    i = str(i)
    window = int(len(i) / 2)
    if i[:window] == i[window:]:
        return True
    else:
        return False

def check_invalid_part2(i):
    i = str(i)
    window_max = int(len(i) / 2)

    # loop over window sizes between 1 and window_max
    for w_size in range(1, window_max+1):
        if len(i) % w_size != 0:
            continue

        if check_window_p2(i, w_size):
            return True
        else:
            continue
    return False

def check_window_p2(id, w_size):
    for w in range(0, len(id)-1*w_size, w_size):
        if id[w:w+w_size] != id[w+w_size:w+2*w_size]:
            return False
    return True

if __name__ == '__main__':
    with open('input.txt') as inf:
        data = inf.read().splitlines()

    ranges = data[0].split(',')

    sum_p1 = 0 
    sum_p2 = 0

    for r in ranges:
        p1, p2 = invalid_sum(r)
        sum_p1 += p1
        sum_p2 += p2

    print('Part 1:', sum_p1)
    print('Part 2:', sum_p2)