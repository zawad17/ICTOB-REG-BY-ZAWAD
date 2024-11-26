import sys
from database import DBhelper


class Flipkart:
    
    def __init__(self):
        #connect to the database
        self.db = DBhelper()
        self.menu()
        
        
        
    def menu(self):
        
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Enter 3 to Exit
        """)
        
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
            
    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the E-Mail: ")
        number = input("Enter the phone number: ")
        birth = input("Enter the date of birth: ")
        division = input("Enter the division: ")
        district = input("Enter the district: ")
        thana = input("Enter the thana: ")
        village = input("Enter the village: ")
        
        response = self.db.register(name, email, number, birth, division, district, thana, village)
        
        if response:
            print("Registration Successfull.")
        else:
            print("Registration failed")
        self.menu()
        
        
    
obj = Flipkart()
           
            