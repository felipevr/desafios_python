#!/bin/python
#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

def main_loop(x, y, z, n):
    x += 1
    y += 1
    z += 1

    l = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+j+k) != n:
                    l.append([i,j,k])
                    
    print(l)

def main_list_c(x, y, z, n):
    x += 1
    y += 1
    z += 1
    l = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if (i+j+k) != n]
    print(l)
    

main_list_c(3,3,3,5)