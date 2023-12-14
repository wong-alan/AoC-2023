import re
from functools import cache
from typing import TextIO

from utils import timed


@timed
def part_one(text: TextIO) -> int:
    total_arrangements = 0

    def count_arrangements(symbols: str, groups: list[int]):
        if '?' in groups:
            return count_arrangements(symbols.replace('?', '.', 1), groups) + \
                count_arrangements(symbols.replace('?', '#', 1), groups)
        else:
            if groups == [len(group) for group in re.findall(r"#+", symbols)]:
                return 1
            return 0
        pass

    for line in text:
        symbols, groups = line.split()
        groups = [int(group) for group in groups.split(',')]
        total_arrangements += count_arrangements(symbols, groups)

    return total_arrangements


@timed
def part_two(text: TextIO) -> int:
    total_arrangements = 0
    @cache
    def count_arrangements(symbols: str, groups: tuple):
        if len(groups) == 0:
            return 1 if '#' not in symbols else 0

        min_group_start = 0
        max_group_start = len(symbols) - sum(groups) - len(groups) + 1
        if '#' in symbols:
            max_group_start = min(symbols.index('#'), max_group_start)

        first_group_size, *remaining_groups = groups
        arrangements = 0
        for start in range(min_group_start, max_group_start + 1):  # sliding window
            end = start + first_group_size
            group = symbols[start:end]

            is_group_possible = all(char in '#?' for char in group)
            is_end_of_record = end >= len(symbols)
            is_group_separated = is_end_of_record or symbols[end] in '.?'
            if not is_group_possible or not is_group_separated:
                continue

            remaining_symbols = symbols[end + 1:]
            arrangements += count_arrangements(remaining_symbols, tuple(remaining_groups))
        return arrangements

    for line in text:
        symbols, groups = line.split()
        symbols = '?'.join(symbols for _ in range(5))
        groups = ','.join(groups for _ in range(5))
        groups = tuple(int(group) for group in groups.split(','))  # use a tuple for cache, since lists are not hashable

        total_arrangements += count_arrangements(symbols, groups)
    return total_arrangements


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
