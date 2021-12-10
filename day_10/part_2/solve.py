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

before_terminating = []
indices_to_discard = []

for index, line in enumerate(data):
    if line[0] not in opening_tags:
        indices_to_discard.append(index)
        continue

    should_stop = False
    open_tags = []

    for i, symbol in enumerate(line):
        if should_stop:
            break

        if not open_tags:
            open_tags.append(symbol)
            # print("Opened", symbol, "".join(open_tags), i + 1)
            continue

        current_tag = open_tags[len(open_tags) - 1]

        if symbol in opening_tags:
            open_tags.append(symbol)
            # print("Opened", symbol, "".join(open_tags), i + 1)
        else:
            expected_tag = tags[current_tag]

            if expected_tag == symbol:
                open_tags.pop(-1)
                # print("Closed", symbol, "".join(open_tags), i + 1)
            else:
                # print("Unexpected", symbol, "".join(open_tags), i + 1)
                indices_to_discard.append(index)
                should_stop = True

    before_terminating.append(open_tags)
    # print("")

before_terminating = [
    x for i, x in enumerate(before_terminating) if i not in indices_to_discard]

termination_sequences = [[tags[k] for k in line[::-1]]
                         for line in before_terminating]


scores = []

mapping = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

for sequence in termination_sequences:
    print("Seq:", sequence)
    score = 0

    for char in sequence:
        score *= 5
        score += mapping[char]

    scores.append(score)

scores = sorted(scores)
print(len(scores))
print(scores[(len(scores) // 2)])
