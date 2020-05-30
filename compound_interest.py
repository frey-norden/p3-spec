#!/usr/bin/env python3
# File: compound_interest.py

# A = P*((1 + (r/n))**(nt))
P = 10000
n = 12
r = 0.08
t = int(input('Enter number of years: '))
A = P*((1 + (r/n))**(n*t))
print(round(A, 2))
