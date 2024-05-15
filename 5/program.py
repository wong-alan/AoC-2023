import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text):
    locations = []
    seed_to_soil = {}
    soil_to_fert = {}
    fert_to_watr = {}
    watr_to_lite = {}
    lite_to_temp = {}
    temp_to_humi = {}
    humi_to_locn = {}
    map_list = [seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lite, lite_to_temp, temp_to_humi, humi_to_locn]
    current_map = -1

    seed_line = text.readline()
    seeds = [int(seed) for seed in seed_line.split()[1:]]

    for line in text:
        if line == "\n":
            pass
        elif line.endswith("map:\n"):
            current_map += 1
        else:
            dest, src, length = [int(num) for num in line.split()]
            map_list[current_map][(src, src + length - 1)] = dest - src

    for value in seeds:
        for map in map_list:
            for (range_left, range_right), jump in map.items():
                if range_left <= value <= range_right:
                    value += jump
                    break
        locations.append(value)

    return min(locations)

@timed
def part_two(text):
    seed_to_soil = {}
    soil_to_fert = {}
    fert_to_watr = {}
    watr_to_lite = {}
    lite_to_temp = {}
    temp_to_humi = {}
    humi_to_locn = {}
    map_list = [seed_to_soil, soil_to_fert, fert_to_watr, watr_to_lite, lite_to_temp, temp_to_humi, humi_to_locn]
    current_map = -1

    seed_line = [int(seed) for seed in text.readline().split()[1:]]
    seeds = [(seed_line[i], seed_line[i] + seed_line[i+1] - 1) for i in range(0, len(seed_line), 2)]

    for line in text:
        if line == "\n":
            pass
        elif line.endswith("map:\n"):
            current_map += 1
        else:
            dest, src, length = [int(num) for num in line.split()]
            map_list[current_map][(src, src + length - 1)] = dest - src

    def transform_range(seed_left, seed_right, map):
        new_ranges = []
        for (range_left, range_right), jump in map.items():
            if seed_left > range_right or seed_right < range_left:
                # Seed range is outside map range
                pass
            elif seed_left < range_left <= seed_right <= range_right:
                # Seed range is hanging out of left side
                new_ranges.extend(transform_range(seed_left, range_left - 1, map))
                new_ranges.append((range_left + jump, seed_right + jump))
                break
            elif range_left <= seed_left <= range_right < seed_right:
                # Seed range is hanging out of right side
                new_ranges.append((seed_left + jump, range_right + jump))
                new_ranges.extend(transform_range(range_right + 1, seed_right, map))
                break
            elif range_left <= seed_left and seed_right <= range_right:
                # Seed range is within map range
                new_ranges.append((seed_left + jump, seed_right + jump))
                break
            elif seed_left < range_left and seed_right > range_right:
                # Seed range is hanging out of left and right side of map range
                new_ranges.extend(transform_range(seed_left, range_left - 1, map))
                new_ranges.append((range_left + jump, range_right + jump))
                new_ranges.extend(transform_range(range_right + 1, seed_right, map))
                break
            else:
                print(f"Range: {range_left:,}-{range_right:,} :: Seed: {seed_left:,}-{seed_right:,}")
                raise Exception("Something bad is happening")

        if not new_ranges:
            return [(seed_left, seed_right)]
        return new_ranges

    for map in map_list:
        new_seed_range = []
        for (seed_left, seed_right) in seeds:
            new_seed_range.extend(transform_range(seed_left, seed_right, map))
        seeds = new_seed_range

    return min([left for (left, right) in seeds])


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
