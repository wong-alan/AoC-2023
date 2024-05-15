import copy
from typing import TextIO, Tuple, List
from itertools import chain
import operator
import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text: TextIO) -> int:
    platform = []
    rocks = []
    for row, line in enumerate(text):
        text_line = []
        for col, char in enumerate(line.rstrip()):
            text_line.append(char)
            if char == 'O':
                rocks.append([row, col])
        platform.append(text_line)

    # Because of how we created the rocks list, all upper rocks will roll first
    for rock in rocks:
        while rock[0] > 0 and platform[rock[0] - 1][rock[1]] == '.':
            platform[rock[0] - 1][rock[1]] = 'O'
            platform[rock[0]][rock[1]] = '.'
            rock[0] -= 1

    return sum(len(platform) - row for row, _ in rocks)


@timed
def part_two(text: TextIO) -> int:
    cycle_limit = 1_000_000_000
    platform = []
    rocks = []
    for row, line in enumerate(text):
        text_line = []
        for col, char in enumerate(line.rstrip()):
            text_line.append(char)
            if char == 'O':
                rocks.append([row, col])
        platform.append(text_line)

    roll = {  # Rock roll direction
        "N": (-1,  0), # Up
        "W": ( 0, -1), # Left
        "S": ( 1,  0), # Down
        "E": ( 0,  1)  # Right
    }
    order = {  # Rock traversal order
        # For [N, W] iterate forwards, ie top-down, left to right
        # For [S, E] iterate backwards, ie bottom-up, right to left
        "N":  1, "W":  1,
        "S": -1, "E": -1
    }
    axis = {  # 0 = row, 1 = col
        "N": 0, "W": 1,
        "S": 0, "E": 1
    }
    edge = { # Platform is a square
        "N": 0,
        "W": 0,
        "S": -(len(platform) - 1),
        "E": -(len(platform) - 1)
    }

    def roll_rocks(rocks: List[List[int]], platform: List[List[str]], direction: str):
        row_dir, col_dir = roll[direction]
        roll_axis = axis[direction]
        limit = edge[direction]
        sign = order[direction]

        for rock in rocks[::order[direction]]:
            # N,W: rock > 0
            # S,E: rock < edge => -rock > -edge
            while rock[roll_axis]*sign > limit \
                    and platform[rock[0] + row_dir][rock[1] + col_dir] == '.':
                platform[rock[0] + row_dir][rock[1] + col_dir] = 'O'
                platform[rock[0]][rock[1]] = '.'
                rock[roll_axis] += -1 * sign
        # Rocks can change order
        rocks.sort(key = operator.itemgetter(0, 1))

    # Keep a list to detect cycle
    platform_map = {stringify(platform): 0}
    platform_list = [copy.deepcopy(platform)]
    loop_start, loop_end = 0, 0
    cycle = ["N", "W", "S", "E"]

    for i in range(1, cycle_limit + 1):
        for direction in cycle:
            roll_rocks(rocks, platform, direction)
        platform_list.append(copy.deepcopy(platform))

        platform_str = stringify(platform)
        if platform_str in platform_map:
            loop_start = platform_map[platform_str]
            loop_end = i
            break
        platform_map[platform_str] = i
        if i == cycle_limit:
            break

    # Calculate final platform state from cycle length
    zero = loop_start - 1 # Assume cycle doesn't start at 0
    cycle_length = loop_end - loop_start
    offset = (cycle_limit - zero) % cycle_length
    final_index = zero + offset if offset != 0 else zero + cycle_length
    final_platform = platform_list[final_index]

    return sum(row.count("O") * (len(final_platform) - i) for i, row in enumerate(final_platform))

# Lists are not hashable, so we need to convert the platform
def stringify(platform: List[List[str]]):
    return "".join(chain.from_iterable(platform))

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
