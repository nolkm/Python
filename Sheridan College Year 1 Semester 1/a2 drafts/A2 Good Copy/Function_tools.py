'''
Course: PROG12974
Assignment: 2
Name: <Your name>
ID: <Your Sheridan Student Number>
Instructor: Syed Tanbeer
'''

#drawing square and cube 

def Triangle_Square():#main function
    while True: 
        userIn = input("Please Select from one of the following options \nPLEASE TYPE '1' FOR \n-- DRAWING A SQUARE\nPLEASE TYPE '2' FOR \n-- DRAWING A TRIANGLE \n enter selection here >> ")#prompting the user to select the program 
        if userIn == '1':#if input is equal to string 1 
            outputSquare()#outputSquare Function 
        elif userIn == '2':#if input is equal to string 2 
            outputTriangle()#outputTriangle Function 
        else: 
            print("Error ")#invalid input message
        
        userIn = input("\n Would you like to Continue? Y/n ")#asking user if they would like to continue
        if userIn.lower() == 'n':#if user says no break 
            break
        
def outputTriangle():
    usrNum1 = int(input("Enter the height of the triangle: "))#prompting user for input 
    print("*")#printing the first star
    for height in range(usrNum1 - 2 ): #subtracting two to account for the first single start and the base of the triangle that way there is no overlaping, after printing a start it movews to the nested loop
        print('*', end= '')#
        for space in range(height):#printing the empty space based on the range of the height of the triangle
            print(' ', end= ' ')#spaces
        print('*')#printing the hypotnuse 
    print('* ' * (usrNum1 - 1))#printng the base 

def outputSquare():
    H = int(input("Enter the width of the rectangle: "))#prompting for input
    W = int(input("Enter the length of the rectangle: "))
    for top in range(W):
        print(' * ', end = '')#outputting the top 
        if top == W - 1:
            print('\n')
    
    for height in range(H - 2):#outputing the side
        print(' * ', end = '')
       
        for space in range(top - 1):#spaces
            print('   ', end ='')
            if space == top - 2: 
                print(' * \n')#other side 
       
    for bottom in range(W):
        print(' * ', end = '')#bottom 
    #end of output square    

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
    #end of fermat 

    #facto power series 
def facto_pwrSeries():
    while True:    
        userIn = int(input("Enter the value for n: "))
        print("The sum of the series: ",facto_power(userIn))#outputting the format and the function
        userIn2 = input("Would you like to Continue? Y/n ")#asking user if they would like to continue
        if userIn2.lower() == 'n':
            break
    #end of main

def power(num, n):#this is same function from fermat program i created 
    if n == 0:
        return 1 #since anything to power of 0 is 1 
    elif n < 0: 
        print("Error Positive int only") #making sure it is a positive int 
    else: 
        return num * power(num, n-1)

def factorial(num):#factorial funciton  
    if num == 0: 
        return 1 #0! = 0 || so return 0 
    else:
        return num * factorial(num-1)#subtracting one from num so it is going down each time 

def facto_power(n):#taking n to return the serires
    if n == 0: 
        return 0 
    else: 
        return (power(n, n)/factorial(n)) + facto_power(n-1)#recursive series 




#password 

def password():
    print(" Welcome to PASSWORDCHECKER\n here are valid password rules \n1. Password length must be at least 8 characters.\n2. Password must contain combination of uppercase, lowercase, numbers, and symbols (except ‘<’ and ‘>’).  ")#valid password output
    while True: 
        passwordChecker(passwordInput())#the stdout for passwordInput() becomes stdin for passwordChecker()
        userIn = input("Would you like to Continue? Y/n ")#asking user if they would like to continue
        if userIn.lower() == 'n':
            break
    print("Thanks For using the password checker")
    #end of main 

def passwordInput():#function to get user input
    pwd = input("Enter a password: ")
    #end of passwordInput
    return pwd#returning the user input as pwd
    
def passwordChecker(pwd):#function to check the input 
    Upr = 0 #upper GLOBAL
    Lwr = 0 #lower GLOBAL
    Symbol = 0 #symbol GLOBAL
    Digit = 0 #digit GLOBAL
    if len(pwd) >= 8: # checking for the length of the password 
        for char in range(len(pwd)):#looping through each individual character based off of the char index 
            
            if pwd[char] == '>' or pwd[char] == '>':# if it contains illegal symbols 
                Symbol += 1#adding 1 to symbol 
            elif pwd[char].isdigit():
                Digit += 1#adding 1 to Digit 
            elif pwd[char].isalpha():
                if pwd[char].isupper():
                    Upr += 1 #adding one to uppper 
                elif pwd[char].islower():
                    Lwr += 1 #adding one to lower 
    else:
        print("Error: Password should be atleast 8 characters long.")
    
    if Lwr == 0:
        print("Password should contain Lower case letters")
    if Symbol > 0:
        print("Cannot contain '>' or '<' symbols ")
    if Digit == 0:
        print("Password should contain digits")
    if Upr == 0:
        print("password should contain  upper case characters")
    else:
        print("Thanks!")



    #END OF PASSWORD CHECKER

