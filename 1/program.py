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


def part_two(text):
    total_calibration = 0
    numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = [str(i) for i in range(10)]

    def find_all(search_str, target):
        start = 0
        while True:
            start = search_str.find(target, start)
            if start == -1:
                return
            yield start
            start += len(target)

    for line in text:
        first, last = 2_147_483_647, -1
        tens,  ones = 2_147_483_647, -1
        for i in range(1, 10):
            word_indexes = find_all(line, numbers[i])
            for index in word_indexes:
                if index < first:
                    first = index
                    tens = i * 10
                if index > last:
                    last = index
                    ones = i
            num_indexes = find_all(line, digits[i])
            for index in num_indexes:
                if index < first:
                    first = index
                    tens = i * 10
                if index > last:
                    last = index
                    ones = i
        calibration = tens + ones
        total_calibration += calibration

    return total_calibration


with open("input.txt", "r") as file:
    answer_one = part_one(file)

with open("input.txt", "r") as file:
    answer_two = part_two(file)

print(f"One: {answer_one} \nTwo: {answer_two}")
