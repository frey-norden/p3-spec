#!/usr/bin/env python3
# File: vacay_day.py

starting_day = int(input("What day to start on (Sun 0 - Sat 6) "))
len_of_stay = int(input("How many days? "))
return_day = (starting_day + len_of_stay) % 7
print(return_day)
