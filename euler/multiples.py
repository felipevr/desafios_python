#!/bin/python3
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below N.

import sys


def multiplo(n):
    soma = 0
    for i in range(n-1):
        num = i+1
        if (num % 3 == 0 or num % 5 == 0):
            soma += num
            #print("Numero: {} Soma: {}".format(num, soma))
            
    return soma

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(multiplo(n))
    