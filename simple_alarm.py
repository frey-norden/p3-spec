#!/usr/bin/env python3
# File: simple_alarm.py

def alarm():
    '''Alarm prompts user for number of hours till alarm. Takes integers,
    returns time alarm will go off. Assumes 24 hour clock.'''

    alarm = int(input('Enter number of hours: '))
    current_time = int(input('Enter current hour: '))
    new_time = (alarm % 24) + current_time
    if new_time > 24:
        new_time -= 24
    return new_time

def main():
    print(alarm())

if __name__ == "__main__":
    main()
