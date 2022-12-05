'''
Dev: Michael || Mm0)
Date: 11/21/2022
College Year 1 Semester 1 (PROG124029)
'''

#inventory data base for A3 
import inventoryDict as inventory#import my inventory from an external python file 
import sys# importing Sys for the sys.exit method 
print("START")#just a checkpoint 
database = inventory.dataBase()#creating a copy of the original data base in this program 
global CATEGORY_LIST #CREATING GLOBAL CATEGORY LIST
CATEGORY_LIST = inventory.categoryList 

def main(): 
    while True: #while user doesnt choose to quit
        ch = choice()#varible for the return value of the option the user selects
        #while user doesnt choose to quit 
        if ch.isnumeric() == False:
            print(f"ERROR: {ch} is ainvlaid input \nPlease enter a valid int ")# error msg
        if ch == '1':#show_all()
            show_all(database)#function to show all items 
        elif ch == '2':#look_up()
            look_up(database)#function that looks up all items 
            print('')
        elif ch == '3':
            add_item(database)
        elif ch == '4': 
            change_item(database)#changing item in DB 
        elif ch == '5': 
            delete_item(database)#deleting item from DB 
        elif ch == '6': 
            find_item_category(database)#finding items given category 
        elif ch == '7': 
            itemCount_priceCategory(database)#Item count, average price by category
        elif ch == '8': 
            priceUP(database)#finding the most exspensive item 
        elif ch == '9':
            total_price(database)#total price by item 
        elif ch == '10':
            sys.exit("*choice == 10: userIN ended Program* \nThank you:Good Bye!")
        else: 
            print('*ERROR @ main* \nplease enter valid input')
def choice():
    print("""
    1. show all items
    2. Look up inventory
    3. Add an item to inventory
    4. Change an item
    5. Delete an item
    6. Find items given category 
    7. Item count, average price by category
    8. Most exspensive item by category 
    9. Total price by item
    10. Quit the proram
    """)#options
    print(f"CATEGORY_LIST(DATBASE) = {CATEGORY_LIST} ") # DISPLAYING THE CATEGORY LIST CHANGES 
    valid = False#assigning a boolean value of false as my control varible 
    while valid == False:#looping the prompt
        try:
            choice = input("Enter your choice: ")#prompting user for choice 
            valid = True
        except ValueError:
            print("*ERROR*\nplease enter a Int of the option you're trying to select")
    return choice
    #end of choice()

def show_all(inventory):
    print('You Selected Option 1') #welcome
    print(f"\n\033[96m{'*'*30} Displaying all items {'*'*30}")
    # Printing the header
    print(f"{'Item Code':<15}{'Item Name':<15}{'Category':<15}{'Price (CA$)':<15}{'Quantity':<15}")  
    print(f"{'-'*75}")              # Printing the header separator
    for key in inventory:           # Loop through the dictionary and print the values in a tabular format
        print(f"{key:<15}{inventory[key][0]:<15}{inventory[key][1]:<15}{inventory[key][2]:<15}{inventory[key][3]:<15}")
    print("\033[0m")
    
    #end of show_all()

def look_up(database):#option2
    itemID = input("Enter the item id: ") #prompting the user for the ITEM ID 
  
    print(database.get(itemID,"User id not found *404* "))#.get() will check for ITEM ID if it can't find it then it will display error message 
    #end of look_up

def add_item(database):#function to add item to data base 
    print("You selected Option '3' ") #welcome

    item = list()#creating a empty dict to input all of the item stats
    valid = False#making a valid selection varible to control my loop 

    while True:
        itemID = input("Enter Item Id: ")#prompt user for item id
        itemCategory = input("Please enter in the item Category: ")#item Category
        if itemCategory.lower() in CATEGORY_LIST:
            print("Yes it is in CATEGORY_LIST" )
        elif itemCategory not in CATEGORY_LIST and itemID[0] != 'f':
            CATEGORY_LIST.append(itemCategory.lower()) # adding the new category to my Category Database 
            cntrlVar = False
        if len(itemID) > 3:
            #valid = False#making valid false 
            print("Please enter a Valid input || please enter a Item ID that is no great than 3 characters ")#error message  

        elif itemID not in database:#verifying that the user ID isn't already in the Database  
            if itemID[0].lower() == 'f' and itemCategory.lower() != CATEGORY_LIST[0].lower():
                print("Error, Any itemID starting with  the letter 'f' must have a category of 'Fruit' ") #error msg
                #valid = False #continuing the loop 
            elif itemID[0].lower() == 'v' and itemCategory.lower() != CATEGORY_LIST[1].lower():
                print("Error, Any itemID starting with  the letter 'v' must have a category of 'Vegetable' ") #error msg
                #valid = False #continuing the loop 
            elif itemID[0].lower() == 'd' and itemCategory.lower() != CATEGORY_LIST[2].lower():
                print("Error, Any itemID starting with  the letter 'd' must have a category of 'Dairy' ") #error msg
                #valid = False #continuing the loop 
            else: 
                cntrlVar = False#loop control varible
                break#valid = True#making valid true to break out of the loop 
        else:
            print(f"ItemID: {itemID} Already Exists with {database.get(itemID)}, please remove this item before proceeding ")
            return None #taking user back to menu
        
    while cntrlVar == False:
        itemName = input("Please enter in the item Name: ")#prompting for item name

        try:
            itemPrice = float(input("Please enter Item price: "))#prompting for item price  
            cntrlVar = True#breaking out of loop 
        except ValueError: 
            print("*error* \n Item Price must be a Number, not a string")#error msg!
    cntrlVar = False#loop control varible
    while cntrlVar == False:
        try: 
            itemCount = int(input("Please enter the item Count: "))#prompting for user input
            cntrlVar = True
        except ValueError:
            print("Please enter in a number Not a string")#error msg!
    item = [itemName, itemCategory, itemPrice, itemCount]#creating a list with all input 
    database[itemID] = item #adding the key to be the itemId the user entered and the value to be the list of all the item info user inputted 
    

        
def change_item(database):
    print('You Selected Option 4')
    error_counter = 4 #loop control 
    while True: 
        itemID = input("Please enter the item ID: ")

        if itemID in database:
            valid = True#making valid true to break out of the loop 
            itemName = input("Please enter in the item Name: ")#prompting for item name   
            userIn = False#while loop control varible 
            while userIn == False: 
                itemCategory = input("Please enter in the item Category: ")#item Category 
                x = database[itemID]#creating a list from the id input 
                if x[1] == itemCategory:
                    itemCategory = x[1]#assigning the category to itemCategory input if the input matches the default category
                    userIn = True # breaking the while loop... 
                else: 
                    print(f"Item Category Invalid (After {error_counter} Failed Attempts you wll be brought back to Main() Menu)")
                    error_counter -=1# subtracting on attempt every time from my control varibe 
                if error_counter == 0:
                    print("Failed Attempts exceeded the amount allowed Bringing you back to main() Menu")#error msg 
                    return#returning user to main menu 
            cntrlVar = False#loop control varible 
            while cntrlVar == False:
                try:
                    itemPrice = float(input("Please enter Item price: "))#prompting for item price  
                    cntrlVar = True#breaking out of loop 
                except ValueError as e: 
                    print("*error* \n Item Price must be a Number, not a string")#error msg!
            cntrlVar = False#loop control varible
            while cntrlVar == False:
                try: 
                    itemCount = int(input("Please enter the item Count: "))#prompting for user input
                    cntrlVar = True
                except ValueError:
                    print("Please enter in a number Not a string")#error msg!
            item = [itemName, itemCategory, itemPrice, itemCount]#creating a list with all input 
            database[itemID] = item #adding the key to be the itemId the user entered and the value to be the list of all the item info user inputted 
            break
        else:
            print(f'ERROR: Item with ID "{itemID} could not be found.' ) 
    
    #end of change_item()

def delete_item(database):#function to delete items from data base 
    print("--You selected Option '5' Delete_item()--") #welcome

    abort = False #while loop control var
    while abort == False:
        itemID = input("please enter item ID: ")#prompting user for itemID
        if itemID in database: #verifying that the itemID that hase been inputted is in the database 
            confirmation = input(f'Confirm you would like to delete item "{database[itemID]}" this change cannot be reversed (Y/n): ')#Confriming with user the would like to delete the item 
            if confirmation.lower() == 'y':
                print(f'Item "{database[itemID]}"')#output show item was deleted  
                del database[itemID]#deleteting the item with item ID
                return
            elif confirmation == "n":
                print(f'Item "{database[itemID]}" has not been removed... \n--Returning to main() Menu--')
                abort = True
            else: # Invalid input for confirmation
                print("Error Invalid input || PLease try again!")#error msg 
        else:
            userIn = input("{Invalid Input} || would you like to continue?(Y/n): ") #asking user if they want to tryu again 
            if userIn.lower() == 'n':
                print("Returning to Main")
                abort = True
            elif userIn.lower() == 'y':
                abort = False # loop continues.. 
            else: 
                print("Invalid input Please Try again")
    #end of delete_item()

def find_item_category(database):
    print("You selected option 6 ")#function option #num 6
    item_category = input("Please enter the item Category: ")#prompting user for category INPUT..
    if item_category.lower() not in CATEGORY_LIST: #invalid entry
            print('ERROR 404: Item Category "{item_category}" Not Found')#error msg
            return
    for keys, values in database.items():#itterating through the loop 
        if values[1].lower() == item_category.lower():#printing if input is == category in database
            print(values)
        elif values[1].lower() != item_category.lower(): 
            None # if the item category is not equal return none 

     
    #end of find_item_category()

def itemCount_priceCategory(database):#Item count, average price by category
    print("Option 7")#saving for l8r
    fruitCount = 0
    vegeCount = 0 
    dairyCount = 0
    fruitPrice = 0.00
    vegePrice = 0.00
    dairyPrice = 0.00
    otherCount = 0
    for keys, values in database.items():
        print(values[1])
        if values[1].lower() == CATEGORY_LIST[0]:     
            fruitCount += 1 #adding count 
            fruitPrice += values[3] #total cost
        if values[1].lower() == CATEGORY_LIST[1]:
            vegeCount += 1 #adding count 
            vegePrice = values[3] #caculating total cost 
        if values[1].lower() == CATEGORY_LIST[2]:
            dairyCount += 1  #adding count 
            dairyPrice += values[3]   
    print(f'{CATEGORY_LIST[0]} Count = {fruitCount}') #output count for fruit
    print(f'{CATEGORY_LIST[2]} Count = {vegeCount}') #output count for vege
    print(f'{CATEGORY_LIST[1]} Count = {dairyCount}') #output count for dairy
    print(f'{CATEGORY_LIST[0]} average cost = {fruitPrice / fruitCount}') #average cost
    print(f'{CATEGORY_LIST[2]} average cost = {vegePrice / vegeCount}') #average cost
    print(f'{CATEGORY_LIST[1]} average cost = {dairyPrice / dairyCount}') #average cost
    #end of itemCount_priceCategory()

def priceUP(database):  #function to show the most exspensive item by category 
    fruitMax = 0 #vairbles to find the most exspensive item
    vegeMax = 0
    dairyMax = 0

    for keys, values in database.items(): 
        if values[1].lower() == CATEGORY_LIST[0]:     
            if fruitMax < values[3]:
                fruitMax = values[3] #assigning the max price to varible for each category
                fruitMaxName = values[0]
        if values[1].lower() == CATEGORY_LIST[1]:
            if vegeMax < values[3]:
                vegeMax = values[3] #assigning the max price to varible for each category
                vegeMaxName = values[0]
        if values[1].lower() == CATEGORY_LIST[2]:
             if dairyMax < values[3]:
                dairyMax = values[3] #assigning the max price to varible for each category
                dairyMaxName = values[0]
    print(f"Most expensive item in category Fruit: {fruitMaxName} and it costs {fruitMax} ") #displaying the most exspensive item 
    print(f"Most expensive item in category Fruit: {vegeMaxName} and it costs {vegeMax} ") #displaying the most exspensive item 
    print(f"Most expensive item in category Fruit: {dairyMaxName} and it costs {dairyMax} ") #displaying the most exspensive item 
    #end of priceUP()
def total_price(database): #function to show all the items and their price.. 
    for keys, values in database.items(): 
        print(f"Item id = {keys} || item = {values[0]}, total price = {values[3]}")

if __name__ == '__main__':#checking for main()
    main()#calling main() function 
