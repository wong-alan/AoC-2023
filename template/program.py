from typing import TextIO
from utils import timed


@timed
def part_one(text: TextIO) -> int:
    for line in text:
        break
    return 0


@timed
def part_two(text: TextIO) -> int:
    for line in text:
        break
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
