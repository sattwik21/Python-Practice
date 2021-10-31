import time

st=time.time()
l=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8]
#bubble sort
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>=l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
bs=time.time()
print("bubble sort takes "+str(bs-st)+"s")

l=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8]
#selection sort
for i in range(0,len(l)-1):
    tbc=i
    for j in range(i+1,len(l)):
        if l[j]<=l[tbc]:
            l[j],l[tbc]=l[tbc],l[j]
print(l)
ss=time.time()
print("selection sort takes "+str(ss-bs)+"s")

l=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8]
#insertion sort
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=k
print(l)
iss=time.time()
print("insertion sort takes "+str(iss-ss)+"s")

l=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,6,7]
#print(len(l))
#merge sort
def merge(arr,n):
    if n>1:
        ar1=merge(arr[0:int(n/2)],int(n/2))
        ar2=merge(arr[int(n/2):],n-int(n/2))
        lar1=int(n/2)
        lar2=n-lar1
        #print(ar1)
        #print(ar2)
        #print('"""""""""')
        ans=[]
        i,j=0,0
        for k in range(n):
            try:
                if ar1[i]<=ar2[j]:
                    ans.append(ar1[i])
                    i+=1
                else:
                    ans.append(ar2[j])
                    j+=1
            except IndexError:
                if i<=j and i<lar1:
                    ans.append(ar1[i])
                    i+=1
                elif j<=i and j<lar2:
                    ans.append(ar2[j])
                    j+=1
        return ans
    else:
        return arr
print(merge(l,len(l)))
ms=time.time()
print("merge sort takes "+str(ms-iss)+"s")

#pythons own sort function
l=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8]
l.sort()
print(l)
ns=time.time()
print("python sort() takes "+str(ns-ms)+"s")

#quick sort
#ar=[7,2,1,6,5,3,4,4]
ar=[7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8,7,2,9,9,2,4,5,6,1,8,9,8,3,6,5,2,6,8,7,3,6,7,2,8,9,7,3,6,2,7,2,8]
def partition(arr,start,end):
    #print(arr[start:end+1])
    pi=start
    for i in range(start,end):
        if arr[i]<=arr[end]:
            arr[i],arr[pi]=arr[pi],arr[i]
            pi+=1
    arr[pi],arr[end]=arr[end],arr[pi]
    #print("arr",end=" ")
    #print(arr)
    #print(pi)
    return pi

def quick_sort(arr,start,end):
    if start<end:
    	pi=partition(arr,start,end)
    	quick_sort(arr,start,pi-1)
    	quick_sort(arr,pi+1,end)

if __name__=='__main__':
    quick_sort(ar,0,len(ar)-1)
    print(ar)
qs=time.time()
print("quick sort takes "+str(qs-ms)+"s")
