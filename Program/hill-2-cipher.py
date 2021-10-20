"""
Implementation of Hill 2-Cipher!
Important notation:
K = Matrix which is our 'Secret Key'
P = Vector of plaintext (that has been mapped to numbers)
C = Vector of Ciphered text (in numbers)
C = E(K,P) = K*P (mod X) -- X is length of alphabet used
P = D(K,C) = inv(K)*C (mod X)  -- X is length of alphabet used
Assumption: the texts are made up of small letters and space only
            K = [[1, 4], [0, 11]]
"""

import numpy as np

#egcd is extended euclidean algorithm, ax + by = gcd(a,b) it will return gcd, x and y where gcd is euclidean algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

alphabet = "abcdefghijklmnopqrstuvwxyz " # 27 characters
#each letter in the alphabet string is assigned a numeric value starting for 0.
#a = 0, b =1, c = 3, ......
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
#vice versa of letter_to_index
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def matrix_mod_inv(matrix, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
    in this case: extended euclidean algorithm is
    determinant * x + modulus * y = gcd(determinant, modulus)
    egcd function will returns gcd, x , y
    egcd(det, modulus)[1] is x in this case
    matrix used in our key matrix, k = [[1, 4], [0, 11]]
    """
    # Step 1) find the det of key matrix and convert it to int
    # det is 11
    det = int(np.round(np.linalg.det(matrix)))  
    # Step 2)
    # egcd function will return (1,5,-2) if det = 11, modulus = 27
    # egcd(det, modulus)[1] is the second value which is 5
    det_inv = egcd(det, modulus)[1] % modulus  
    # Step 3)
    #formula = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) = [[55 -20], [0 5]]
    #np.linalg.inv is inverse of the matrix
    #convert det * the inverse of the matrix to type integer
    #in python, (a+b)mod n = [(a mod n)+(b mod n)]mod n 
    #hence for negative modulo,  -20% 27 = (-27 + 7) mod 27 = [(-27 mod 27) + 7 mod 27] mod 27 = 7 mod 27 = 7d
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    ) 
    
    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []
    # convert the each alphabet in the plaintext to assigned number
    for letter in message:
        message_in_numbers.append(letter_to_index[letter])
    #Plaintext is split into pairs and converted into vector column, v.
    split_P = [
        message_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0])) #K.shape[0] is 2, hence the split_P will form (1,1) or (1,2) vector for each row
    ]
    #for either (1,2) or (1,1) vector in each row after splitting it.
    for P in split_P:
        #transpose the array to vector column , np.asrray is convert input to an array
        #[:, np.newaxis] is used to increase the dimension of the existing array
        P = np.transpose(np.asarray(P))[:, np.newaxis] 

        #if the shape of P and K are not the same( in other words, if P is not (2,1) array), then add space letter to the P to make sure it is an (2,1) array.
         #usually occur for odd characters in a plaintext
        while P.shape[0] != K.shape[0]: 
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]


        #To encipher each pair, we perform matrix multiplication, K*P, K is key matrix and P is the splitted text and then mod 27
        numbers = np.dot(K, P) % len(alphabet) # mod 27



        n = numbers.shape[0]  # length of encrypted message (in numbers)



        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0]) #the 0 is because P is 2-d array, it is like read the first element at each row

            encrypted += index_to_letter[number] # convert that assigned number back to the alphabet and add it to the encrypted string.

    return encrypted


def decrypt(cipher, Kinv):
    #it is the same methods as decrypt
    #the only difference is we are using inverse key matrix which is 
    decrypted = ""
    cipher_in_numbers = []

    #convert the encrypted alphabets to assigned number
    #Encrypted text is split into pairs and converted into vector column, v
    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])
    
    split_C = [
        cipher_in_numbers[i: i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ] #Kinv.shape[0] is 2, hence the split_P will form (1,1) or (1,2) vector for each row

    #for (1,2) vector in each row after splitting it.
    for C in split_C:
        #transpose the array to vector column , np.asrray is convert input to an array
        #[:, np.newaxis] is used to increase the dimension of the existing array
        C = np.transpose(np.asarray(C))[:, np.newaxis]

        #the encrypted text confirm has even characters. Hence, no need to check whether the spiltted text is (2,1) array or not

         #To decrypt each pair, we perform matrix multiplication, Kinv*C, Kinv is inverse key matrix and C is the splitted text and then mod 27
        numbers = np.dot(Kinv, C) % len(alphabet)



        n = numbers.shape[0] # length of decrypted message (in numbers)



        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0]) #the 0 is because P is 2-d array, it is like read the first element at each row
            decrypted += index_to_letter[number] # convert that assigned number back to the alphabet and add it to the decrypted string.


    return decrypted






K = np.matrix([[1, 4], [0, 11]]) # for length of alphabet = 27

Kinv = matrix_mod_inv(K, len(alphabet))
#Kinv = np.matrix([[1, 7], [0, 5]])


from tkinter import *
root = Tk()
root.title("Hill 2-Cipher")

# creating a label widget
mylabel1 = Label(
    root, text="This program is showing the implementation of Hill 2-Cipher").grid(row=0, column=0)

mylabel2 = Label(
    root, text="There are 2 assumptions in this Hill 2-Cipher program\n").grid(row=1, column=0)

mylabel3 = Label(root, text="1. The input texts are made up of small letters and space only.").grid(
    row=2, column=0)

mylabel4 = Label(root, text="Each letter in the alphabet string is assigned a numeric value starting for 0.").grid(
    row=3, column=0)

mylabel5 = Label(root, text="a = 0, b =1, c = 3, ...... and end with space letter = 26.").grid(
    row=4, column=0)
mylabel6 = Label(
    root, text="2. The key matrix that we are using in this program is , K = [[1, 4], [0, 11]]\n\n\n").grid(
    row=5, column=0)
myLabel7 = Label(root, text="Enter the plaintext:").grid(row=6, column=0)
message = Entry(root, width=40, borderwidth=5)
message.grid(row=7, column=0)
# default text inside the text box
message.insert(0, "enter the plaintext")

encrypted = Entry(root, width=40, borderwidth=5)
encrypted.grid(row=12, column=0)

decrypted = Entry(root, width=40, borderwidth=5)
decrypted.grid(row= 18, column = 0)
def myClick():
    encrypted_message = encrypt(message.get(), K)
    # e.get() return watever we input in the input field
    encrypted.delete(0, END)  # to clear the screen
    encrypted.insert(0, encrypted_message)

    decrypted_Message =decrypt(encrypted_message, Kinv)
    decrypted.delete(0, END)  # to clear the screen
    decrypted.insert(0, decrypted_Message)
    myLabel13 = Label(root,text ="\nDecrypted message from the encrypted plaintext and the plaintext are the same.").grid(row=19,column = 0)
    myLabel14 = Label(root,text ="This means our program can decrypt and encrypt the text.").grid(row=20,column = 0)

    


space = Label(root, text="").grid(row=8, column=0)
# the encrypt button
myButton = Button(root, text="Encrypt the text!", command=myClick, cursor="hand2")
myButton.grid(row=9, column=0)
# the output button
space2 = Label(root, text="").grid(row=10, column=0)
myLabel8 = Label(root, text="Encrypted text: ").grid(row=11, column=0)
myLabel9 = Label(root, text="").grid(row=13, column=0)
space3 = Label(root, text="").grid(row=14, column=0)
myLabel10 = Label(root, text="Since we can encrypt the plaintext, we also can decrypt back the encrypted text.").grid(row=15, column=0)
myLabel11 = Label(root, text="For decrypt, we are using inverse Key Matrix to do so.\n").grid(row=16, column=0)
myLabel12 = Label(root, text="Decrypted message from the encrypted plaintext:").grid(row=17, column=0)


# to let the program keep running as we moving our mouse

root.mainloop()