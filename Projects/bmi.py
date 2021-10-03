weight = float(input("Input your Weight(Kg): "))
height = float(input("Input your Height(mt): "))

bmi = (weight/height)/height
print("Your BMI is :", bmi)

if (bmi>0):
        if (bmi<=16):
            print("you are severely underweight")
        elif (bmi<=18.5):
            print("you are underweight")
        elif (bmi<=25):
            print("you are Healthy")
        elif (bmi<=30):
            print("you are overweight")
        else: 
            print("you are severely overweight")
else:
    print("Enter valid details")
