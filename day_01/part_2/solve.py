with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    data = [int(line) for line in data]

SLIDING_WINDOW_SIZE = 3

previous = []
previous_sum = sum(previous)
increments = 0

for entry in data:
    if len(previous) < SLIDING_WINDOW_SIZE:
        previous.append(entry)
        continue
    
    previous.pop(0)
    previous.append(entry)
    current_sum = sum(previous)

    if current_sum > previous_sum:
        increments += 1
    
    previous_sum = sum(previous) 

print("Increments:", increments)