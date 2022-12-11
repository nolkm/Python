#CREATED: 9/30/2022 || YEAR 1//SEMESTER 1
'''
Assigment No.: 1 

Course PROG12974

Michael Aaron Nolk 

Student Num: 

Submission Date: 10/08/2022

Instructor's Name:
'''
#Exercise 3: Calories Burned [marks: 7]

#INPUT
gender = input('Please enter in your Gender "M" or "F": ' )#prompting user for input of their gender 


if gender.lower() == "m":#if user inputs 'm'
    print("Male")#flag//check point
    
    #INPUT #2
    age = float(input("please enter in your age: "))#prompting user for input of their age 
    weight =float( input("please enter in your weight(in Lb(s)): "))#prompting user for input of their weight(lbs) 
    heartRate = float(input("Enter in your Heart rate(bpm(s))"))#prompting user for input of their heart rate (bpm)
    durationOfExercise = int(input("Enter in the duration of the exercise(min(s)): "))#prompting user for input of the duration of their exercise (mins)
    
    #PROCESS (Math)
    caloriesBurned = (((age * 0.2017) - (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * durationOfExercise / 4.184)#calculating the amouint of Calories burned (For Male)
    
    outPut = f'You burned {caloriesBurned:.2f}'#storing output in varible to Follow I.P.O method || using format to 2 floating points

    #OUTPUT
    print(outPut)
elif gender.lower() == "f":#if user inputs 'f' 
    print("Female")#flag//check point
    
    #INPUT #2
    age = float(input("please enter in your age: "))#prompting user for input of their age 
    weight =float( input("please enter in your weight(in Lb(s)): "))#prompting user for input of their weight(lbs) 
    heartRate = float(input("Enter in your Heart rate(bpm(s))"))#prompting user for input of their heart rate (bpm)
    durationOfExercise = int(input("Enter in the duration of the exercise(min(s)): "))#prompting user for input of the duration of their exercise (mins)

    #PROCESS (Math)
    caloriesBurned =(((age *0.074) - (weight * 0.05741 ) + (heartRate * 0.4472) - 20.4022) * durationOfExercise / 4.184)#Calculating the amount of calories burned (for Female )
    
    outPut = f' You burned {caloriesBurned:.2f}'#storing output in varible to Follow I.P.O method ||using format to 2 floating points

    #OUTPUT
    print(outPut)
    
else:#else For Invalid Input <ERROR> 
    print("<ERROR> Please Try again <ERROR>")


print("Square-Cube Table by: Michael ")#output stamp




