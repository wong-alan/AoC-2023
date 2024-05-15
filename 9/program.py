import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text):
    total = 0

    def extrapolate_value(values):
        diff = [j - i for i, j in zip(values[:-1], values[1:])]
        if all(num == 0 for num in diff):
            return 0
        return diff[-1] + extrapolate_value(diff)

    for line in text:
        values = [int(num) for num in line.split()]
        total += values[-1] + extrapolate_value(values)

    return total


@timed
def part_two(text):
    total = 0

    def extrapolate_value(values):
        diff = [j - i for i, j in zip(values[:-1], values[1:])]
        if all(num == 0 for num in diff):
            return 0
        return diff[0] - extrapolate_value(diff)

    for line in text:
        values = [int(num) for num in line.split()]
        total += values[0] - extrapolate_value(values)

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
