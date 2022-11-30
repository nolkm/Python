# Sheridan-College-Python-Year-1-Semester-1
#inventory data base for A3 
import inventoryDict as inventory#import my inventory from an external python file 
import sys# importing Sys for the sys.exit method 
print("START")#just a checkpoint 
database = inventory.dataBase()#creating a copy of the original data base in this program 
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
            delete_item(datbase)#deleting item from DB 
        elif ch == 6: 
            find_item_category(database)#finding items given category 
        elif ch == 7: 
            itemCount_priceCategory(database)#Item count, average prpice by category
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
    for key, value in database.items():#for loop to format the output 
        print(key, value)#printing the entire databse, line by line using for loop 
    #end of show_all()

def look_up(database):#option2
    itemID = input("Enter the user id: ") #prompting the user for the ITEM ID 

    print(database.get(itemID,"User id not found *404* "))#.get() will check for ITEM ID if it can't find it then it will display error message 
    #end of look_up

def add_item(database):#function to add item to data base 
    item = list()#creating a empty dict to input all of the item stats
    valid = False#making a valid selection varible to control my loop 

    while valid == False:
        itemID = input("Enter Item Id: ")#prompt user for item id
        if len(itemID) > 3:
            valid = False#making valid false 
            print("Please enter a Valid input || please enter a Item ID that is no great than 3 characters ")#error message 
            ValueError#throwing a value error 

        elif itemID not in database:#verifying that the user ID isn't already in the Database 
            valid = True#making valid true to break out of the loop 
            itemName = input("Please enter in the item Name: ")#prompting for item name   
            itemCategory = input("Please enter in the item Category: ")#item Category 
            cntrlVar = False#loop control varible 
            while cntrlVar == False:
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

        else:
            print(f"ItemID: {itemID} Already Exists with {database.get(itemID)}, please remove this item before proceeding ")
            return None #taking user back to menu 



if __name__ == '__main__':#checking for main()
    main()#calling main() function 