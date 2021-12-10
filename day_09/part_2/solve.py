def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(x) for x in line] for line in data]

    return data


def get_neighbours(pos, matrix):
    neighbours = []
    x, y = pos

    top = (matrix[y][x + 1], (x+1, y)) if x + 1 < len(matrix[0]) else None
    bottom = (matrix[y][x - 1], (x-1, y)) if x - 1 >= 0 else None
    left = (matrix[y - 1][x], (x, y-1)) if y - 1 >= 0 else None
    right = (matrix[y + 1][x], (x, y+1)) if y + 1 < len(matrix) else None
    neighbours = [top, bottom, left, right]

    return [x for x in neighbours if x is not None]


def is_low_point(pos, matrix):
    neighbours = get_neighbours(pos, matrix)
    x, y = pos
    current = matrix[y][x]
    return all([True if current < neighbor[0] else False for neighbor in neighbours])


def get_low_points(matrix):
    low_points = []

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if is_low_point((x, y), matrix):
                low_points.append(((x, y), matrix[y][x]))

    return low_points


data = read_data()
low_points = get_low_points(data)

basins = []

for low_point in low_points:
    processed = []

    basin = [low_point[0]]
    remaining_low_points = [low_point]

    #print("Moving on...")

    while remaining_low_points:
        next = remaining_low_points.pop(0)
        point = next[0]
        value = next[1]

        if point not in processed:
            processed.append(point)

        neighbours = get_neighbours(point, data)
        neighbours = [x for x in neighbours if x[1]
                      and x[0] < 9 not in processed]

        # print("Point", next)
        # print("Neighbors:", neighbours)
        # print("Processed:", processed)

        for neighbour in neighbours:
            neighbour_value = neighbour[0]
            neighbour_point = neighbour[1]
            # print("Neighbour point:", neighbour_point, neighbour_value)

            if neighbour_value > value and neighbour_value < 9:
                remaining_low_points.append((neighbour_point, neighbour_value))
                # print("Added!")

                if neighbour_point not in basin:
                    basin.append(neighbour_point)

        # print("To process:", remaining_low_points)
        # print("Basin:", basin)

    basins.append(basin)

largest = sorted(basins, key=len)

to_keep = [largest.pop(-1), largest.pop(-1), largest.pop(-1)]

product = len(to_keep[0])

for basin in to_keep[1:]:
    product *= len(basin)

print("Result:", product)
