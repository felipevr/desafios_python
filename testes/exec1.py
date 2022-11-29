#!/bin/python3

import math
import os
import random
import re
import sys
import timeit
import cProfile





def addtu(id, users):
    if id in users:
        users[id] += 1
    else:
        users[id] = 1

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#
def processLogs(logs, threshold):
    # identify the users that have a number of transcations over a threshold
    # ascending numeric value
    users = {}
    
    #sender_user_id (9d)
    #recipient_user_id (9d)
    #amount_of_transaction
    for entry in logs:
        a = entry.split()
        u1 = int(a[0])
        u2 = int(a[1])
        addtu(u1, users)
        if (u2 != u1):
            addtu(u2, users)
    
    over = {}
    for u in users:
        if users[u] >= threshold:
            over[u] = users[u]
    s = sorted(over)
    
    return [str(i) for i in s]
        
            
        
logs = ''
threshold = 0
fptr = sys.stdout

def main():
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')


def main_fake():
    processLogs(logs, threshold)

def main_loop():
    for i in range(500000):
        main_fake()


if __name__ == '__main__':
    
    main()
    print((timeit.Timer(main_fake).timeit(number=200000)))
    cProfile.run("main_loop()")

    fptr.close()