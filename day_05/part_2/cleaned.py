from collections import defaultdict


def parse_data():
    FILENAME = "example.txt"
    #FILENAME = "input.txt"

    with open(FILENAME, "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(" -> ") for line in data]
        data = [[entry.split(",") for entry in line] for line in data]
        data = [[(int(entry[0]), int(entry[1])) for entry in line]
                for line in data]

    return data


def print_output(dimensions, lines):
    output = ""

    for i in range(0, dimensions + 1):
        for j in range(0, dimensions + 1):
            count = lines[j][i]
            output += str(count) if count != 0 else "."

        output += "\n"

    print(f"\n{output}")


def calculate_overlap(lines):
    overlap = 0

    for i in range(0, max(lines) + 1):
        for j in range(0, max(lines) + 1):
            if lines[i][j] >= 2:
                overlap += 1

    return overlap


def get_dimensions(data):
    xs = [[(entry[0], entry[1]) for entry in line] for line in data]
    xs = [x for sublist in xs for x in sublist]
    return max(max(xs))


data = parse_data()
line_overview = defaultdict(lambda: defaultdict(int))

for line in data:
    x1, y1 = line[0]
    x2, y2 = line[1]

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


print_output(dimensions=get_dimensions(data), lines=line_overview)
print("Overlap:", calculate_overlap(line_overview))
