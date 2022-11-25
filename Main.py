from Menu1 import *
from Admin import *
# from RestaurantDatabases.Payment import *
def main():
    admin = Dashboard("Customer","Customer")
    # payment= MakePayment()
    admin.options()
    # payment.Pay()
if __name__ == "__main__":
    main()
    
else:
    print("Error")