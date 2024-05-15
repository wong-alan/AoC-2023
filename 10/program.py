from utils import timed


@timed
def part_one(text):
    row, column = None, None
    pipes = [[char for char in line.rstrip()] for line in text]
    for i, line in enumerate(pipes):
        for j, char in enumerate(line):
            if char == 'S':
                row, column = i, j
                break
        if row:
            break

    north = {'|': 'N',
             '7': 'W',
             'F': 'E',
             'S': None}
    south = {'|': 'S',
             'J': 'W',
             'L': 'E',
             'S': None}
    east = {'-': 'E',
            '7': 'S',
            'J': 'N',
            'S': None}
    west = {'-': 'W',
            'F': 'S',
            'L': 'N',
            'S': None}

    direction = None
    if pipes[max(row - 1, 0)][column] in ['|', '7', 'F']:
        direction = 'N'
    elif pipes[min(row + 1, len(pipes[0]) - 1)][column] in ['|', 'L', 'J']:
        direction = 'S'
    elif pipes[row][max(column - 1, 0)] in ['-', 'L', 'F']:
        direction = 'E'
    # "Unnecessary" since the pipe is connected on 2 sides, we are guaranteed to find a connected side in 3 checks
    # elif pipes[row][min(column + 1, len(pipes) - 1)] in ['-', 'J', '7']:
    #     direction = 'W'

    steps = 0
    curr_symbol = None
    prev_dir = direction
    while curr_symbol != 'S':
        match direction:
            case 'N':
                row -= 1
                prev_dir = north
            case 'S':
                row += 1
                prev_dir = south
            case 'E':
                column += 1
                prev_dir = east
            case 'W':
                column -= 1
                prev_dir = west

        curr_symbol = pipes[row][column]
        direction = prev_dir[curr_symbol]
        steps += 1

    return steps / 2


@timed
def part_two(text):
    row, column = None, None
    pipes = [[char for char in line.rstrip()] for line in text]
    for i, line in enumerate(pipes):
        for j, char in enumerate(line):
            if char == 'S':
                row, column = i, j
                break
        if row:
            break

    north = {'|': 'N',
             '7': 'W',
             'F': 'E',
             'S': None}
    south = {'|': 'S',
             'J': 'W',
             'L': 'E',
             'S': None}
    east = {'-': 'E',
            '7': 'S',
            'J': 'N',
            'S': None}
    west = {'-': 'W',
            'F': 'S',
            'L': 'N',
            'S': None}

    direction = None
    first_north = False
    if pipes[max(row - 1, 0)][column] in ['|', '7', 'F']:
        direction = 'N'
        first_north = True
    elif pipes[min(row + 1, len(pipes[0]) - 1)][column] in ['|', 'L', 'J']:
        direction = 'S'
    elif pipes[row][max(column - 1, 0)] in ['-', 'L', 'F']:
        direction = 'E'
    # "Unnecessary" since the pipe is connected on 2 sides, we are guaranteed to find a connected side in 3 checks
    # elif pipes[row][min(column + 1, len(pipes) - 1)] in ['-', 'J', '7']:
    #     direction = 'W'

    main_loop = {}
    curr_symbol = None
    prev_dir = direction
    while curr_symbol != 'S':
        main_loop[(row, column)] = True
        match direction:
            case 'N':
                row -= 1
                prev_dir = north
            case 'S':
                row += 1
                prev_dir = south
            case 'E':
                column += 1
                prev_dir = east
            case 'W':
                column -= 1
                prev_dir = west

        curr_symbol = pipes[row][column]
        direction = prev_dir[curr_symbol]
    if first_north:
        pipes[row][column] = '|'

    area = 0
    for r_idx, row in enumerate(pipes):
        is_inside = False
        for c_idx, column in enumerate(row):
            if main_loop.get((r_idx, c_idx), False):
                if column in ['|', 'L', 'J']:
                    is_inside = not is_inside
            elif is_inside:
                # pipes[r_idx][c_idx] = 'O'
                area += 1
            # else:
                # pipes[r_idx][c_idx] = ' '
    # for row in pipes:
    #     print(''.join(row))
    return area


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
