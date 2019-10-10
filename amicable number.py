x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j
if(sum1==y and sum2==x):
    print("Amicable!")
else:
    print("Not Amicable!")

'''
Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number.
he smallest pair of amicable numbers is (220, 284). They are amicable because the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.

The first ten amicable pairs are: (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416), (63020, 76084), and (66928, 66992).
Amicable numbers were known to the Pythagoreans, who credited them with many mystical properties. A general formula by which some of these numbers could be derived was invented circa 850 by the Iraqi mathematician Thābit ibn Qurra (826–901)
It states that if

p = 3×2(n − 1) − 1,
q = 3×2(n − 1),
r = 9×2(2(n − 1 ))− 1,
where n > 1 is an integer and p, q, and r are prime numbers, then 2n×p×q and 2n×r are a pair of amicable numbers. This formula gives the pairs (220, 284) for n = 2, (17296, 18416) for n = 4, and (9363584, 9437056) for n = 7, but no other such pairs are known. Numbers of the form 3×2n − 1 are known as Thabit numbers. In order for Ibn Qurra's formula to produce an amicable pair,
two consecutive Thabit numbers must be prime; this severely restricts the possible values of n.

To establish the theorem, Thâbit ibn Qurra proved nine lemmas divided into two groups. The first three lemmas deal with the determination of the aliquot parts of a natural integer. The second group of lemmas deals more specifically with the formation of perfect, abundant and deficient numbers.
'''
