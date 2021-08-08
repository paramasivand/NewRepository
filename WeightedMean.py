################################################################
# Prgram Name      : Weighted Mean
# Author           : Paramasivan Dorai
# Date             : 28-Jul-2019
# Input Parameters : Contains number of inputs in the array
# Description      : The program accepts an array of intigers and
#                    the weightage and prints the weighted mean
###############################################################

import array
import sys

i = 0
iSum = 0
iSum1 = 0
MinNumber = 100000
iCounter = 0
iMiddle_1 = 0
iMiddle_2 = 0
fMedian = 0.0
fMean = 0.0
iVal = 0

while True :
    ArrayLength = input ()
    ArrayLength_int = int(ArrayLength)
    if ArrayLength_int < 5:
        print ('Please enter a correct value')
        iVal = 1
        exit
    elif ArrayLength_int >50:
        print ('Please enter a value between 10 and 2500')
        iVal = 1
        exit
    else :
        break

#ArrayLength_int = int(ArrayLength)

MeanArr = array.array('q')
WeightArr = array.array('q')
istr = input ().split (' ')
MeanArr = [int(num) for num in istr]


ArrayLength_int = int(len(MeanArr))
iVal = 0

for i in range(0,ArrayLength_int) :
    if MeanArr[i] < 0:
        print("Invalid Number at element %i" %i)
        iVal = 1
    elif MeanArr[i] > 100000:
        print("Invalid Number at element %i" %i)
        iVal = 1

if iVal == 1:
    sys.exit()

istr = input ().split (' ')
WeightArr = [int(num) for num in istr]

ArrayLength_int1 = int(len(WeightArr))

iVal = 0

for i in range(0,ArrayLength_int1) :
    if WeightArr[i] < 0:
        print("Invalid Number at element %i" %i)
        iVal = 1
    elif WeightArr[i] > 100000:
        print("Invalid Number at element %i" %i)
        iVal = 1

if iVal == 1:
    sys.exit()

for j in range (0, ArrayLength_int):
    iSum = iSum + (MeanArr[j] * WeightArr[j])
    iSum1 = iSum1 + WeightArr[j]

#print ("\n***********************************************************")

#print ("The Sum of the numbers in the array is : %i" %iSum)

fMean = iSum / iSum1

#print ("\n***********************************************************")

print(round(fMean,1))

#print ("\n***********************************************************")
