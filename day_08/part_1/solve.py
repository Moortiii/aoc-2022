def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip().split(" ") for line in data]

    return data


mapping = {
    1: "cf",
    7: "acf",
    4: "bcdf",
    2: "acdeg",
    3: "acdfg",
    5: "abdfg",
    0: "abcefg",
    6: "abdefg",
    9: "abcdfg",
    8: "abcdefg"
}

data = read_data()

count = 0

for line in data:
    output_values = line[11:]

    for value in output_values:
        if len(value) in [2, 4, 3, 7]:
            count += 1

print("Result:", count)
