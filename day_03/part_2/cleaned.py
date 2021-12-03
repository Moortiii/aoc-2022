from collections import defaultdict

FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

def get_most_and_least_common(entries):
    positions = defaultdict(int)

    for entry in entries:
        digits = [int(d) for d in entry]

        for index, digit in enumerate(digits):
            if digit == 1:
                positions[index] += 1
            else:
                positions[index] -= 1

    most_common = defaultdict(int)
    least_common = defaultdict(int)

    for key, value in positions.items():
        if value == 0:
            most_common[int(key)] = 1
            least_common[int(key)] = 0
        elif value > 0:
            most_common[int(key)] = 1
            least_common[int(key)] = 0
        else:
            most_common[int(key)] = 0
            least_common[int(key)] = 1

    return {
        "most_common": most_common,
        "least_common": least_common
    }


def remove_unmatching(entries, identifier):
    entries_kept = entries.copy()
    matcher = get_most_and_least_common(entries_kept)[identifier]

    for i in range(len(data[0])):
        matcher = get_most_and_least_common(entries_kept)[identifier]
        
        for entry in entries_kept[:]:
            if len(entries_kept) == 1:
                break

            digit = int(entry[i])
            
            if digit != matcher[i]:
                entries_kept.remove(entry)

    return entries_kept[0]

oxygen_rating = int(remove_unmatching(data, "most_common"), 2)
carbon_rating = int(remove_unmatching(data, "least_common"), 2)
life_support_rating = oxygen_rating * carbon_rating

print("Carbon rating:", carbon_rating, bin(carbon_rating))
print("Oxygen rating:", oxygen_rating, bin(oxygen_rating))
print("Life support rating:", life_support_rating)