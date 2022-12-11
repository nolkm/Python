#created 10/8/2022

'''
Calories Burned Calculator 


'''
#input

gender = input('Please enter in your Gender "M" or "F": ' )#prompting user for input of their gender 


if gender.lower() == "m":#if user inputs 'm'
    print("Male")#flag//check point
    
    #input #2
    age = float(input("please enter in your age: "))#prompting user for input of their age 
    weight =float( input("please enter in your weight(in Lb(s)): "))#prompting user for input of their weight(lbs) 
    heartRate = float(input("Enter in your Heart rate(bpm(s))"))#prompting user for input of their heart rate (bpm)
    durationOfExercise = int(input("Enter in the duration of the exercise(min(s)): "))#prompting user for input of the duration of their exercise (mins)
    
    #process (Math)
    caloriesBurned = (((age * 0.2017) - (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * durationOfExercise / 4.184)#calculating the amouint of Calories burned (For Male)
    
    outPut = f'You burned {caloriesBunred:.2f}'#storing output in varible to Follow I.P.O method || using format to 2 floating points

elif gender.lower() == "f":#if user inputs 'f' 
    print("Female")#flag//check point
    
    #input #2
    age = float(input("please enter in your age: "))#prompting user for input of their age 
    weight =float( input("please enter in your weight(in Lb(s)): "))#prompting user for input of their weight(lbs) 
    heartRate = float(input("Enter in your Heart rate(bpm(s))"))#prompting user for input of their heart rate (bpm)
    durationOfExercise = int(input("Enter in the duration of the exercise(min(s)): "))#prompting user for input of the duration of their exercise (mins)

    #process (Math)
    caloriesBurned =(((age *0.074) - (weight * 0.05741 ) + (heartRate * 0.4472) - 20.4022) * durationOfExercise / 4.184)#Calculating the amount of calories burned (for Female )
    
    output = f' You burned {caloriesBurned:.2f}'#storing output in varible to Follow I.P.O method ||using format to 2 floating points

else:#else For Invalid Input <ERROR> 
    print("<ERROR> Please Try again <ERROR>")





