'''
Assignment No.: 2
Course: PROG12974
Your Name: Michael Aaron Nolk
Your Sheridan Student Number: 991673010
Submission date: 11/20/2022
Instructor’s name: Syed Tanbeer
'''

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



