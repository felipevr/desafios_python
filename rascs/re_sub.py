#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

n = int(input().strip())
for i in range(n):
    line = input()
    #print (re.sub(r"\s\|\|\s", " or ", re.sub(r"\s&&\s", " and ", line)))
    #print (re.sub(r" \|\| ", " or ", re.sub(r" && ", " and ", line)))
    print (re.sub(r"\b\|\|\b", " or ", re.sub(r"\b&&\b", " and ", line)))
