#The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, we will return the value of Tn.

def tribonacci(n):
        #if n==0, then return 0
        if(n==0):
            return 0
        
        #if n==1 or n==2 return 1
        elif(n==1 or n==2):
            return 1

        # Make a list and append the first three values
        li=[]
        li.append(0)
        li.append(1)
        li.append(1)

        # Then using concept of Dynamic programming, append the values to the list upto n
        for i in range (3,n+1):
            li.append(li[i-2]+li[i-1]+li[i-3])
        return li[n]


n=int(input())
print(tribonacci(n))