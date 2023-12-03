from utils import timed


@timed
def part_one(text):
    for line in text:
        break
    return "Hello"


@timed
def part_two(text):
    for line in text:
        break
    return "world"


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
