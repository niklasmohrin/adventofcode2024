#!/usr/bin/env python3

import sys
import re
import operator
from functools import reduce

program = sys.stdin.read()
print(
    sum(
        reduce(operator.mul, map(int, match))
        for match in re.findall(r"mul\((\d+),(\d+)\)", program, re.MULTILINE)
    )
)


def parse(program):
    enabled = True
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", program, re.MULTILINE):
        match m.group(0):
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    yield m


print(sum(reduce(operator.mul, map(int, match.groups())) for match in parse(program)))
