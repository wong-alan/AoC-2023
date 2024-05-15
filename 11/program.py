import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text):
    space = [[char for char in line] for line in text]
    galaxies = []
    seen_rows = set()
    seen_columns = set()
    seen_space = {0: seen_rows, 1: seen_columns}
    for row_idx, row in enumerate(space):
        for col_idx, col in enumerate(row):
            if col == '#':
                galaxies.append((row_idx, col_idx))
                seen_rows.add(row_idx)
                seen_columns.add(col_idx)
    total_path = 0
    for gal_idx, galaxy_1 in enumerate(galaxies):
        for galaxy_2 in galaxies[gal_idx + 1:]:
            path = 0
            for i in range(2):
                small = min(galaxy_1[i], galaxy_2[i])
                large = max(galaxy_1[i], galaxy_2[i])
                path += large-small
                seen = seen_space[i]
                for space in range(small, large):
                    if space not in seen:
                        path += 1
            total_path += path
    return total_path


@timed
def part_two(text):
    space = [[char for char in line] for line in text]
    galaxies = []
    seen_rows = set()
    seen_columns = set()
    seen_space = {0: seen_rows, 1: seen_columns}
    for row_idx, row in enumerate(space):
        for col_idx, col in enumerate(row):
            if col == '#':
                galaxies.append((row_idx, col_idx))
                seen_rows.add(row_idx)
                seen_columns.add(col_idx)
    total_path = 0
    for gal_idx, galaxy_1 in enumerate(galaxies):
        for galaxy_2 in galaxies[gal_idx + 1:]:
            path = 0
            for i in range(2):
                small = min(galaxy_1[i], galaxy_2[i])
                large = max(galaxy_1[i], galaxy_2[i])
                path += large-small
                seen = seen_space[i]
                for space in range(small, large):
                    if space not in seen:
                        path += 999_999
            total_path += path
    return total_path


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
