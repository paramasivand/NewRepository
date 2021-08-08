######################################################
# Program Name     : Standard Deviation
# Author           : Paramasivan Dorai
# Date             : 28-Jul2019
# Input Parameters : Number of items
# Description      : Standard Deviation
#######################################################

import array
import sys
import cmath

ArrayLength_int = 0
fMean = 0.0
iSum = 0
iSum1 = 0
fStdDev = 0.0
fSqrRt = 0.0

while True :
    ArrayLength = input ()
    ArrayLength_int = int(ArrayLength)
    if ArrayLength_int < 5:
        print ('Please enter a value between 10 and 100')
        iVal = 1
        exit
    elif ArrayLength_int >100:
        print ('Please enter a value between 10 and 100')
        iVal = 1
        exit
    else :
        break


StdDev = array.array('q')

istr = input().split(' ')

StdDev = [int(num) for num in istr]

ArrayLength_int = len(StdDev)

for i in range(0,ArrayLength_int):
    iSum = iSum + StdDev[i]

fMean = iSum / ArrayLength_int

for i in range (0,ArrayLength_int):
    iSum1 = iSum1 + ((fMean - StdDev[i]) * (fMean - StdDev[i]))

fStdDev = cmath.sqrt(iSum1/ArrayLength_int)

print (round(fStdDev.real,1) + round(fStdDev.imag,1))
