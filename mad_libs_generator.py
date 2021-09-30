#Mad Libs Generator

#Loop back to this point once code finishes
loop = 1
while (loop < 10):
    noun = input("Choose a number: ")
    pnoun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adj = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    print ("------------------------------------------")
    print ("Be kind to your",noun,"- legged", pnoun)
    print ("For",pnoun," may be somebody's", noun2,",")
    
    print ("This is the famous ",place,",")
    print ("Where the weather is always",adj,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is!")
    print ("------------------------------------------")

    loop = loop + 1
        