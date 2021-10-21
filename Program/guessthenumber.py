import random
 
max = 10
secretNumber = random.randrange(1, max)
 
rispostaUtente = int(input("Insert a number: "))
 
if rispostaUtente == secretNumber:
    print("You guessed it! \^o^/")
elif rispostaUtente < secretNumber:
    print("The number is too low, you lost.  ╯︿╰")
else:
    if rispostaUtente > max:
        print("You have entered a number that is out of range.")
    else:
        print("The number is too high, you lost.  ＞﹏＜")
