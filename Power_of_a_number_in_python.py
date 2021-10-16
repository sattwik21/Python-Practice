def power(base,exp):#function declaration 
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))
base=int(input("Enter the base number.."))
exp=int(input("Enter the exponential value.."))
print("Result:",power(base,exp))#Calling the function