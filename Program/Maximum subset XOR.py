# Python program to find
# maximum XOR subset
 
# Number of bits to
# represent int
INT_BITS=32
  
# Function to return
# maximum XOR subset
# in set[]
def maxSubarrayXOR(set,n):
 
    # Initialize index of
    # chosen elements
    index = 0
  
    # Traverse through all
    # bits of integer
    # starting from the most
    # significant bit (MSB)
    for i in range(INT_BITS-1,-1,-1):
     
        # Initialize index of
        # maximum element and
        # the maximum element
        maxInd = index
        maxEle = -2147483648
        for j in range(index,n):
         
            # If i'th bit of set[j]
            # is set and set[j] is
            # greater than max so far.
            if ( (set[j] & (1 << i)) != 0
                     and set[j] > maxEle ):
                 
                maxEle = set[j]
                maxInd = j
         
        # If there was no
        # element with i'th
        # bit set, move to
        # smaller i
        if (maxEle ==-2147483648):
            continue
  
        # Put maximum element
        # with i'th bit set
        # at index 'index'
        temp=set[index]
        set[index]=set[maxInd]
        set[maxInd]=temp
  
        # Update maxInd and
        # increment index
        maxInd = index
  
        # Do XOR of set[maxIndex]
        # with all numbers having
        # i'th bit as set.
        for j in range(n):
         
            # XOR set[maxInd] those
            # numbers which have the
            # i'th bit set
            if (j != maxInd and
               (set[j] & (1 << i)) != 0):
                set[j] = set[j] ^ set[maxInd]
         
  
        # Increment index of
        # chosen elements
        index=index + 1
     
  
    # Final result is
    # XOR of all elements
    res = 0
    for i in range(n):
        res =res ^ set[i]
    return res
 
# Driver code
 
set= [9, 8, 5]
n =len(set)
 
print("Max subset XOR is ",end="")
print(maxSubarrayXOR(set, n))
 
# This code is contributed
# by Rajat Jain.