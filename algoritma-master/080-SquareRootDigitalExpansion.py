#!/usr/bin/python3
# -*- coding: utf-8 -*-
# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

from math import sqrt
from decimal import *

getcontext().prec = 110
toplam = 0
for m in range(2,100):
    if(int(sqrt(m))**2!=m):
        toplam += int(str(Decimal(m).sqrt()).split(".")[0])
        n = str(Decimal(m).sqrt()).split(".")[1][:99]
        for i in n:
            toplam += int(i)
print(toplam)
