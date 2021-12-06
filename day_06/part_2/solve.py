from collections import deque

FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.read()
    data = [int(num) for num in data.split(",")]

growth = deque([0 for _ in range(0, 9)])

for number in data:
    growth[number] += 1


def simulate_growth(growth):
    for _ in range(256):
        growth.rotate(-1)
        growth[6] += growth[8]

    return growth


output = simulate_growth(growth)
print("Total number of fishies:", sum(output))
