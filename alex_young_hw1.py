# CS362 HW1
# Alex Young
# Run this file using python3 alex_young_hw1.py

n = int (input('Enter year: '))
if n % 4 == 0:
    if n % 400 == 0:
        print (n, 'is a leap year.')
    else:
        if n% 100 == 0:
            print (n, ' is not a leap year')
        else:
            print (n, 'is a leap year.')
else:
    print (n, ' is not a leap year')