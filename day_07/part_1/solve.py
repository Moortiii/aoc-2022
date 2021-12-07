from collections import defaultdict


def read_content(filename):
    with open(filename) as f:
        data = f.read()
        data = [int(number) for number in data.split(",")]

    return data


def solve(data):
    occurences = defaultdict(int)

    for number in data:
        occurences[number] += 1

    distances = defaultdict(int)

    for i in range(max(data) + 1):
        distance = 0

        for number, count in occurences.items():
            distance += (abs(number - i)) * count

        distances[i] = distance

    return distances[min(distances, key=distances.get)]


#FILENAME = "input.txt"
FILENAME = "example.txt"

data = read_content(FILENAME)
result = solve(data)
print("Part 1:", result)
