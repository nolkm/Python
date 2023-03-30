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



## END OF IMPORTS! 


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
        try:
            with open(r"C:\Users\micha\OneDrive\Desktop\Year 1 Sem 2 Python\ASSIGNMENT2-DB\Items_YourFirstName.csv", 'r') as C:
                csv_data = csv.reader(C)
                i = 0 #creating a counter 
                print(csv_data)
                
                for row in csv_data: 
                    if i == 0:
                        print('HEADERS SKIPPED') #SKIPPING THE HEADERS 
                    else:
                        rowT = tuple(row) # taking each row from list a tuple 
                        print(rowT)
                        cursor.execute('INSERT INTO Items_MICHAEL(iid, name, category, price) VALUES("%s", "%s", "%s", "%s")', rowT)  
                    i += 1 #adding 1 to my counter 
            print("Data Inserted Complete!") # completion message 
            db.commit() #commiting of the data 
        except Exception: 
            print("Data Was Already Inserted!") #error Handling...
        
            print("Operation Complete!") #end of operation 
        

def createTABLE():
        create_query = ''' CREATE TABLE Items_MICHAEL(
        iid VARCHAR(255) NOT NULL, 
        name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL, 
        price VARCHAR(255) NOT NULL,
        PRIMARY KEY (iid))''' #SQL QUERY for creating my table 
        try:
            cursor.execute(create_query)
            print('Table Created Successfully! ')
        except Exception:
            print(' Table Already Exists! ')
    
        print("Operation Complete!") #end of operation 
        #self.cursor.execute('SELECT * FROM item_michael') #selecting values from table  
        db.commit() #commiting of the data  

def resetDB(self):
        try: 
            self.cursor.execute('DROP TABLE MyStore') #command to Drop The Table 
        except Exception as E: 
            print(E)
        print("Operation Complete!") #end of operation 

        db.commit() #commiting of the data  
    
def connectionClose():
        db.close()

def selectDB():
        cursor.execute('SELECT * FROM Items_MICHAEL') #selecting values from table  
        for line in cursor: 
             print(line)

class Items: #testing the items bein gput in a class
    def __init__(self, iid, name, category, price) -> None:
          super().__init__()
          self.iid = iid
          self.name = name
          self.category = category
          self.price = price 

    def returnValue(self):
        print(f"{self.iid}{self.name}{self.category}{self.price}")

if __name__ == '__main__':
    db = create_connection()
    cursor = db.cursor()
   
                        
                




   