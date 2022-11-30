'''
Assignment No.: 2
Course: PROG12974
Your Name: Michael Aaron Nolk
Your Sheridan Student Number: 991673010
Submission date: 11/20/2022
Instructor’s name: Syed Tanbeer
'''


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


facto_pwrSeries()