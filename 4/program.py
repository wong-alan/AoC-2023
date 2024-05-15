import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text):
    total_score = 0
    for line in text:
        game = line.split(":")[1]
        winning_nums, nums = game.split("|")
        winning_nums = winning_nums.split()
        nums = nums.split()
        matches = sum([1 if num in winning_nums else 0 for num in nums])
        if matches:
            total_score += 2**(matches-1)
    return total_score


@timed
def part_two(text):
    games = []
    for line in text:
        game = line.split(":")[1]
        winning_nums, nums = game.split("|")
        winning_nums = winning_nums.split()
        nums = nums.split()
        games.append(sum([1 if num in winning_nums else 0 for num in nums]))
    copies = [1] * len(games)
    for i in range(len(games)):
        for j in range(games[i]):
            # Does not check if we run over copies list
            copies[i+j+1] += copies[i]
    return sum(copies)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
