#!/usr/bin/env python3

import sys

grid = list(map(str.strip, sys.stdin))


def rot(mat):
    out = [[None] * len(mat) for _ in range(len(mat[0]))]
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            out[len(mat) - 1 - j][i] = val
    return ["".join(row) for row in out]


def diags(mat):
    out = [""] * (2 * len(mat) - 1)
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            out[i + j] += val
    return out


XMAS = [
    "M_S",
    "_A_",
    "M_S",
]


def matches(mat, x, y, pat):
    for dy, row in enumerate(pat):
        for dx, val in enumerate(row):
            if val != "_" and mat[y + dy][x + dx] != val:
                return False
    return True


count1 = count2 = 0
for _ in range(4):
    grid = rot(grid)
    count1 += sum(row.count("XMAS") for row in grid)
    count1 += sum(diag.count("XMAS") for diag in diags(grid))

    for y in range(len(grid) - 2):
        for x in range(len(grid[y]) - 2):
            count2 += matches(grid, x, y, XMAS)
print(count1)
print(count2)
