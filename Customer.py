from Admin import*
from Menu1 import *

# Customer class and this class inherits from the Drinks and Food class
class Customer(Drinks,Food):
    def __init__(self):
        self.drink = Drinks()
        self.food = Food()
        self.take = 0
        self.apply = 0
    # This method is used to get the choice of the customer  
    def choice(self):
        print("Select the type of service you want")
        # Using tabulate to display the menu
        print(tabulate([['1', 'Food'], ['2', 'Drinks']], headers=['S/N', 'Service']))
        self.take = int(input())
        # This is used to check if the customer wants to order food or drink
        if self.take == 1:
            print(self.food.Menu())
            self.apply = int(input("Enter your choice : "))
            self.food.choice(self.apply)
            
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more food?,or get a drink (y/n) : ")
            if next == 'y':
                self.choice()
        # This is used to check if the customer wants to order drink  
        elif self.take == 2:
            # This is used to display the menu of the drinks
            print(self.drink.Menu())
            # This is used to get the choice of the customer
            self.apply = int(input("Enter your choice : "))
            self.drink.choice(self.apply)
              
            # This is used to check if the customer wants to order more food or drink
            next = input("Do you want to order more drinks?,or get food (y/n) : ")
            if next == 'y':
                self.choice()
        # This method is used to return the Total amount of the customer request
    def Amount(self):
        return self.food.getTotal() + self.drink.getTotal()
    
    
    #This method is used to get the number of people on a table
    def Tables(self):
        summation = 0
        storage = []
        customer = Customer()
        number = int(input("Enter the number of people on the table : "))
        for i in range(number):
            print("Customer ",i+1)
            customer.choice()
            #print("Total amount for customer ",i+1," is ",customer.Amount())
            storage.append(customer.Amount())
            length = len(storage)
            for i in range(length):
                summation+=storage[i]
            print("*"*50)
            print ("Total amount to be paid is : ",summation)
            print("*"*50)
        print("Thank you for choosing us")
 