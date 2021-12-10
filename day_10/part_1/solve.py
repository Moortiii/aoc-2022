def read_data():
    with open("input.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    return data


data = read_data()

tags = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

opening_tags = [key for key in tags.keys()]
closing_tags = [value for value in tags.values()]

invalid_tags = []

for line in data:
    if line[0] not in opening_tags:
        invalid_tags.append(line[0])
        continue

    should_stop = False
    open_tags = []

    for i, symbol in enumerate(line):
        if should_stop:
            break

        if not open_tags:
            open_tags.append(symbol)
            #print("Opened", symbol, "".join(open_tags), i + 1)
            continue

        current_tag = open_tags[len(open_tags) - 1]

        if symbol in opening_tags:
            open_tags.append(symbol)
            #print("Opened", symbol, "".join(open_tags), i + 1)
        else:
            expected_tag = tags[current_tag]

            if expected_tag == symbol:
                open_tags.pop(-1)
                #print("Closed", symbol, "".join(open_tags), i + 1)
            else:
                #print("Unexpected", symbol, "".join(open_tags), i + 1)
                invalid_tags.append(symbol)
                should_stop = True

    # print("")

mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

print("Result:", sum([mapping[x] for x in invalid_tags]))
