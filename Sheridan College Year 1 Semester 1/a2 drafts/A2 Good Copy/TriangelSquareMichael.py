'''
Assignment No.: 2
Course: PROG12974
Your Name: Michael Aaron Nolk
Your Sheridan Student Number: 991673010
Submission date: 11/20/2022
Instructor’s name: Syed Tanbeer
'''

#drawing square and cube 

def Triangle_Square():
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
    H = int(input("Enter the width of the rectangle: "))
    W = int(input("Enter the length of the rectangle: "))
    for top in range(W):
        print(' * ', end = '')
        if top == W - 1:
            print('\n')
    
    for height in range(H - 2):
        print(' * ', end = '')
       
        for space in range(top - 1):
            print('   ', end ='')
            if space == top - 2: 
                print(' * \n')
       
    for bottom in range(W):
        print(' * ', end = '')
           

