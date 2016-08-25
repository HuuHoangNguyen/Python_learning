#!/usr/bin/python

# Random numbers are used for games. simulations, testing, security, and privacy applications.
# Python includes following functions that are commonly used
import random
print "==================================================================="
print "choice(seq): a random item from a list, tuple, or string "

print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A string') : ", random.choice('A string')

print "==================================================================="
print "randrange([start, ] stop [,step]) : returns a randomly selected element from range(start, stop, step)"
# Select an even numbers in 100 <= number < 10000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)
#Select another numbers in 100 <=  number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

print "==================================================================="
print "random(x): a random float r, such that o is less than or equal to r and r s less than 1"
# First random number
print "random() : ", random.random()
# Second random number
print "random() : ", random.random()

print "==================================================================="
print " seed([x]): Set the integer starting value use in generating random numbers "
print " Call this functions before calling any other random module function. Return None"
random.seed(10)
print "Random number with seed 10 : ", random.random()
# It will generate sam random number
random.seed(10)
print "Random number with seed 10 : ", random.random()
# It will generate same random number
random.seed(10)
print "Random number with seed 10 : ", random.random()

print "==================================================================="
print "shuffle(lst): Randomizes the items of a list in place. Return None"
list = [20, 16, 10, 5]
random.seed(100)
random.shuffle(list)
print "Resheffled list : ", list
random.seed(199)
random.shuffle(list)
print "Reshuffed list : ", list

print "==================================================================="
print "uniform(x, y): a=A random float r, such that x is less than or equal to r and r is less than y"
print "Random float uniform(5, 10) : ", random.uniform(5, 10)
print "Random float uniform(7, 14) : ", random.uniform(7, 14)
