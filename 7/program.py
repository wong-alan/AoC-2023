from utils import timed


@timed
def part_one(text):
    card_pwr = {
        'A': 0xE,
        'K': 0xD,
        'Q': 0xC,
        'J': 0xB,
        'T': 0xA,
        '9': 0x9,
        '8': 0x8,
        '7': 0x7,
        '6': 0x6,
        '5': 0x5,
        '4': 0x4,
        '3': 0x3,
        '2': 0x2
    }
    hand_pwr = {
        (5, 0): 0x700_000,  # Five of a kind
        (4, 1): 0x600_000,  # Four of a kind
        (3, 2): 0x500_000,  # Full house
        (3, 1): 0x400_000,  # Three of a kind
        (2, 2): 0x300_000,  # Two pair
        (2, 1): 0x200_000,  # One pair
        (1, 1): 0x100_000,  # High card
    }
    hands = []
    for line in text:
        val_count = [0] * 16
        power = 0x0
        hand, bid = line.split()
        for index, card in enumerate(hand):
            power += card_pwr[card] * (0x10 ** (0x4 - index))
            val_count[card_pwr[card]] += 1

        val_count.sort(reverse=True)
        power += hand_pwr[tuple(val_count[:2])]
        hands.append((power, int(bid)))

    hands.sort()
    winnings = 0
    for index, hand in enumerate(hands):
        winnings += hand[1] * (index + 1)
    return winnings


@timed
def part_two(text):
    card_pwr = {
        'A': 0xD,
        'K': 0xC,
        'Q': 0xB,
        'T': 0xA,
        '9': 0x9,
        '8': 0x8,
        '7': 0x7,
        '6': 0x6,
        '5': 0x5,
        '4': 0x4,
        '3': 0x3,
        '2': 0x2,
        'J': 0x1,
    }
    hand_pwr = {
        (5, 0): 0x700_000,  # Five of a kind
        (4, 1): 0x600_000,  # Four of a kind
        (3, 2): 0x500_000,  # Full house
        (3, 1): 0x400_000,  # Three of a kind
        (2, 2): 0x300_000,  # Two pair
        (2, 1): 0x200_000,  # One pair
        (1, 1): 0x100_000,  # High card
    }
    hands = []
    for line in text:
        val_count = [0] * 16
        power = 0x0
        hand, bid = line.split()
        for index, card in enumerate(hand):
            power += card_pwr[card] * (0x10 ** (0x4 - index))
            val_count[card_pwr[card]] += 1

        joker_count = val_count[card_pwr['J']]
        val_count[card_pwr['J']] = 0
        val_count.sort(reverse=True)
        if joker_count:
            val_count[0] += joker_count

        power += hand_pwr[tuple(val_count[:2])]
        hands.append((power, int(bid)))
    hands.sort()

    winnings = 0
    for index, hand in enumerate(hands):
        winnings += hand[1] * (index + 1)
    return winnings


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
