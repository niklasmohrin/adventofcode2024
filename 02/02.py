#!/usr/bin/env python3

import operator
import sys
from functools import partial
from itertools import chain, starmap

from more_itertools import ilen, windowed

reports = [tuple(map(int, line.split())) for line in sys.stdin]
differences = lambda it: list(starmap(operator.sub, windowed(it, 2)))
is_forwards_safe = lambda report: all(1 <= d <= 3 for d in differences(report))
forwards_or_backwards = lambda fw, report: fw(report) or fw(report[::-1])
print(ilen(filter(partial(forwards_or_backwards, is_forwards_safe), reports)))


def is_forwards_safe_after_removing_one(report):
    return any(
        is_forwards_safe(chain(report[:i], report[i + 1 :])) for i in range(len(report))
    )


print(
    ilen(
        filter(
            partial(forwards_or_backwards, is_forwards_safe_after_removing_one), reports
        )
    )
)
