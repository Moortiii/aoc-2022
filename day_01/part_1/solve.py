with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    data = [int(line) for line in data]

previous = None
increments = 0

for entry in data:
    if previous and previous < entry:
        increments += 1

    previous = entry

print("Increments:", increments)