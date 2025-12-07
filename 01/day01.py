def process_move(position, move):
    direction = move[0]
    val = int(move[1:])

    p1 = position

    if direction == 'R':
        times_passed_zero = int((val + position)/100)
        position += val
    elif direction == 'L':
        if val >= position and position > 0:
            
            if val < 100:
                times_passed_zero = 1
            else:
                times_passed_zero = int((val - position)/100)
        else:
            times_passed_zero = 0
        position -= val
    else:
        raise SyntaxError(f'Unknown instruction {direction}')

    return position % 100, times_passed_zero



if __name__ == '__main__':
    with open('input.txt') as inf:
        data = inf.read().splitlines()

    dial_position = 50
    password_p1 = 0
    password_p2 = 0

    print('Init:', dial_position)

    for move in data:
        dial_position, times_passed_zero = process_move(dial_position, move)
        print(move, dial_position, times_passed_zero)
        
        #part1
        password_p1 += 1 if dial_position == 0 else 0
        password_p2 += times_passed_zero
    print('Part 1:', password_p1)
    print('Part 2:', password_p2)