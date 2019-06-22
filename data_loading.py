import cell_fields


def load_level():
    return [
        ['#','#','#','#','#','#','#','#','#','#','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','.','.','.','.','.','.','.','.','.','#'],
        ['#','#','#','#','#','#','#','#','#','#','#']
    ]


def setup_directions():
    directions = {
        "w": {
            "x": 0,
            "y": -1
        },
        "s": {
            "x": 0,
            "y": 1
        },
        "a": {
            "x": -1,
            "y": 0
        },
        "d": {
            "x": 1,
            "y": 0
        },
    }

    return directions


def load_signs():
    signs = {
        "player": "@",
        "empty": "."
    }

    return signs


def get_cell_type_by_sign(cell_sign):
    for cell_type, sign in load_signs().items():
        if sign == cell_sign:
            return cell_type


def parse_level_data(level):
    level_data = {
        "cells": [],
        "updates": []
    }

    y = 0
    for row in level:
        data_row = []
        level_data["cells"].append(data_row)
        x = 0
        for cell in row:
            cell_type = get_cell_type_by_sign(cell)

            cell_data = {
                cell_fields.TYPE: cell_type,
                cell_fields.POSITION: {
                    "x": x,
                    "y": y
                },
                cell_fields.VISITOR: None
            }

            data_row.append(cell_data)
            x += 1
        y += 1

    return level_data
