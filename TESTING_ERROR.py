#testing connnectecting to the DB
import mysql.connector
import csv
import time 
import sys
import getpass
import sys
import datetime
import platform
import socket
from prettytable import PrettyTable


## END OF IMPORTS! 
def stamp():
    colourText('''
    $ Assignment: 2
    $ Your Name: Michael Aaron Nolk 
    $ Your Sheridan student number: 991673010
    $ Prof. Syed Tanbeer 
    ''')


def colourText(string):
     string = str(string)
     print("\033[91m" + string + "\033[0m") #just output colourful text 

def readerD(table_name): # This function will allow us to read data from a table

    sql = f'Select * from {table_name}' # This command is to read all the rows and columns from the selected table
    cursor.execute(sql) # executing the command
    result = cursor.fetchall() # store the returned info into a variable
    return result


def loadingBar(percentage): 
    sys.stdout.write('\r') 

    if percentage == 100: 
        print("SYS.MSG = PLease wait as We Process the Login... ")
        msg = " CONNECTED! --> [%-20s] %d%%" % ('\033[92m=\033[0m'*int(percentage/5), percentage) 
        print(f'\033[92m{msg}')
    else: 
        sys.stdout.write("Attempting to Connect: [%-20s] %d%%" % ('='*int(percentage/5), percentage)) 
    sys.stdout.flush() 

def create_connection():
    global conn # made global so that its visible from other functions
    print("\033[40m")
    system_hostname = socket.gethostname()
    internetADDRESS = socket.gethostbyname(system_hostname)

    print('#######################~MySQL~###############################') #output message 
    #Ask for username and password
    print("\033[92m " + f"WELCOME {system_hostname} PLEASE LOGIN TO THE MySQL APPLICATION \n \t\t IP ADDRESS: {internetADDRESS} ") #welcome statement 
    
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
 
    #Create connection
    try:
        conn = mysql.connector.connect(host="localhost", user=username, passwd=password, database='MyStore') #end of connection 
        cursor = conn.cursor() #creating a Cursor to execute within MySQL 
    except mysql.connector.Error as err: #except statement for unsucessful login 
        print("\033[91m" + "Something went wrong: {}".format(err) + "\033[0m")
        sys.exit(1) #exit with process code 1 == ERROR 

    #Display success message
    for x in range(101): 
            loadingBar(x) 
            time.sleep(0.001)
    print("\t\n\033[92m" + "Connection established successfully!" + "\033[0m")

    #Print user name and system information
    print("\t\t\033[94m" + "User Name: " + username + "\033[0m")
    print("\t\t\033[94m" + "System: " + platform.system() + "\033[0m") 
    print("\t\t\033[94m" + "Login Time: " + datetime.datetime.now().strftime("%x %X") + "\033[0m") #date and time output 
    #Print server information
    print("\033[92m" + "Server Information: " + "\033[0m")
    cursor.execute('SELECT VERSION();')
    print("\t\t\033[94m" + "Server Version: ", cursor.fetchall(), "\033[0m")

    #SQL COMMANDs 
    cursor.execute("SHOW TABLES") #command to show databases 
    print('\033[94m Data Objects Present:', cursor.fetchall(), ' \033[0m') #outputting all the tables 
    
    return conn
    #Print server uptime, IP address and port
    

def insertTable(): #insert data into table from CSV file method 
        print("\033[40m")
        print("HELLO")
        with open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Transactions.txt", "r") as f:
            transaction_list = [line.strip().replace(" ", "") for line in f.readlines()]
            for line in f:
                line = line.strip().replace(" ", "")
                values = line.split()
                values = [int(v) for v in values]
                transaction_list.append(values)
            print("Requirment 6")
            cursor = db.cursor() # creating cursor to execute SQL queries 
            dictDB = {} #null dict 
            quanity3 = list() #null list 
            total_price = 0
            for i in range(len(transaction_list)):
                    
                    if i == 0 or i == 1:
                        pass
                    else:
                        Transaction_id = int(transaction_list[i][0])
                        iid = int(transaction_list[i][1])
                        quanity = int(transaction_list[i][2])
                        dictDB[Transaction_id] = [iid, quanity]  #creating my DIct 
                        cursor.execute(f"INSERT INTO transactions (tid, iid, quantity) VALUES ({Transaction_id}, {iid}, {quanity})")
                        db.commit()

        cursor.execute("SELECT * FROM items_michael")

             # loop through the items and insert them into the respective category total tables
        for row in cursor.fetchall():
                    item_id = row[0]
                    item_name = row[1]
                    category = row[2]
                    item_cost = row[3]
                    
                    if category == "Dairy":
                        cursor.execute(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Fruit":
                        cursor.execute(f"INSERT INTO CategoryTotal_Fruit (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Meat":
                        cursor.execute(f"INSERT INTO CategoryTotal_Meat (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Snacks":
                        cursor.execute(f"INSERT INTO CategoryTotal_Snacks (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Vegetables":
                        cursor.execute(f"INSERT INTO CategoryTotal_Vegetables (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")

                    db.commit() # commit the changes made in the loop to the databaser

        try:
            with open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Items_YourFirstName.csv", 'r') as C:
                csv_data = csv.reader(C)
                i = 0 #creating a counter 
                print(csv_data)
                
                for row in csv_data: 
                    item_id = row[0]
                    item_name = row[1]
                    category = row[2]
                    item_cost = row[3]
                    
                    if category == "Dairy":
                        cursor.execute(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Fruit":
                        cursor.execute(f"INSERT INTO CategoryTotal_Fruit (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Meat":
                        cursor.execute(f"INSERT INTO CategoryTotal_Meat (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Snacks":
                        cursor.execute(f"INSERT INTO CategoryTotal_Snacks (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                    elif category == "Vegetables":
                        cursor.execute(f"INSERT INTO CategoryTotal_Vegetables (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")
                        print(f"INSERT INTO CategoryTotal_Dairy (ItemID, Item, Amount) VALUES ({item_id}, '{item_name}', {item_cost})")


                    if i == 0:
                        print('HEADERS SKIPPED') #SKIPPING THE HEADERS 
                    else:
                        
                        rowItems = list(row) # taking each row from list a tuple 
                        rowItems[0] = int(rowItems[0])
                        rowItems[3] = float(rowItems[3])
                        print(rowItems)
                       # cursor.execute(f'INSERT INTO Items_MICHAEL(iid, name, category, item_cost) VALUES("%s", "%s", "%s", "%s")', rowItems)  
                    i += 1 #adding 1 to my counter 
            print("Data Inserted Complete!") # completion message 
            db.commit() #commiting of the data 
        except Exception as E: 
            print(E)
            
           
       
        
            print("Operation Complete!") #end of operation 
        

def createTABLE():
        print("\033[40m")
        create_query = ''' CREATE TABLE Items_MICHAEL(
        iid VARCHAR(255) NOT NULL, 
        name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL, 
        item_cost VARCHAR(255) NOT NULL,
        PRIMARY KEY (iid))''' #SQL QUERY for creating my table 
        try:
            cursor.execute(create_query)
            print('Table Created Successfully! ')
        except Exception:
            print(' Table Already Exists! ')
    
        print("Operation Complete!") #end of operation 
        #self.cursor.execute('SELECT * FROM item_michael') #selecting values from table  
        db.commit() #commiting of the data  

def resetDB():
        print("\033[40m")
        try: 
            cursor.execute('DROP TABLE items_michael') #command to Drop The Table 
        except Exception as E: 
            print(E)
        print("Operation Complete! Table was Dropped sucessfully") #end of operation 

        db.commit() #commiting of the data  
    
def connectionClose():
        db.close()

def selectDB():
    print("\033[40m")

    userInput = int(input('please select from which DB you want to display: \n\t (1) items_michael \n\t (2) categorytotal_fruit \n\t (3) categorytotal_meat \n\t (4) categorytotal_snacks \n\t (5) categorytotal_vegetables \n\t (6) categorytotal_dairy \n Please Eneter int(: -- >> '))
    tables = ['CategoryTotal_Dairy', 'CategoryTotal_Fruit', 'CategoryTotal_Meat', 'CategoryTotal_Snacks', 'CategoryTotal_Vegetables']
    if userInput == 1:
       cursor.execute('select * from Items_Michael')
    elif userInput == 2:
        table = tables[1]
    elif userInput == 3:
        table = tables[2]
    elif userInput == 4:
        table = tables[3]
    elif userInput == 5:
        table = tables[4]
    elif userInput == 6: 
        table = tables[0]
    else:
        print('Invalid input')
        # optionally, you can exit the program here or prompt the user to try again
    
    if userInput > 1:
        cursor.execute(f"SELECT * FROM {table}")
        results = cursor.fetchall()

        MySQL_table = PrettyTable()
        MySQL_table.field_names = [i[0] for i in cursor.description]
        MySQL_table.add_rows(results)

        print(f"Table Name: {table}")
        print(MySQL_table)
        print('\n')
        return None #exiting function 
    else: 
        pass #voiding 


    # create a prettytable object with the column names
    table = PrettyTable(['ID', 'Name', 'Description', 'item_cost'])

    # fetch all rows from the result set before executing another SQL statement
    rows = cursor.fetchall()

    # add the rows to the table
    try: 
        #   -- “CategoryTotal_Fruit”, “CategoryTotal_Meat”, “CategoryTotal_Snacks”, and “CategoryTotal_Vegetables”
        for row in rows:
            table.add_row([row[0], row[1], row[2], row[3]])
    except Exception as e:
         print(e)
    print(table) #printing all the items 
    print("Opertation Complete")

   
class Items: #testing the items bein gput in a class
    def __init__(self, iid, name, category, item_cost) -> None:
          super().__init__()
          self.iid = iid
          self.name = name
          self.category = category
          self.item_cost = item_cost 

    def returnValue(self):
        print(f"{self.iid}{self.name}{self.category}{self.item_cost}")



def checkout():

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Get the item IDs from the user
    item_ids = input("Enter the IDs of the items you want to purchase (comma-separated): ")

    # Split the item IDs and convert them to integers
    item_ids = [int(id) for id in item_ids.split(",")]
    print(item_ids)

    # Fetch the items from the database using their IDs
    items = [] #creating null list 
    for item_id in item_ids:
        cursor.execute("SELECT * FROM items_michael WHERE iid = %s", (item_id,))
        item = cursor.fetchone() #retrieving the value from cursor then creating list 
        item = list(item)
        #print(f"Item as List : {item} ") #debugging 
        item[0] = int(item[0]) #turning item ID into a int not a str 
        item[3] = float(item[3]) # turning item cost into a float
        item[1] = str(item[1])
        item[2] = str(item[2]) #turing bot into str to get rid of extra quotes... 
        print(item[2], item[1])#debugging 
        if item:
            print("IF ITEM ---") #placer 
            items.append(item)
            print(item) #printing item ... 

    # Calculate the total cost of the items
    total_cost = 0
    category_totals = {}
    for item in items:
        quantity = int(input(f"Enter the quantity of {item[1]} you want to purchase: "))
        item_cost = quantity * float(item[3])
        total_cost += item_cost
        category = str(item[2])
        print(f'Category: {category} || item_cost: {item_cost}') #debugging purposes 
        category_total = category_totals.get(category, 0)
        category_total += item_cost
        category_totals[category] = category_total

        if category == "'Dairy'":
            cursor.execute(f"UPDATE CategoryTotal_Dairy SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
            print(f"UPDATE CategoryTotal_Dairy SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
        elif category == "'Fruit'":
            cursor.execute(f"UPDATE CategoryTotal_Fruit SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
            print(f"UPDATE CategoryTotal_Fruit SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
        elif category == "'Meat'":
            cursor.execute(f"UPDATE CategoryTotal_Meat SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
            print(f"UPDATE CategoryTotal_Meat SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
        elif category == "'Snacks'":
            cursor.execute(f"UPDATE CategoryTotal_Snacks SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
            print(f"UPDATE CategoryTotal_Snacks SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
        elif category == "'Vegetables'":
            cursor.execute(f"UPDATE CategoryTotal_Vegetables SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
            print(f"UPDATE CategoryTotal_Vegetables SET Amount = Amount + {item_cost} WHERE ItemID = {item_id}")
        else: 
            print(f"Invalid Category {category}... ") #error msg 
        db.commit()
    # Display the total cost and category totals
    print(f"Total cost: ${total_cost}")
    for category, category_total in category_totals.items():
        print(f"{category} total: ${category_total}")

def req8():
    tranactions = readerD("Transactions")
    items = readerD("Items_Michael")
    dict_item = {}
    
    for d in items:
        key = int(d[0])
        value = d[3]
        name = d[1]
        dict_item[key] = [value, name]

    for d in tranactions:
        itemID = d[1]
        quantity = d[2]
        val = dict_item.get(itemID)
        if val is None:
            print(f"No item found for itemID {itemID}")
            continue
        price = float(val[0])
        name = val[1]
        amount = quantity * price
        if quantity >= 3:
            print(f"iid = {itemID}\tname = {name}\tquantity = {quantity}\ttotal price = {amount}")


def customQuery():
    try:
        print("--+ Please enter in the Query Below +--") #enter msg 
        sqlStatement = input("Enter SQL Query -->> ") #getting input 
        cursor.execute(sqlStatement)
        results = cursor.fetchall()

        MySQL_table = PrettyTable()
        MySQL_table.field_names = [i[0] for i in cursor.description]
        MySQL_table.add_rows(results)

        print(f"--+ MySQL OUTPUT +--") #out msg 
        print(MySQL_table)
        print('\n')
    except Exception as E: 
        print(E)
    print("Operation Complete! ") #end msg 



def menu(): #user menu 
      #global db  # creating 
      #global cursor # creating global varibles
      #insertTable()
      while True:
        print("\033[1;32;40m")  # set text color to green
        print("***** Welcome to MySQL Database *****")
        print("\033[1;33;40m")  # set text color to yellow
        print("Please select an option:")
        print("1. Connect to Database [ALREADY ESTABLISHED]")
        print("2. Display All Records")
        print("3. Insert a New Record")
        print("4. Delete a Record")
        print("5. Checkout")
        print("6. Custom Query")
        print("7. total cost of all Transactions")
        print("8. quanity greter then 3")
        print("0. Exit")

        choice = input("Enter your choice: ")
        print("\033[0;37;40m")  # reset text color to white

        if choice == '1':
            db = create_connection()
        elif choice == '2':
            print("---+ REQUIREMENT 6 +---")
            selectDB()
            stamp()
        elif choice == '3':
            print(" ---+ REQUIRMENT 3 +---")
            insertTable()
            stamp()
        elif choice == '4':
            print("---+ DELETEING RECORDS +---")
            deleteRecord()
            stamp()
        elif choice == '5':
            print("---+ REQUIREMENT 5 +---")
            checkout() 
            stamp() 
        elif choice == '6':
            print("---+ REQUIREMENT 9 +---")
            customQuery()
            stamp() 
        elif choice == '7': 
            print("---+ REQUIREMENT 7 +---")
            Tranactions_rep7()
            stamp()
        elif choice == '8':
            print("---+ REQUIREMENT 8 +---")
            req8()
            stamp()
        elif choice == '0':
            db.close()# Close the database connection
            print("Thank you for using MySQL Database. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n") 

def transactionLookUp(): #look up for transactions 

    pass
     
def deleteRecord(): 
    table_name = input("please enter a table name: ")
    id = input("Please enter iid: ")
    deleteQuery = f"DELETE FROM {table_name} WHERE id = {id}" #delet edurory var
    try: 
        cursor.execute(deleteQuery) #deleteing query being executed in cursor 
    except Exception as E: 
        print(E)
    print("Record Removed.")

def Tranactions():
    with open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Transactions.txt", "r") as f:
        transaction_list = [line.strip() for line in f.readlines()] #comprenshion for my value in my list 
        for line in f:
            line = line.strip()
            values = line.split()
            values = [int(v) for v in values]
            transaction_list.append(values)
        print(transaction_list)
        for i in range(len(transaction_list)):
            print(transaction_list[i])



def Tranactions_rep7():
    cursor = db.cursor() # creating cursor to execute SQL queries 

    with open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Transactions.txt", "r") as f:
        transaction_list = [line.strip().replace(" ", "") for line in f.readlines()]
        for line in f:
            line = line.strip().replace(" ", "")
            values = line.split()
            values = [int(v) for v in values]
            transaction_list.append(values)
        print("Requirment 6")
        cursor = db.cursor() # creating cursor to execute SQL queries 
        dictDB = {} #null dict 
        quanity3 = list() #null list 
        total_price = 0
        for i in range(len(transaction_list)):
                
                if i == 0 or i == 1:
                    pass
                else:
                    Transaction_id = int(transaction_list[i][0])
                    iid = int(transaction_list[i][1])
                    quanity = int(transaction_list[i][2])
                    dictDB[Transaction_id] = [iid, quanity]  #creating my DIct 
                    #cursor.execute(f"INSERT INTO transactions (tid, iid, quantity) VALUES ({Transaction_id}, {iid}, {quanity})")
                    #db.commit()
                    cursor.execute(f"select * from items_michael where iid = {iid};")
                    price = cursor.fetchall()
                # print(price)
                    price[0] = float(price[0][0])
                    total_price += price[0] #adding price 

                    
        print(f"Total Price for all transactions: {total_price}" ) #total price 

def requirement_8():
     
     data_t =  open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Transactions.txt", "r")
     data_i =  open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\items_michael.txt", "r")
     dict_item = {}
     
     for d in data_i:
        key = d[0]
        value = d[3]
        name = d[1]
        dict_item[key] = [value, name]

     for d in data_t:
        itemID = d[1]
        quantity = d[2]
        val = dict_item.get(itemID)
        price = val[0]
        name = val[1]
        amount = quantity*price
        if quantity >= 3:
             print(f"iid = {itemID}\tname = {name}\tquantity = {quantity}\ttotal price = {amount}")

if __name__ == '__main__':
    print("\033[40m")
    db = create_connection() #establishing connection with MySQL data BASE! 
    cursor = db.cursor() # creating cursor to execute SQL queries 
    menu()
    stamp()
                        
                




   