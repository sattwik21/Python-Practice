str1 = input()
str2 = input()
str1 = str1.lower()
str2 = str2.lower()
list1 = []
list2 = []

for char in str1:
    if char.isalpha() == True: #Only accepts alphabets and adds them to the list
        list1.append(char)
        
for char in str2:
    if char.isalpha() == True:
        list2.append(char)

if(sorted(list1) == sorted(list2)): #To check if both strings use exact same alphabets
    print("Given strings are anagrams.", end="")
else:
    print("Given strings are not anagrams.", end="")   