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
        if ch == 1:#show_all()
            show_all(database)#function to show all items 
        
        elif ch == 2:#look_up()
            look_up(database)#function that looks up all items 
        elif ch == 3:
            add_item(database)
        elif ch == 4: 
            change_item(database)#changing item in DB 
        elif ch == 5: 
            delete_item(database)#deleting item from DB 
        elif ch == 6: 
            find_item_category(database)#finding items given category 
        elif ch == 7: 
            itemCount_priceCategory(database)#Item count, average price by category
        elif ch == 8: 
            priceUP(database)#finding the most exspensive item 
        elif ch == 9:
            total_price(database)#total price by item 
        elif ch == 10:
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
            choice = int(input("Enter your choice: "))#prompting user for choice 
            valid = True
        except ValueError:
            print("*ERROR*\nplease enter a Int of the option you're trying to select")
    return choice
    #end of choice()

def show_all(database):
    print('You Selected Option 1') #welcome

    for key, value in database.items():#for loop to format the output 
        print(key, value)#printing the entire databse, line by line using for loop 
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
        if values[1] == item_category:#printing if input is == category in database
            print(values)
        elif values[1] != item_category: 
            None
     
    #end of find_item_category()

def itemCount_priceCategory(database):#Item count, average price by category
    print("Production in Progress")#saving for l8r
'''
def categoryList(*category):#using the astrisk to accept any number of arguments 
    category_list = ["Fruit","Vegetable","Dairy"] #creating a list with the default Categories 
    if category not in category_list:
        category_list.append(str(category))#adding a new values   
        return category_list
    else:
        print("Nothing Changed... ")  # error msg
        return category_list #return list by default when no changes are made 
     
x = categoryList("Meat")
print(x)
print(categoryList())

'''

    #end of itemCount_priceCategory()

if __name__ == '__main__':#checking for main()
    main()#calling main() function 
