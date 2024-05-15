from typing import TextIO, List
import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text: TextIO) -> int:
    reflected_cols = 0
    reflected_rows = 0

    def check_reflection(pattern: List[List[str]]) -> int:
        for i in range(1, len(pattern)):
            differences = 0
            line_pairs = zip(pattern[i - 1::-1], pattern[i:])
            for line_a, line_b in line_pairs:
                differences = sum(1 for a, b in zip(line_a, line_b) if a != b)
                if differences:
                    break
            if differences == 0:
                return i
        return 0

    pattern = []
    for line in (line.rstrip() for line in text):
        if line:
            pattern.append([char for char in line])
        else:
            rows = check_reflection(pattern)
            if rows:
                reflected_rows += rows
            else:
                # Transpose
                pattern = list(map(list, zip(*pattern)))
                cols = check_reflection(pattern)
                if cols:
                    reflected_cols += cols
                else:
                    print("Missing reflection!")
            pattern = []

    return reflected_cols + 100 * reflected_rows


@timed
def part_two(text: TextIO) -> int:
    reflected_cols = 0
    reflected_rows = 0

    # Check for reflections with exactly one difference
    def check_reflection(pattern: List[List[str]]) -> int:
        for i in range(1, len(pattern)):
            smudges = 0
            line_pairs = zip(pattern[i-1::-1], pattern[i:])
            for line_a, line_b in line_pairs:
                smudges += sum(1 for a, b in zip(line_a, line_b) if a != b)
                if smudges > 1:
                    break
            if smudges == 1:
                return i
        return 0

    pattern = []
    for line in (line.rstrip() for line in text):
        if line:
            pattern.append([char for char in line])
        else:
            rows = check_reflection(pattern)
            if rows:
                reflected_rows += rows
            else:
                # Transpose
                pattern = list(map(list, zip(*pattern)))
                cols = check_reflection(pattern)
                if cols:
                    reflected_cols += cols
                else:
                    print("Missing reflection!")
            pattern = []

    return reflected_cols + 100 * reflected_rows


# Requires 2 empty lines at end of input file
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
