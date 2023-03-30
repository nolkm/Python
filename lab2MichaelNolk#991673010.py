import threading #importing the threading module 
import time 
def stamp():
    print('''
    $ Quiz/Lab: 3
    $ Your Name: Michael Aaron Nolk 
    $ Your Sheridan student number: 991673010

    ''')


def ABC_HOTEL(): # method to get user input for number of rooms 
    try: 
        n = int(input("Please enter the total number of availableRooms in the ABC Hotel: "))
        number_of_rooms = {num: "Available" for num in range(n)}
        print(number_of_rooms)
        return number_of_rooms
        
    except Exception as e: 
        print('Task Complete')

def agentA(availableRooms, lock): # AGENT-A takes care of room bookings only (one room at a time)
    lock.acquire() # acquire the lock before modifying the dictionary
    print('Room Booking task started by ', threading.currentThread().getName())
    print('___'*10) #divider
    try:
        for keys, values in availableRooms.items():
            if values == "Available":
                print(f"\t{keys} is available") #outputting if the availableRooms are available  
            else:
                print(f"\t{values} is unavailable") #outputting if availableRooms are unavailable 
        room_number = int(input("What Room would you like to book? please Enter in the Room Number: "))
        
        if availableRooms.get(room_number, None) == "Available":
            availableRooms[room_number] = "Unavailable"
            print("Room booked successfully.")
        else:
            print("Room is already unavailable.")
        lock.release() # release the lock

    except Exception as E:
        #print(E) #error msg    
        print('Task Complete') 
        lock.release() # release the lock

def agentB(availableRooms, lock): # AGENT-B processes the checkouts only (one room at a time)
    lock.acquire() # acquire the lock before modifying the dictionary
    print('Process Checkout task started by ', threading.currentThread().getName())
    print('___'*10) #divider
    for keys, values in availableRooms.items():
            if values == "Available":
                print(f"\t{keys} is available") #outputting if the availableRooms are available  
            else:
                print(f"\t{keys} is unavailable") #outputting if availableRooms are unavailable 
    try:
        room_number = int(input("What Room would you like to checkout? please Enter in the Room Number: "))
        
        if availableRooms.get(room_number, None) == "Unavailable":
            availableRooms[room_number] = "Available"
            print("Checkout successful.")
        else:
            print("Room is already available.")

        lock.release() # release the lock

    except Exception as E:
        #print(E) #error msg    
        print('Task Complete') 
    lock.release() # release the lock

def agentC(availableRooms, lock): # AGENT-C is responsible to display the current room booking status. 
    lock.acquire() # acquire the lock before modifying the dictionary
    print('Displaying Current Rooms task started by ', threading.currentThread().getName())
    print('___'*10) #divider
    available = 0 # available
    unavailable = 0 # unavailable 
    print('Room Status...')
    for keys, values in availableRooms.items():
        if values == "Available":
            print(f"\t Room {keys} is available") #outputting if the availableRooms are available 
            available += 1 #counting num of available availableRooms 
#eror 
        else:
            print(f"\t Room {keys} is unavailable") #outputting if availableRooms are unavailable 
            unavailable += 1
        print('_'*22)
    print(f'\t\tTotal of {available} available Rooms \n\t\t Total of {unavailable} Unavailable availableRooms') #output 
    lock.release() # release the lock

if __name__ == '__main__':
    availableRooms = ABC_HOTEL()  #getting my dict of avalible rooms 
    lock = threading.Lock() #Option 1, Using a lock to lock the Critical info which is in this case the dict from availableRooms
   
    '''
    #ingnore! ! !  
        try:
            userIN = int(input("Please Select from 1 of the Following tasks: \n\t (1) Agent A room Booking \n\t (2) Agent B room checkout \n\t Agent C room checkout")) #getting user in 

            if userIN == 1: 
                agentA_task1.start()
            elif userIN == 2: 
                agentB_task1.start()


        
        except Exception as E:
            print(E)
        '''

    counter = 0 #count every loop will += 1 to the counter... 
    exitCounter = 10 # set the value for the counter, this is number of times it will loop at max if user does not choose to quit 
    exitCode = True #exit code for loop 
    while exitCode == True and counter < exitCounter:
        #creating all of the agent threads 
        agentA_task1 = threading.Thread(name='Agent-A || ROOM BOOKING',target=agentA, args=(availableRooms,lock))
        agentB_task1 = threading.Thread(name='Agent-B || ROOM CHECKOUT',target=agentB, args=(availableRooms,lock))
        agentC_task1 = threading.Thread(name='Agent-A || ROOM STATUS',target=agentC, args=(availableRooms,lock))
        
        agentA_task1.start() #starting 
        time.sleep(1) # sleep!!!
        agentB_task1.start()
        time.sleep(1) # sleep!!!
        agentC_task1.start()
        
        agentA_task1.join()
        agentB_task1.join()
        agentC_task1.join()
        counter += 1 # increment counter
        
        # sleep for some time before running the threads again
        time.sleep(1)
        yesOrNo = input('Would you like to continue? "y/n": ') #asking user if they would like to continue 
        if yesOrNo.lower() == 'n':
            exitCode = False #breaking the loop 
        elif yesOrNo.lower() == 'y': #elif if user enters yes 
            exitCode = True #continuing the loop sine the value stays True !!!
        else: 
            print('Error! ') #error msg 
            
        
        
    print("\n \033[92m" +  "All threads have completed execution."+ "\033[0m") #end of program 
    stamp()


