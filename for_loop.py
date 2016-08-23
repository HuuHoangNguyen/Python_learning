#!/usr/bin/python

print "====================================================================="
for letter in 'Python': #First Example
    print "Current letter :", letter

fruits = ['banana', 'apple', 'mango']
for fruit in  fruits:           #Second Example
    print 'Current fruit: ', fruit
print "END"


print "====================================================================="
for num in range(10,20):                    # to iterate between 10 to 20
    for i in range (2, num):                # to iterate on the factors of the number
        if num % i == 0:                    # to determine the first factor
            j = num/i                       # to calculate the seconf factor

            print "%d equal %d * %d" %(num, i, j)
            break                           # to move to the next number, the #first FOR
    else:
            print num, 'is a prime number'


print "====================================================================="
