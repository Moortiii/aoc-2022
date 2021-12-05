FILENAME = "example.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]


def transpose(rows):
    return [
        "".join(row[i] for row in rows)
        for i in range(len(rows[0]))
    ]


def get_most_common(rows):
    return [
        1 if row.count("1") >= row.count("0") else 0
        for row in transpose(rows)
    ]


def get_least_common(rows):
    return [v ^ 1 for v in get_most_common(rows)]


def find_matching(entries, filter_func):
    rows = entries.copy()
    bits = len(entries[0])

    for i in range(bits):
        if len(rows) == 1:
            return rows[0]

        target = filter_func(rows)
        print("Rows:", rows)
        rows = [row for row in rows if row[i] == target[i]]


oxygen_rating = int(find_matching(data, get_most_common), 2)
carbon_rating = int(find_matching(data, get_least_common), 2)
life_support_rating = oxygen_rating * carbon_rating

print("Carbon rating:", carbon_rating, bin(carbon_rating))
print("Oxygen rating:", oxygen_rating, bin(oxygen_rating))
print("Life support rating:", life_support_rating)
