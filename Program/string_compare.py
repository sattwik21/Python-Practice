# This program takes two strings and compares them to see which one has a larger value. It essentially does what strcmp would do in C++. It compares each character of both strings and if they are equal, it goes to the next character. If one is larger than another, then it returns that the string with the larger character is bigger than the string with the smaller. And by larger and smaller, it is referring to the binary value of the characters. Case-insensitive


# case_insensitive string compare
def str_cmp(str1, str2):
    if str1.lower() > str2.lower():
        print(str1 + " is greater than " + str2)
        return 1
    elif str1.lower() < str2.lower():
        print(str2 + " is greater than " + str1)
        return 0
    else:
        print("The strings are equal")
        return


# driver
s1 = 'Bath'  # t > r, thus Bath is greater than Bark
s2 = 'Bark'

str_cmp(s1, s2)

# since function is case-insensitive, these will be equal to the function
j = str_cmp("Jill", "jIlL")  # returns none since they are equal
print(j)
