######################################################
# Program Name     : Quartile (Integer)
# Author           : Paramasivan Dorai
# Date             : 28-Jul2019
# Input Parameters : Number of items and input
# Description      : Quartile calculation
#######################################################

import array
import sys


ArrayLength_int = 0
iSum = 0
iSum1 = 0
iMedianArr = array.array('q')
iTempArr = array.array('q')
iTargetArr = array.array('q')
iTargetArr_FH = array.array('q')
iTargetArr_SH = array.array('q')
deff_arr = array.array('q')
iTemp = 0
MinNumber = 100000
iMedian = 0
iMedian_Lower = 0
iMedian_Upper = 0

### Defenition

def bsort (deff_arr) :
    MinNumber = 100000
    iCount = len(deff_arr)
    iCount1 = len(deff_arr)
    for i in range (0 , iCount1) :
        for j in range (0, iCount) :
            if deff_arr[j] < MinNumber :
                MinNumber = deff_arr[j]
                iCounter = j
        deff_arr.pop(iCounter)
        iCount = iCount - 1
        iTargetArr.append(MinNumber)
        iCounter = 0
        MinNumber = 100000
    return (iTargetArr)

### Getting the Lenth of the Array

iVal = 0

while True:
    ArrayLength = input()
    ArrayLength_int = int(ArrayLength)
    if ArrayLength_int < 5 :
        iVal = 1
        print("Please Enter a valid value")
        exit
    elif ArrayLength_int > 50 :
        iVal = 1
        print ("Please Enter a valid value")
        exit
    else :
        iVal = 0
        break

if iVal == 1:
    sys.exit

#print (ArrayLength_int)

iStr = input().split(' ')

iMedianArr = [int(num) for num in iStr]

ArrayLength_int = len(iMedianArr)

iVal = 0

for i in range(0,ArrayLength_int):
    if iMedianArr[i] < 0 :
        iVal = 1
        print ("Invalid Number at %i th element" %i)
        exit
    elif iMedianArr[i] > 100 :
        iVal = 1
        print ("Invalid number at %i th element" %i)
        exit
    else :
        iVal = 0

if iVal == 1 :
    sys.exit

for i in range (0,ArrayLength_int) :
    iTempArr.append(iMedianArr[i])

iTempArr = bsort (iTempArr)
if ArrayLength_int == 2 :
    iMedian = (iTempArr[0] + iTempArr[1]) / 2
elif ArrayLength_int%2 == 0:
    iMedian = (iTempArr[int(ArrayLength_int/2)] + iTempArr[int(ArrayLength_int/2 - 1)]) / 2
else :
    iMedian = iTempArr[int(ArrayLength_int/2)]

for i in range(0,ArrayLength_int) :
    if iTempArr[i] < iMedian :
        iTargetArr_FH.append(iTempArr[i])
    elif iTempArr[i] > iMedian :
        iTargetArr_SH.append(iTempArr[i])

iArrayLength_FH = len(iTargetArr_FH)
if iArrayLength_FH == 2:
    iMedian_Lower = (iTargetArr_FH[0] + iTargetArr_FH[1]) / 2
elif iArrayLength_FH%2 == 0:
    iMedian_Lower = (iTargetArr_FH[int(iArrayLength_FH/2)] + iTargetArr_FH[int(iArrayLength_FH/2 - 1)]) / 2
else :
    iMedian_Lower = iTargetArr_FH[int(iArrayLength_FH/2)]

iArrayLength_SH = len(iTargetArr_SH)
if iArrayLength_SH == 2:
    iMedian_Upper = (iTargetArr_SH[0] + iTargetArr_SH[1])/2
elif iArrayLength_SH%2 == 0:
    iMedian_Upper = (iTargetArr_SH[int(iArrayLength_SH/2)] + iTargetArr_SH[int(iArrayLength_SH/2 - 1)]) / 2
else :
    iMedian_Upper = iTargetArr_SH[int(iArrayLength_SH/2)]

print(int(iMedian_Lower))
print (int(iMedian))
print(int(iMedian_Upper))
