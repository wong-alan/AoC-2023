import re
from functools import reduce


def part_one(text):
    game_id_sum = 0
    maximum = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in text:
        impossible = False
        parts = re.split(":|;|,", line)

        for cubes in parts[1:]:
            num, color = cubes.strip(" \n").split(" ")
            if int(num) > maximum[color]:
                impossible = True
                break

        if impossible:
            continue

        game_id_sum += int(parts[0].split(" ")[1])
    return game_id_sum


def part_two(text):
    total_power = 0
    key = {
        "red": 0,
        "green": 1,
        "blue": 2
    }

    for line in text:
        minimum = [1, 1, 1]  # red, green, blue
        parts = re.split(":|;|,", line)

        for cubes in parts[1:]:
            num, color = cubes.strip(" \n").split(" ")
            if int(num) > minimum[key[color]]:
                minimum[key[color]] = int(num)

        total_power += reduce(lambda x, y: x * y, minimum)
    return total_power


with open("input.txt", "r") as file:
    answer_one = part_one(file)

with open("input.txt", "r") as file:
    answer_two = part_two(file)

print(f"One: {answer_one} \nTwo: {answer_two}")
