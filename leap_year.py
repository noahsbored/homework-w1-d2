leap = int(input('enter a year'))4


if leap % 4 == 0 and (leap %100 != 0 or year % 400 ==  0) :    
    print (its a leap year)
else:
    print ('not a leap year')