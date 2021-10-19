#python program to find a number from  a list of numbers using Linear search

#Input list from the user
lis=eval(input("Enter the list of numbers"))

#Input the  number to be searched
N=int(input("Enter the number to be searched"))
 
#Traverse through the list
for i in lis:
    if i==N:
        print("The number is found",i)
        break
else:   
    print("The number is not found")    