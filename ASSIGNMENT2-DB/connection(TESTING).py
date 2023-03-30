#creating a seprate file to hide the root credintials 
from abc import ABC 
import mysql
import hashlib #testing purposes 
class RootUser(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__userName = 'root'
        self.__passwd = '335834818' 

    def Connection(self): #
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="335834818"
        )#end of db 

#testing pass security 





