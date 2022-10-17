#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

def sub(lin):
    ret = re.sub(r"\s\|\|\s", " or ", re.sub(r"\s&&\s", " and ", lin))
    return re.sub(r"\s\|\|\s", " or ", re.sub(r"\s&&\s", " and ", ret))

n = int(input().strip())
for i in range(n):
    line = input()
    print (sub(line))