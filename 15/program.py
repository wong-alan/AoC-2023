from collections import OrderedDict
from typing import TextIO
from utils import timed


@timed
def part_one(text: TextIO) -> int:
    sequence = text.readline()
    steps = sequence.split(",")

    total = 0
    for step in steps:
        total += calc_hash(step)
    return total


def calc_hash(label: str) -> int:
    result = 0
    for char in label:
        result += ord(char)
        result *= 17
        result %= 256
    return result


@timed
def part_two(text: TextIO) -> int:
    sequence = text.readline()
    steps = sequence.split(",")

    # { 0 : { ab: 1 , cd: 2 } }
    # Box 0 has lens ab (focal length 1) and lens cd (focal length 2)
    boxes: OrderedDict[int, OrderedDict[str, int]] = OrderedDict((i, OrderedDict()) for i in range(256))

    for step in steps:
        if "=" in step:
            label, focus = step.split("=")
            box = calc_hash(label)
            boxes[box][label] = int(focus)
        else:  # - in steps
            label = step.rstrip("-")
            box = calc_hash(label)
            boxes[box].pop(label, None)

    total = 0
    for box, lenses in boxes.items():
        for slot, length in enumerate(lenses.values()):
            total += (box + 1) * (slot + 1) * length

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
