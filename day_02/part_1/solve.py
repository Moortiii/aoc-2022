with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    data = [(line.split()[0], int(line.split()[1])) for line in data]

position = {
    "x": 0,
    "y": 0,
    "z": 0,
}

for instruction in data:
    direction, displacement = instruction

    if direction == "forward":
        position["x"] += displacement
    elif direction == "down":
        position["y"] += displacement
    elif direction == "up":
        position["y"] -= displacement

print(position["x"] * position["y"])