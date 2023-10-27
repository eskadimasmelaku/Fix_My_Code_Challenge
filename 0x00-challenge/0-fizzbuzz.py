#!/usr/bin/python3
""" FizzBuzz
"""

import sys

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

if len(sys.argv) != 2:
    print("Usage: ./0-fizzbuzz.py <n>")
else:
    n = int(sys.argv[1])
    fizz_buzz(n)
