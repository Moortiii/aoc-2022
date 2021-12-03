FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]


def get_most_and_least_common(rows):
    transposed = [
        "".join(row[i] for row in rows)
        for i in range(len(rows[0]))
    ]

    most_common = []

    for row in transposed:
        set_bits_count   = row.count("1")
        unset_bits_count = row.count("0")

        if set_bits_count >= unset_bits_count:
            most_common.append(1)
        else:
            most_common.append(0)

    return {
        "most_common": most_common,
        "least_common": [v ^ 1 for v in most_common]
    }


def remove_unmatching(entries, target):
    rows = entries.copy()
    column_count = len(entries[0])

    for column in range(column_count):
        value_to_match = get_most_and_least_common(rows)[target]
        
        for row in rows[:]:
            if len(rows) == 1:
                break

            digit = int(row[column])
            
            if digit != value_to_match[column]:
                rows.remove(row)

    return rows[0]

oxygen_rating = int(remove_unmatching(data, "most_common"), 2)
carbon_rating = int(remove_unmatching(data, "least_common"), 2)
life_support_rating = oxygen_rating * carbon_rating

print("Carbon rating:", carbon_rating, bin(carbon_rating))
print("Oxygen rating:", oxygen_rating, bin(oxygen_rating))
print("Life support rating:", life_support_rating)