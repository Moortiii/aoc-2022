def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(x) for x in line] for line in data]

    return data


# def get_neighbours(pos, matrix):
#     """ If we want all neighbors, not just in all 4 directions """
#     # https://stackoverflow.com/a/49973756
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows else 0
#     x, y = pos

#     for _y in range(max(0, x - 1), min(rows, x + 2)):
#         for _x in range(max(0, y - 1), min(cols, y + 2)):
#             if (_y, _x) != pos:
#                 yield matrix[_y][_x]


def get_neighbours(pos, matrix):
    neighbours = []
    x, y = pos

    top = matrix[y][x + 1] if x + 1 < len(matrix[0]) else None
    bottom = matrix[y][x - 1] if x - 1 >= 0 else None
    left = matrix[y - 1][x] if y - 1 >= 0 else None
    right = matrix[y + 1][x] if y + 1 < len(matrix) else None
    neighbours = [top, bottom, left, right]

    return [x for x in neighbours if x is not None]


def is_low_point(pos, matrix):
    neighbours = get_neighbours(pos, matrix)
    x, y = pos
    current = matrix[y][x]
    return all([True if current < neighbor else False for neighbor in neighbours])


data = read_data()
low_points = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if is_low_point((x, y), data):
            low_points.append(((x, y), data[y][x]))

risk_level = sum([entry[1] + 1 for entry in low_points])
print("Risk level:", risk_level)
