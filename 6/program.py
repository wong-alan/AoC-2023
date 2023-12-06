from functools import reduce

from utils import timed


@timed
def part_one(text):
    times = [int(time) for time in text.readline().split()[1:]]
    distances = [int(dist) for dist in text.readline().split()[1:]]
    races = zip(times, distances)

    ways_to_win = []
    for time, distance in races:
        wins = 0
        for t in range(1, time):
            dist = t * (time - t)
            if dist > distance:
                wins += 1
        ways_to_win.append(wins)

    return reduce(lambda x, y: x * y, ways_to_win)


@timed
def part_two(text):
    time = int(text.readline().replace(" ", "").split(":")[1])
    distance = int(text.readline().replace(" ", "").split(":")[1])

    ways_to_win = 0
    for t in range(1, time):
        dist = t * (time - t)
        if dist > distance:
            ways_to_win += 1

    return ways_to_win


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
