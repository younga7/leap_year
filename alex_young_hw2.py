# CS362 HW1
# Alex Young
# Run this file using python3 alex_young_hw2.py

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