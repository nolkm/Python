'''
Assignment No.: 2
Course: PROG12974
Your Name: Michael Aaron Nolk
Your Sheridan Student Number: 991673010
Submission date: 11/20/2022
Instructor’s name: Syed Tanbeer
'''

#Fermat’s Last Theorem says that there are no positive integers a, b, and c such that 
def fermat_theorem():
    while True: 
        fermat()
        userIn = input("Would you like to Continue? Y/n ")#asking user if they would like to continue
        if userIn.lower() == 'n':
            break
def power(num,n):
    if n == 0:
        return 1 #since anything to power of 0 is 1 
    elif n < 0: 
        print("Error Positive int only")
    else: 
        return num * power(num, n-1)

def fermat():
    print('Welcome to Fermat theorem please enter the values below for a**n + b**n = c**n ')
    #INPUTS FOR A, B, C, AND N
    A = int(input('Please enter A: '))#INPUT FOR A 
    B = int(input('Please enter B: '))#INPUT FOR B
    C = int(input('Please enter C: '))#INPUT FOR C
    N = int(input('Please enter N: '))#INPUT FOR N

    if power(A,N) + power(B,N) == power(C,N):#IF LEFT SIDE IS = TO RIGHT SIDE 
        print(f"For n = 2, Left hand side = Right hand side: The theorem holds")
    elif power(A,N) + power(B,N) != power(C,N):#if right hand side is not equal to left hand side 
       print(f"For n = {N}, Left hand side != Right hand side: The theorem holds") 
                       
    print(f'{power(A,N)} + {power(B,N)} = {power(C,N)}') 

