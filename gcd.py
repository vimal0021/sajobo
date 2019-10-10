#GCD

import fractions
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The GCD of the two numbers is",fractions.gcd(a,b))







#The fractions module provides support for rational number arithmetic.

#A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.
#fractions.gcd(a, b)Return the greatest common divisor of the integers a and b.
#If either a or b is nonzero, then the absolute value of gcd(a, b)
#is the largest integer that divides both a and b.
#gcd(a,b) has the same sign as b if b is nonzero;
#otherwise it takes the sign of a. gcd(0, 0) returns 0.
