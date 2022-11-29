#!/bin/python3

import math
import os
import random
import re
import sys
import timeit
import cProfile

def oi3(ss):
    conta = False
    total = 0
    atual = 0
    #print(ss)
    for l in ss:
        if (l == '|'):
            if (conta):
                total+= atual
            conta = True
            atual = 0
        elif (l == '*' and conta):
            atual += 1
    return total

def oi2(ss):
    if '|' not in ss:
        return 0
    
    a = ss.index('|')
    z = ss.rindex('|')
    
    if (a == z):
        return 0
    
    ss = ss[a:z+1]
    #print(ss)
    caixas = ss.split('|')
    
    total = 0
    for bah in caixas:
        total += len(bah)
    
    return total

def oi(ss):
    if '|' not in ss:
        return 0
    
    a = ss.index('|')
    z = ss.rindex('|')
    
    if (a == z):
        return 0
    
    ss = ss[a:z+1]
        
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


s = ''
startIndices = []
endIndices = []
fptr = sys.stdout

def main():
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

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


def main_fake():
    numberOfItems(s, startIndices, endIndices)

def main_loop():
    for i in range(5000000):
        main_fake()

if __name__ == '__main__':
    main()
    print((timeit.Timer(main_fake).timeit(number=200000)))
    cProfile.run("main_loop()")
    fptr.close()