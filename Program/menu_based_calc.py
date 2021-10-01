# Program to implement a menu based calculator
#It makes use of functional programming concept and handles all the possible errors.
#Contributed by Ahamed Ruyefa

# Function to Add integers
def addIntegers(a, b):
    return a + b


# Function to Subtract integers
def subtractIntegers(a, b):
    return a - b


# Function to Multiply integers
def multiplyIntegers(a, b):
    return a * b


# Function to Divide integers
def divideIntegers(a, b):
    if b == 0:
        return "Divide by zero error"
    return a / b


# Function to get user input
def getIntegers():
    print("Enter two integers with a space between them. eg: 15 20")
    try:
        a, b = input("Enter num1 and num2: ").strip().split()
        a = int(a)
        b = int(b)
        return a, b
    except:
        return "Invalid input"


# Function to Display Menu
def printMenu():
    print("Menu based calculator")
    print("1. Addition of Integers")
    print("2. Subtraction of Integers")
    print("3. Multiplication of Integers")
    print("4. Division of Integers")
    print("5. Evaluation of Expression")


# Function to get User choice
def getChoice():
    try:
        return int(input("Choose your option: "))
    except ValueError:
        return 0


if __name__ == "__main__":
    repeat = True
    while repeat:
        printMenu()
        choice = getChoice()

        if choice in range(1, 5):
            try:
                a, b = getIntegers()
                if choice == 1:
                    print(addIntegers(a, b))
                elif choice == 2:
                    print(subtractIntegers(a, b))
                elif choice == 3:
                    print(multiplyIntegers(a, b))
                elif choice == 4:
                    print(divideIntegers(a, b))
            except:
                print("NAN")
        elif choice == 5:
            expression = input("Enter expression to evaluate: ")
            try:
                print(eval(expression))
            except:
                print("NAN")
        else:
            print("Invalid choice")

        if input("Continue? (y/n): ") in ["y", "Y"]:
            repeat = True
        else:
            repeat = False
