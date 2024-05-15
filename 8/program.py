import math
import re
from itertools import cycle
import sys
import os
sys.path.append(os.path.abspath(".."))
from utils import timed


@timed
def part_one(text):
    directions = text.readline().rstrip()
    text.readline()

    nodes = {}
    for line in text:
        node, links = line.split(" = ")
        links = re.findall(r"([A-Z]{3})", links)
        nodes[node] = links

    path = {"L": 0, "R": 1}
    steps = 0
    current_node = "AAA"
    for direct in cycle(directions):
        if current_node == "ZZZ":
            break
        current_node = nodes[current_node][path[direct]]
        steps += 1
    return steps


@timed
def part_two(text):
    directions = text.readline().rstrip()
    text.readline()

    nodes = {}
    start_nodes = []
    for line in text:
        node, links = line.split(" = ")
        links = re.findall(r"([A-Z]{3})", links)
        nodes[node] = links
        if node.endswith("A"):
            start_nodes.append(node)

    path = {"L": 0, "R": 1}
    steps = [0] * len(start_nodes)
    for index, start in enumerate(start_nodes):
        current_steps = 0
        current_node = start
        direct_loop = cycle(directions)
        while not current_node.endswith("Z"):
            current_node = nodes[current_node][path[next(direct_loop)]]
            current_steps += 1
        steps[index] = current_steps
    return math.lcm(*steps)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        answer_one = part_one(file)

    with open("input.txt", "r") as file:
        answer_two = part_two(file)

    print(f"One: {answer_one} \nTwo: {answer_two}")
