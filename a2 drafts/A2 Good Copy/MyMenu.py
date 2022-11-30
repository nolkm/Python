'''
Assignment No.: 2 
Course: PROG12974
Your Name: Michael Aaron Nolk
Your Sheridan Student Number: 991673010
Submission date: 11/20/2022
Instructor’s name: Syed Tanbeer
'''
import Function_tools# importing functions 
def main():
    while True: 
        print("""
    1 – Draw Shape
        a) Triangle
        b) Rectangle
    2 - Fermat’s Last Theorem
    3 – Facto-Power Series 
    4 – Check Password
    5 - Quit

        """)#multi line print statement for options 
        usrIn = int(input("Please select a Option: "))

        if usrIn == 1:#if user selects the triangle square
            Function_tools.Triangle_Square()
            print("Michael Aaron Nolk || Student Num: 991673010")#signature
        elif usrIn == 2:#if usr selects fermat
            Function_tools.fermat_theorem()
            print("Michael Aaron Nolk || Student Num: 991673010")#signature
        elif usrIn == 3:#user wants fermat
            Function_tools.facto_pwrSeries()
            print("Michael Aaron Nolk || Student Num: 991673010")#signature
        elif usrIn == 4:# if user wants facto pwrSeries 
            Function_tools.password()
            print("Michael Aaron Nolk || Student Num: 991673010")#signature
        elif usrIn == 5: #is user chooses to quit break from loop 
            print("Thank you for using my menu program")# good by message
            print("Michael Aaron Nolk || Student Num: 991673010")#signature
            break

if __name__ == '__main__':
    main()#main function for MyMenu.py