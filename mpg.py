#!/usr/bin/env python3
# File: mgp.py

def mpg():
    miles = float(input('Enter number of miles: '))
    gallons = float(input('Enter gallons used: '))
    def MPG(miles, gallons):
        mpg = miles / gallons
        return round(mpg, 1)

    print('The miles per gallon is:',MPG(miles,gallons))

def main():
    mpg()

if __name__ == "__main__":
    main()
