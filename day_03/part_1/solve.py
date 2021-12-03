from collections import defaultdict

FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

gamma_rate = 0
epsilon_rate = 0

positions = defaultdict(int)

for entry in data:
    digits = [int(d) for d in entry]

    for index, digit in enumerate(digits):
        if digit == 1:
            positions[index] += 1
        else:
            positions[index] -= 1

gamma_rates = defaultdict(int)
epsilon_rates = defaultdict(int)

for key, value in positions.items():
    if value > 0:
        gamma_rates[int(key)] = 1
        epsilon_rates[int(key)] = 0
    else:
        gamma_rates[int(key)] = 0
        epsilon_rates[int(key)] = 1

gamma_rate = int("".join([str(v) for v in gamma_rates.values()]), 2)
epsilon_rate = int("".join([str(v) for v in epsilon_rates.values()]), 2)

power_consumption = gamma_rate * epsilon_rate

print("Consumption:", power_consumption)