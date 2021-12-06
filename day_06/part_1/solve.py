NUMBER_OF_DAYS = 3
#FILENAME = "example.txt"
FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.read()
    data = [int(num) for num in data.split(",")]

print(data)

for i in range(80):
    to_add = []

    for i, number in enumerate(data):
        if number == 0:
            data[i] = 6  # Reset
            to_add.append(8)  # Add new lanternfish
        else:
            data[i] = number - 1

    data.extend(to_add)

print(len(data))
