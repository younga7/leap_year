# CS362 HW2
# Alex Young
# 1/26/2021
# Run this file using python3 alex_young_hw2.py
# This program checks if a year is a leap year with error handling

c = 0
while c == 0:
    try:
        n = int (input('Enter year: '))
        c = 1
    except:
        print ('Error, input is not valid, try again!')
if n % 4 == 0:
    if n % 400 == 0:
        print (n, 'is a leap year.')
    else:
        if n % 100 == 0:
            print (n, 'is not a leap year.')
        else:
            print (n, 'is a leap year.')
else:
    print (n, 'is not a leap year.')