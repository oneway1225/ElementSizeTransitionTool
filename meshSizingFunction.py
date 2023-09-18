## Step 1 - Importing necessary libraries

import numpy as np
import math
from operator import add


## Function definition

def sizeFunction(S1, S2, L):
    ## Step 2 - Initialise Values
    elementList = [] # Create a new empty list for elements to fill the gap 
    
    numElements = int(2*L / (S1 + S2)) # Estimate the number of elements needed to fill the gap (needs to be an integer)
    if numElements == 0: numElements = 1 # Cannot have 0 elements, so by default you need at least one element to fill the gap

    rate = (S2 - S1) / numElements # Estimate the growth rate of how the element size is going to grow
    
    maxLimit = max(S1, S2) # Determine the maximum limit for the elements

    ## Step 3 - Calculate Initial Sizes of the Filler Elements
    ## Special Case when only one element is needed to fill the gap:
    if numElements == 1:
        elementList.append(L) ## There is only one element and its size cannot be larger than the gap length, so has to equal L
        totalLength = L
    
    ## For any other cases that require more than one element to fill the gap:
    else:    
        for i in range(numElements):
            elementList.append(S1 + (i+1) * rate) ## This is the initial estimate of element sizes, assuming arithematic series and initial estimated growth rate
                
    ## Step 4 - Check for Errors
        totalLength = sum(elementList) ## This value is likely to exceed L    
        count = sum(1 for x in elementList if x >= maxLimit) ## Count the number of elements with a sizer larger than the maximum limit. The size of these elements will need to be reduced to the maximum limit

    ## Step 5 - Refine the Element Sizes
        while abs(totalLength - L) > 0.0001 or count > 0 and rate != 0: ## Triggered when the totalLength sum of element sizes is not equal to L, or if there is an element larger than the maximum limit
            remainder = L - totalLength
            remainder = (remainder / (numElements - count)) ## The remainder needs to be re-distributed between those elements that are less than the maximum size limit

            elementList = [x + remainder if x < maxLimit else maxLimit for x in elementList] ## Re-distribute the remainder - if the element size is larger than Smax, then change it to Smax
            totalLength = sum(elementList)
            count = sum(1 for x in elementList if x > maxLimit) ## Check that there is no element that exceeds the size limit, otherwise continue the while loop
 
    return "The list of new element sizes: ", elementList, "The number of elements required: ", numElements, "totalLength sum of new elements: ", totalLength


## Testing
# TC01
#sizeFunction(1,1,10)

# TC02
#sizeFunction(1,5,3)

# TC03
#sizeFunction(1,3,0.5)

# TC04
#sizeFunction(1,2,10)

# TC05
#sizeFunction(1,2,30)

# TC06
# sizeFunction(2,1,10)

# TC07
sizeFunction(1,10,20)