from utils import timed


@timed
def part_one(text):
    total_calibration = 0
    for line in text:
        calibration = 0
        for char in line:
            if char.isdigit():
                calibration += 10 * int(char)
                break
        for char in line[::-1]:
            if char.isdigit():
                calibration += int(char)
                break
        total_calibration += calibration
    return total_calibration


@timed
def part_two(text):
    total_calibration = 0
    numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for line in text:
        first, last = 2_147_483_647, -1
        tens,  ones = 2_147_483_647, -1

        for i in range(1, 10):
            first_index = line.find(numbers[i])
            last_index = line.rfind(numbers[i])
            if first_index != -1 and first_index < first:
                first = first_index
                tens = i * 10
            if last_index != -1 and last_index > last:
                last = last_index
                ones = i

            first_index = line.find(digits[i])
            last_index = line.rfind(digits[i])
            if first_index != -1 and first_index < first:
                first = first_index
                tens = i * 10
            if last_index != -1 and last_index > last:
                last = last_index
                ones = i

        calibration = tens + ones
        total_calibration += calibration

    return total_calibration


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
