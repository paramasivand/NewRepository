################################################################
# Prgram Name      : MeanMedianMode
# Author           : Paramasivan Dorai
# Date             : 14-June-2019
# Input Parameters : Contains number of inputs in the array
# Description      : The program accepts an array of intigers and
#                    prints the mean median mode of the numbers
###############################################################

import array
import sys

i = 0
iSum = 0
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
    if ArrayLength_int < 10:
        print ('Please enter a correct value')
        iVal = 1
        exit
    elif ArrayLength_int >2500:
        print ('Please enter a value between 10 and 2500')
        iVal = 1
        exit
    else :
        break

#ArrayLength_int = int(ArrayLength)

MinMaxArr = array.array('q')
Temp_Arr = array.array('q')
Target_Arr = array.array('q')

istr = input ().split (' ')

#print (istr)

MinMaxArr = [int(num) for num in istr]

ArrayLength_int = int(len(MinMaxArr))

iVal = 0

for i in range(0,ArrayLength_int) :
    if MinMaxArr[i] < 0:
        print("Invalid Number at element %i" %i)
        iVal = 1
    elif MinMaxArr[i] > 100000:
        print("Invalid Number at element %i" %i)
        iVal = 1

if iVal == 1:
    sys.exit()

#for i in range (0, ArrayLength_int):
#    k = input ("\n Please enter the value for the element %i :" %i )
#    MinMaxArr.append(int(k))

for j in range (0, ArrayLength_int):
    iSum = iSum + MinMaxArr[j]

#print ("\n***********************************************************")

#print (MinMaxArr)

#print ("\n***********************************************************")

#print ("The Sum of the numbers in the array is : %i" %iSum)

fMean = iSum / ArrayLength_int

#print ("\n***********************************************************")

print(round(fMean,1))

#print ("\n***********************************************************")


###########################################################################
### Median Calculation
###########################################################################

for i in range(0,ArrayLength_int):
    Temp_Arr.append(MinMaxArr[i])

#print(Temp_Arr)

iCount = ArrayLength_int

for m in range (0, ArrayLength_int):
    for l in range (0 , iCount):
        if  Temp_Arr[l] < MinNumber:
            MinNumber = Temp_Arr[l]
            iCounter = l
    Temp_Arr.pop(iCounter)
#    print (Temp_Arr)
    iCount = iCount - 1
    Target_Arr.append(MinNumber)
    iCounter = 0
    MinNumber = 100000

#print (MinMaxArr)
#print (Temp_Arr)
#print (Target_Arr)

if ArrayLength_int%2 == 0:
    iMiddle_1 = (ArrayLength_int / 2) - 1
    iMiddle_2 = iMiddle_1 + 1
    fMedian = (Target_Arr[int(iMiddle_1)] + Target_Arr[int(iMiddle_2)]) / 2
    #print (fMedian)
else:
    iMiddle_1 = (ArrayLength_int/2)
    fMedian = Target_Arr[int(iMiddle_1)]


print (round(fMedian,1))

###########################################################################
### Mode Calculation
###########################################################################

iCount_maxoccr = 0
iMode = 0

for m in range (0, ArrayLength_int):
    iCount_occr = 0
    for l in range (0 , ArrayLength_int):
        if Target_Arr[m] == Target_Arr[l]:
            iCount_occr = iCount_occr + 1
    if iCount_occr > iCount_maxoccr:
        iMode = Target_Arr[m]
        iCount_maxoccr = iCount_occr

if iCount_maxoccr == 1:
    #print ("\n***********************************************************")
    iMode = Target_Arr[0]
    print (iMode)
else :
    #print ("\n***********************************************************")
    print (iMode)

#print ("\n***********************************************************")
#print (MinMaxArr)
#print (Target_Arr)
