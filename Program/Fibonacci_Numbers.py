#The Tribonacci sequence Tn is defined as follows: 

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# Given n, we will return the value of Tn.

def fibonacci(n):
        #if n==0, then return 0
        if(n==0 or n==1):
            return n
        
       
        # Make a list and append the first two values
        li=[]
        li.append(0)
        li.append(1)
        

        # Then using concept of Dynamic programming, append the values to the list upto n
        for i in range (2,n+1):
            li.append(li[i-2]+li[i-1])
        return li[n]


n=int(input())
print(fibonacci(n))