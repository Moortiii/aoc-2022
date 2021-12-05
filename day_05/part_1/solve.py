import sys
from collections import defaultdict

FILENAME = "input.txt"
#FILENAME = "example.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    data = [line.split(" -> ") for line in data]

line_overview = defaultdict(lambda: defaultdict(int))


def get_dimensions(data):
    flattened = []

    for line in data:
        x, y = line

        for value in x.split(","):
            flattened.append(int(value))

        for value in y.split(","):
            flattened.append(int(value))

    return (0, max(flattened))


dimensions = get_dimensions(data)
print(dimensions)

for line in data:
    print(line)
    x1, y1 = line[0].split(",")
    x1 = int(x1)
    y1 = int(y1)

    x2, y2 = line[1].split(",")
    x2 = int(x2)
    y2 = int(y2)

    if x2 < x1:
        temp = x2
        x2 = x1
        x1 = temp

    if y2 < y1:
        temp = y2
        y2 = y1
        y1 = temp

    added = []

    if x1 == x2 or y1 == y2:
        for i in range(x1, (x2 + 1)):
            point = (i, y1)
            if point not in added:
                line_overview[i][y1] += 1
                added.append(point)
                # print(f"Added point at ({i},{y1})")

        for i in range(y1, (y2 + 1)):
            point = (x1, i)
            if point not in added:
                line_overview[x1][i] += 1
                added.append(point)
                # print(f"Added point at ({x1},{i})")

    # print("")


def print_output(lines):
    output = ""

    for i in range(0, get_dimensions(data)[1] + 1):
        for j in range(0, get_dimensions(data)[1] + 1):
            count = lines[j][i]
            output += str(count) if count != 0 else "."

        output += "\n"

    print(f"\n{output}\n")


def calculate_overlap(lines):
    overlap = 0

    for i in range(0, max(lines) + 1):
        for j in range(0, max(lines) + 1):
            if lines[i][j] >= 2:
                overlap += 1

    return overlap


print_output(line_overview)
overlap = calculate_overlap(line_overview)
print("Overlap:", overlap)
