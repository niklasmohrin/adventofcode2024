#!/usr/bin/env python3

import sys
from collections import Counter
from more_itertools import unzip

left_list, right_list = map(
    list, unzip(tuple(map(int, line.split())) for line in sys.stdin)
)
print(sum(abs(x - y) for x, y in zip(sorted(left_list), sorted(right_list))))
right_counts = Counter(right_list)
print(sum(x * right_counts[x] for x in left_list))
