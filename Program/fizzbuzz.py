n = int(input("Enter number : "))

if num%5 == 0 and num%3 == 0: #Needs to be checked first, otherwise multiples of 3 and 5 will be printed as Fizz
	print(num, "- FizzBuzz")
elif num%3 == 0:
        print(num, "- Fizz")
elif num%5 == 0:
	print(num, "- Buzz")
else:
        print("Neither fizz nor buzz")