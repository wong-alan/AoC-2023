from collections import deque
from typing import TextIO
from utils import timed
from pprint import pprint

moves = {
    "N": (-1, 0),  # Up
    "W": (0, -1),  # Left
    "S": (1, 0),   # Down
    "E": (0, 1)    # Right
}
reflect_slash = {
    "N": "E",
    "W": "S",
    "S": "W",
    "E": "N"
}
reflect_backslash = {
    "N": "W",
    "W": "N",
    "S": "E",
    "E": "S"
}


def move_beam(coords, direction, grid):
    next_moves = []
    space = grid[coords[0]][coords[1]]

    if space == ".":
        next_moves = [(tuple((sum(x) for x in zip(coords, moves[direction]))), direction)]
    elif space == "/":
        direction = reflect_slash[direction]
        next_moves = [(tuple((sum(x) for x in zip(coords, moves[direction]))), direction)]
    elif space == "\\":
        direction = reflect_backslash[direction]
        next_moves = [(tuple((sum(x) for x in zip(coords, moves[direction]))), direction)]
    elif space == "|":
        if direction == "N" or direction == "S":
            next_moves = [(tuple((sum(x) for x in zip(coords, moves[direction]))), direction)]
        else:
            north = (tuple((sum(x) for x in zip(coords, moves["N"]))), "N")
            south = (tuple((sum(x) for x in zip(coords, moves["S"]))), "S")
            next_moves = [north, south]
    elif space == "-":
        if direction == "W" or direction == "E":
            next_moves = [(tuple((sum(x) for x in zip(coords, moves[direction]))), direction)]
        else:
            west = (tuple((sum(x) for x in zip(coords, moves["W"]))), "W")
            east = (tuple((sum(x) for x in zip(coords, moves["E"]))), "E")
            next_moves = [west, east]

    return next_moves


def calc_energized(start_coords, start_dir, grid) -> int:
    seen_list = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    energized = set()
    next_spaces = deque([(start_coords, start_dir)])

    while len(next_spaces):
        coordinates, direction = next_spaces.popleft()
        # If the beam leaves the grid
        if coordinates[0] < 0 or coordinates[0] >= len(grid) \
                or coordinates[1] < 0 or coordinates[1] >= len(grid):
            # Grid is a square
            continue
        # Check if we've been here
        if direction in seen_list[coordinates[0]][coordinates[1]]:
            continue
        else:
            energized.add(coordinates)
            seen_list[coordinates[0]][coordinates[1]].append(direction)
        next_spaces.extend(move_beam(coordinates, direction, grid))

    return len(energized)


@timed
def part_one(text: TextIO) -> int:
    grid = []
    for line in text:
        grid.append(line)

    return calc_energized((0, 0), "E", grid)


# Could memoize some results to optimize
@timed
def part_two(text: TextIO) -> int:
    grid = []
    for line in text:
        grid.append(line)

    # Use len(grid) in all directions since grid is a square
    max_north = max([calc_energized((0, i), "S", grid) for i in range(len(grid))])
    max_south = max([calc_energized((len(grid) - 1, i), "N", grid) for i in range(len(grid))])
    max_east = max([calc_energized((i, len(grid) - 1), "W", grid) for i in range(len(grid))])
    max_west = max([calc_energized((i, 0), "E", grid) for i in range(len(grid))])

    return max(max_north, max_south, max_east, max_west)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
