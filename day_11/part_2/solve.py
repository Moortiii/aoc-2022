from itertools import product
from collections import defaultdict


def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [[int(x) for x in line] for line in data]

    return data


def get_neighbours(cell, dimensions):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < dimensions for n in c):
            yield c


def print_matrix(matrix):
    for line in matrix:
        print("".join([str(x) for x in line]))

    print()


def step(matrix, number_of_flashes, i):
    def increment():
        for y in range(DIMENSIONS):
            for x in range(DIMENSIONS):
                matrix[y][x] += 1

    def flash(point):
        x, y = point

        if flash_mapping[y][x]:  # only flash once per step
            return

        if matrix[y][x] > 9:
            flash_mapping[y][x] = True
            neighbours = list(get_neighbours((x, y), DIMENSIONS))

            for neighbour in neighbours:
                nx, ny = neighbour
                matrix[ny][nx] += 1

                if matrix[ny][nx] > 9:
                    flash_mapping[y][x] = True
                    flash((nx, ny))

    def reset(number_of_flashes):
        # Reset flash mapping and energy level of those who flashed
        flashed = []

        for y in range(DIMENSIONS):
            for x in range(DIMENSIONS):
                flashed.append(flash_mapping[y][x])

        if all(flashed):
            print(f"All flashed simultaneously at {i}")
            import sys
            sys.exit()

        for y in range(DIMENSIONS):
            for x in range(DIMENSIONS):
                if flash_mapping[y][x]:
                    number_of_flashes += 1
                    matrix[y][x] = 0

                flash_mapping[y][x] = False

        return number_of_flashes

    flash_mapping = defaultdict(lambda: defaultdict(bool))

    increment()

    for y in range(DIMENSIONS):
        for x in range(DIMENSIONS):
            if matrix[y][x] > 9:
                flash((x, y))

    number_of_flashes = reset(number_of_flashes)

    # print(f"After step {i}:")
    # print_matrix(matrix)

    return matrix, number_of_flashes


DIMENSIONS = 10
NUMBER_OF_STEPS = 2000

matrix = read_data()
number_of_flashes = 0

# print(f"Before any steps:")
# print_matrix(matrix)

for i in range(1, NUMBER_OF_STEPS + 1):
    matrix, number_of_flashes = step(matrix, number_of_flashes, i)

print("Number of flashes:", number_of_flashes)
