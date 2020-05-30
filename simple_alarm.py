#!/usr/bin/env python3
# File: simple_alarm.py

alarm = int(input('Enter number of hours: '))
current_time = int(input('Enter current hour: '))
new_time = (alarm % 24) + current_time
print(new_time)
