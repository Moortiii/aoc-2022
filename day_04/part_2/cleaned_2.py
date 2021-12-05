import json
BOARD_SIZE = 5

with open("example.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    drawing_numbers = data[0].split(",")  # Extract drawing numbers

    # Discard board separators and drawing numbers
    data = [line for line in data[2:] if line != ""]


def create_boards(data):
    boards = []

    while data:
        board = {
            "cells": [],
            "has_won": False
        }

        for y in range(BOARD_SIZE):
            line = data.pop(0)
            numbers = line.split(" ")
            numbers = [x for x in numbers if x != ""]
            row = []

            for x in range(BOARD_SIZE):
                row.append({
                    "x": x,
                    "y": y,
                    "value": numbers.pop(0),
                    "marked": False
                })

            board["cells"].append(row)
        boards.append(board)

    return boards


def get_rows(board):
    return [
        [row for row in board["cells"][i]]
        for i in range(BOARD_SIZE)
    ]


def get_columns(board):
    transposed = [[
        board["cells"][i][j] for j in range(BOARD_SIZE)]
        for i in range(BOARD_SIZE)
    ]

    return transposed


def check_has_won(board):
    rows = get_rows(board)
    cols = get_columns(board)

    print("Rows:", json.dumps(rows, indent=2))

    winning_rows = [
        all([row for row in rows if row[i]["marked"] == True])
        for i in range(BOARD_SIZE)
    ]

    print("Winners:", winning_rows)

    winning_columns = [
        all([col for col in cols if col[i]["marked"] == True])
        for i in range(BOARD_SIZE)
    ]

    return any(winning_columns) or any(winning_rows)


def draw_numbers(boards):
    while drawing_numbers:
        number = drawing_numbers.pop(0)

        for board in boards[2:]:
            for y in range(BOARD_SIZE):
                for x in range(BOARD_SIZE):
                    cell = board["cells"][y][x]
                    if cell["value"] == number:
                        cell["marked"] = True
                        print("Cell:", cell)

                        if number == "24":
                            print(check_has_won(board))


boards = create_boards(data)
board = boards[0]
draw_numbers(boards)

# values = [
#     [v[i]["value"] for v in get_columns(board)]
#     for i in range(BOARD_SIZE)
# ]
