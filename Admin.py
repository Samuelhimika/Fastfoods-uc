from Menu1 import *
from tabulate import tabulate
class Dashboard:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def options (self):
        #  Designing the admin menu
        print("*"*120)
        print("Welcome to fast food restaurant")   
        print("*"*120)   
        
    #    Using Tabulate to display the menu with Customer Login
        print(tabulate([['1', 'Customer Login'], ['2', 'Exit']], headers=['S/N', 'Options']))
       
        option=int(input("Enter your Option:"))
        
        if option == 1:
            print("Customer Login")
            self.username = input("Enter username: \n")
            self.password = input("Enter password: \n")
            if self.username == "customer" and self.password == "customer":
                # print("Welcome to our restaurant")
                print("Welcome our esteemed customer")
                customer = Customer()
                customer.Tables()
                print("Thank you for visiting us")
                exit()
            else:
                print("Invalid username or password")
                self.options()
      