######################################################
# Program Name     : Inter Quartile Range
# Author           : Paramasivan Dorai
# Date             : 28-Jul2019
# Input Parameters : Number of items and input
# Description      : IQR calculation
#######################################################

import array
import sys
import statistics


ArrayLength_int = 0
iSum = 0
iSum1 = 0
iMiddle_element = 0
iMedianArr = array.array('q')
iTempArr = array.array('q')
iTempArr1 = array.array('q')
iTargetArr = array.array('q')
iTargetArr_FH = array.array('q')
iTargetArr_SH = array.array('q')
deff_arr = array.array('q')
iDataSetArr = array.array('q')
iTemp = 0
iDataSetArrLength = 0
MinNumber = 100000
fMedian_Func = 0.0
fMedian = 0.0
fMedian_Lower = 0
fMedian_Upper = 0

### Defenition
### Sort Function
def bsort (deff_arr) :
    iTargetFuncArr = array.array('q')
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
        iTargetFuncArr.append(MinNumber)
        iCounter = 0
        MinNumber = 100000
    return (iTargetFuncArr)

### Median Function

def Median_Func (deff_arr) :
    deff_arr = bsort(deff_arr)
    MF_Len = len(deff_arr)
    if MF_Len == 2:
        fMedian_Func = (deff_arr[0] + deff_arr[1]) / 2
    elif MF_Len%2 == 0:
        fMedian_Func = (deff_arr[int(MF_Len/2)] + deff_arr[int(MF_Len/2 - 1)]) / 2
    else :
        fMedian_Func = deff_arr[int(MF_Len/2)]
    return fMedian_Func

############### Input Parameters #####################

##### Getting the Lenth of the Array #########

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


##### Getting the initial values #########

iStr = input().split(' ')

iMedianArr = [int(num) for num in iStr]

ArrayLength_int = len(iMedianArr)

iVal = 0

##### Validation of the array elements #########

for i in range(0,ArrayLength_int):
    if iMedianArr[i] <= 0 :
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

##### Getting the Frequency Input #########

iStr = input().split(' ')

iCountArr = [int(num) for num in iStr]

iCountArrayLength = len(iCountArr)

iVal = 0

##### Validation of the frequency array elements #########

for i in range(0,iCountArrayLength):
    if iCountArr[i] <= 0 :
        iVal = 1
        print ("Invalid Number at %i th element" %i)
        exit
    elif iCountArr[i] > 1000 :
        iVal = 1
        print ("Invalid number at %i th element" %i)
        exit
    else :
        iVal = 0

if iVal == 1 :
    sys.exit

########## Taking a Copy of the Main Array ##########

for i in range (0,ArrayLength_int) :
    iTempArr.append(iMedianArr[i])

#fMedian = Median_Func(iTempArr)
#print (fMedian) # This will be Q2 which is not required for this program

######### For Loop to form the final data set i.e. Repeat elements by frequency #######

for i in range(0,ArrayLength_int) :
    for j in range(0,iCountArr[i]) :
        iDataSetArr.append(iMedianArr[i])

########## Length of the Final Data set ##########

iDataSetArrLength = len(iDataSetArr)

########## Taking a Copy of the Main Array ##########

for i in range (0,iDataSetArrLength) :
    iTempArr1.append(iDataSetArr[i])

########## Median of the Final Data Set ##########

fMedian = Median_Func(iTempArr1)


#print (iDataSetArr)
#print (iCountArr)
#print (iMedianArr)
#print (fMedian)
#print ("dataset before Sort")
#print (iDataSetArr)

########## Sorting the Final Data Set ##########

iDataSetArr = bsort (iDataSetArr)

#print ("dataset after Sort")
#print (iDataSetArr)
#print ("length of array")
#print (iDataSetArrLength)

########## Finding the middle element ##########

iMiddle_element = (int(iDataSetArrLength/2))

########## IQR calculation ##########

if iDataSetArrLength%2 == 0 :
    for i in range (0,iDataSetArrLength) :
        if i < iDataSetArrLength/2 :
            iTargetArr_FH.append(iDataSetArr[i])
        elif i > iDataSetArrLength/2 :
            iTargetArr_SH.append(iDataSetArr[i])

elif iDataSetArr[iMiddle_element] == fMedian :
    for i in range (0,iDataSetArrLength) :
        if i < iMiddle_element :
            iTargetArr_FH.append(iDataSetArr[i])
        elif i > iMiddle_element :
            iTargetArr_SH.append(iDataSetArr[i])

else :
    for i in range (0,iDataSetArrLength) :
        if iDataSetArr[i] < fMedian :
            iTargetArr_FH.append(iDataSetArr[i])
        elif iDataSetArr[i] > fMedian :
            iTargetArr_SH.append(iDataSetArr[i])

#print (fMedian)
#print (iTargetArr_FH)
#print (iTargetArr_SH)

fMedian_Lower = Median_Func(iTargetArr_FH)

#print (fMedian_Lower)

fMedian_Upper = Median_Func(iTargetArr_SH)

#print (fMedian_Upper)

print (float(fMedian_Upper - fMedian_Lower))
