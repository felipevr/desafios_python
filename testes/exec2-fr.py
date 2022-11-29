#!/bin/python3

import math
import os
import random
import re
import sys

def oi(ss):
    if '|' not in ss:
        return 0
    
    a = ss.index('|')
    z = ss.rindex('|')
    
    if (a == z):
        return 0
    
    ss = ss[a:z+1]
    #print(ss)
    #caixas = ss.split('|')
        
    return ss.count('*')


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#
def numberOfItems(s, startIndices, endIndices):
    #a = s.split('|')
    r = []
    n = len(startIndices)
    for i in range(n):
        a = startIndices[i]
        z = endIndices[i]
        #print(a,z)
        r.append(oi(s[a-1:z]))
    
    return r

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
