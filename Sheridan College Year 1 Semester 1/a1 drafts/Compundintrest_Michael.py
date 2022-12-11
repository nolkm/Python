#CREATED: 9/30/2022 || YEAR 1//SEMESTER 1
'''
Assigment No.: 1 

Course PROG12974

Michael Aaron Nolk 

Student Num: 991673010

Submission Date: 10/8/2022

Instructor's Name: Syed Tanbeer 
'''
#Exercise 2: Compound Interest [marks: 7]

#INPUT
p = float(input("Enter in the Amount deposited: ")) #Input for p =  the principal amount that was originally deposited into the account.
r = float(input("Enter the annual intrest rate:"))#Input for r = annual intrest rate
n = float(input("Enter the intrest compunded frequency:"))#Input for n = number of times intrest is compunded a year
t = float(input("Enter the Number of years:"))#Input for t = the specified number of years

#PROCESS
nt = n * t #multiplying nt
precentage = n*100#calculating Precentage 
a = float(p*((1+(r/precentage))**nt))# compund intrest formula

output = f"Total amount after interest: {a:.0f}\nPrincipal amount: {p:.0f}\nIntrest rate: {r:.1f}%\n Number frequency: {n:.0f} \n number of years: {t:.0f}"#creating varibles for output


#OUTPUT
print(f"{output} ")#output in formatted string 

print("Compound interest calculator by: by: Micahel Aaron Nolk, #991673010")#output stamp

 
