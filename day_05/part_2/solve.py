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

for line in data:
    x1, y1 = line[0].split(",")
    x1 = int(x1)
    y1 = int(y1)

    x2, y2 = line[1].split(",")
    x2 = int(x2)
    y2 = int(y2)

    added = []

    if x1 == x2 or y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):  # horizontal
            point = (i, y1)

            if point not in added:
                line_overview[i][y1] += 1
                added.append(point)

        for i in range(min(y1, y2), max(y1, y2) + 1):  # vertical
            point = (x1, i)

            if point not in added:
                line_overview[x1][i] += 1
                added.append(point)
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):  # diagonal
            x = i
            y = None

            if y1 >= y2:
                if x1 >= x2:
                    y = min(y1, y2) + (i - min(x1, x2))
                else:
                    y = max(y1, y2) - (i - min(x1, x2))
            else:
                if x1 >= x2:
                    y = max(y1, y2) - (i - min(x1, x2))
                else:
                    y = min(y1, y2) + (i - min(x1, x2))

            point = (x, y)

            if point not in added:
                added.append(point)
                line_overview[x][y] += 1


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


# print_output(line_overview)
overlap = calculate_overlap(line_overview)
print("Overlap:", overlap)
