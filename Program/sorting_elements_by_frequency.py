from collections import defaultdict
def sortfreq(a,n):
    d=defaultdict(lambda:0)
    for i in range(n):
        d[arr[i]] += 1
    a.sort(key=lambda x: (-d[x], x))

    return (a)

#driver fun
if__name__ == "__main__"
   arr = [a,5,2,6,-1,9999999 ,5,8,8,8]
   n= len(a)
   solution = sortfreq(a , n)
   print(*solution)

 # a-> array to be sorted 
 # n -> length of the array
 # d -> its a hashmap  
