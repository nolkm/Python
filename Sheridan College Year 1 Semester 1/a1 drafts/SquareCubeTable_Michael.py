#CREATED: 9/30/2022 || YEAR 1//SEMESTER 1
'''
Assigment No.: 1 

Course PROG12974

Michael Aaron Nolk 

Student Num: 991673010

Submission Date: 

Instructor's Name: Syed Tanbeer 
'''
#Exircise 1 || Square-Cube Table [Mark 6]
 
num1 = 1 #creating a global varible that i will manipulate to display a output 5 times
num2 = 2 #creating a global varible that i will manipulate to display a output 5 times
num3 = 3 #creating a global varible that i will manipulate to display a output 5 times
num4 = 4 #creating a global varible that i will manipulate to display a output 5 times
num5 = 5 #creating a global varible that i will manipulate to display a output 5 times

#INPUT
userInput = int(input("Enter in a number between 1 and 10: "))# prompting the user for input and storing it in a varible called userInput thats data type int  

#PROCESS
if userInput <= 5: # if Varible userInput is less than 5
    #performing math operations of squaring number 1 through 5 
    squaredNum1 = num1**2 #varible num1^2 | The result is stored into a new varible called squaredNum1 
    squaredNum2 = num2**2 #varible num1^2 | The result is stored into a new varible called squaredNum2
    squaredNum3 = num3**2 #varible num1^2 | The result is stored into a new varible called squaredNum3 
    squaredNum4 = num4**2 #varible num1^2 | The result is stored into a new varible called squaredNum4 
    squaredNum5 = num5**2 #varible num1^2 | The result is stored into a new varible called squaredNum5 
    #performing math operations of cubing all numbers
    cubedNum1 = num1**3 #varible num1^3 | The result is stored into a new varible called cubedNum1
    cubedNum2 = num2**3 #varible num2^3 | The result is stored into a new varible called cubedNum2
    cubedNum3 = num3**3 #varible num3^3 | The result is stored into a new varible called cubedNum3
    cubedNum4 = num4**3 #varible num4^3 | The result is stored into a new varible called cubedNum4
    cubednum5 = num5**3 #varible num5^3 | The result is stored into a new varible called cubedNum5
    
    
else: #else input put is greater that 5 
    print(f"Input '{userInput}' is Greater than 5. \n Goodbye")

#OUTPUT
#print('N   N^2   N^3')#outputing my headers 

if userInput == 1: #processing the amount of lines to output 
    print(f'N   N^2    N^3\n{num1}    {squaredNum1}     {cubedNum1} \n ')#output in a formatted string of my three Varibles 
    print('lines: 1')
elif userInput == 2: #processing the amount of lines to output 
    print(f'N   N^2    N^3\n{num1}    {squaredNum1}     {cubedNum1} \n{num2}    {squaredNum2}     {cubedNum2}')
    print('lines: 2')
elif userInput == 3: #processing the amount of lines to output 
    print(f'N   N^2    N^3\n{num1}    {squaredNum1}     {cubedNum1} \n{num2}    {squaredNum2}     {cubedNum2}\n{num3}    {squaredNum3}     {cubedNum3}')
    print('lines: 3')
elif userInput == 4: #processing the amount of lines to output 
    print(f'N   N^2    N^3\n{num1}    {squaredNum1}     {cubedNum1} \n{num2}    {squaredNum2}      {cubedNum2} \n{num3}    {squaredNum3}      {cubedNum3}\n{num4}    {squaredNum4}     {cubedNum4}')
    print('lines: 4')
elif userInput == 5: #processing the amount of lines to output 
    print(f'N   N^2    N^3\n{num1}    {squaredNum1}     {cubedNum1} \n{num2}    {squaredNum2}      {cubedNum2} \n{num3}    {squaredNum3}      {cubedNum3}\n{num4}    {squaredNum4}     {cubedNum4}\n{num5}    {squaredNum5}     {cubednum5}')
    print('lines: 5')
    
print("Square-Cube Table by: Micahel Aaron Nolk, #991673010")#output stamp
