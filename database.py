import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost", user = "root", password = "", database = " database_practice")
            
            self.mycursor = self.conn.cursor()  #capability to talk with database
        
        except:
            print("Some error occured.Could not connect to database.")
            sys.exit(0)
            
        else:
            print("Connected to Database")
            
            
    def register(self, name, email, number, birth, division, district, thana, village):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`Full Name`, `E-Mail`, `Phone Number`, `Date Of Birth yy-mm-dd`, `Division`, `District`, `Thana`, `Village`, `Id`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', NULL);""".format(name, email, number, birth, division, district, thana, village))
            self.conn.commit()
        except:
            return -1
        else :
            return 1
        
        
        