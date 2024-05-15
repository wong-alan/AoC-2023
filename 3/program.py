import re
from utils import timed


@timed
def part_one(text):
    total_part_num = 0
    prev_num = []
    prev_sym = []
    prev_used_num_idx = []

    for line in text:
        num_matches = list(re.finditer(r"\d+", line))
        sym_matches = list(re.finditer(r"[^\\.\d\n]", line))
        used_num_idx = []

        for symbol in sym_matches:
            for num in num_matches:
                if num.start() - 1 <= symbol.start() <= num.end() and \
                        num.start() not in used_num_idx:
                    total_part_num += int(num.group(0))
                    used_num_idx.append(num.start())

            for num in prev_num:
                if num.start() - 1 <= symbol.start() <= num.end() and \
                        num.start() not in prev_used_num_idx:
                    total_part_num += int(num.group(0))
                    prev_used_num_idx.append(num.start())

        for symbol in prev_sym:
            for num in num_matches:
                if num.start() - 1 <= symbol.start() <= num.end() and \
                        num.start() not in used_num_idx:
                    total_part_num += int(num.group(0))
                    used_num_idx.append(num.start())

        prev_num = num_matches
        prev_sym = sym_matches
        prev_used_num_idx = used_num_idx

    return total_part_num


@timed
def part_two(text):
    total_gear_ratio = 0
    prev_prev_num = []
    prev_num = []
    prev_gear = []

    for line in text:
        curr_num = list(re.finditer(r"\d+", line))
        gear_matches = list(re.finditer(r"\*", line))

        for gear in prev_gear:
            nums = []
            for num in prev_prev_num:
                if num.start() - 1 <= gear.start() <= num.end():
                    nums.append(int(num.group(0)))
            for num in prev_num:
                if num.start() - 1 <= gear.start() <= num.end():
                    nums.append(int(num.group(0)))
            for num in curr_num:
                if num.start() - 1 <= gear.start() <= num.end():
                    nums.append(int(num.group(0)))
            if len(nums) == 2:
                total_gear_ratio += nums[0] * nums[1]

        prev_prev_num = prev_num
        prev_num = curr_num
        prev_gear = gear_matches

    # Gears at end
    for gear in prev_gear:
        nums = []
        for num in prev_prev_num:
            if num.start() - 1 <= gear.start() <= num.end():
                nums.append(int(num.group(0)))
        for num in prev_num:
            if num.start() - 1 <= gear.start() <= num.end():
                nums.append(int(num.group(0)))

    return total_gear_ratio


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
