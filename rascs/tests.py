# https://www.hackerrank.com/domains/python/py-introduction

def squared(n):
    if n >= 0:
        for i in range(n):
            print(i**2)

def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        if (year % 100 > 0):
            leap = True
        elif (year % 400 == 0):
            leap = True
    
    return leap

def runner_up():
    n = int(input())
    arr = map(int, input().split())
    
    a = b = -100
    for i in arr:
        #print('i: ', i)
        if i > a:
            b = a
            a = i
        elif i > b and i != a:
            b = i
        #print(a,b)
    
    print(b)