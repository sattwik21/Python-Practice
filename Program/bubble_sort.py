def bubble_sort(arr):
   arr_size = len(arr)

   for i in range (arr_size-1):
      for j in range(0, arr_size-1):
         if arr[j] > arr[j+1]: 
            arr[j], arr[j+1] = arr[j+1], arr[j]



# test array
arr = [3, 8, 2, 10, 23, 2, 50]
bubble_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i]),