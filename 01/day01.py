def process_move(position, move):
    
    # Get direction and movement amount
    direction = move[0]
    val = int(move[1:])

    # set move increment based on direction
    if direction == 'R':
        move = 1
    else:
        move = -1


    # count the # of times it passes 0
    zero_counter = 0

    # process individual moves
    for i in range(1, val+1):
        position += move # Move position by one

        # if move puts position at -1 or 100, adjust accordingly
        if position == 100:
            position = 0
        elif position == -1:
            position = 99

        # count zeros (part 2)
        if position == 0:
            zero_counter += 1

    return position, zero_counter 

if __name__ == '__main__':
    with open('input.txt') as inf:
        data = inf.read().splitlines()

    dial_position = 50
    password_p1 = 0
    password_p2 = 0

    print('Init:', dial_position)

    for move in data:
        dial_position, zeros = process_move(dial_position, move)
        
        #part1
        password_p1 += 1 if dial_position == 0 else 0
        password_p2 += zeros

    print('Part 1:', password_p1)
    print('Part 2:', password_p2)