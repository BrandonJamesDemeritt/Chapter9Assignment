'''
Created on Nov 15, 2022

@author: Brandon Demeritt
'''
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase



def menu():
    '''(3) In main section of your code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart.

        Ex.

        Enter customer's name:
        John Doe
        Enter today's date:
        February 1, 2016

        Customer name: John Doe
        Today's date: February 1, 2016'''
    global cart
    menuOptions = ["a", "r", "c", "i", "o", "q"]
    choice = "a"
    while choice in menuOptions:
        print("\n a - Add item to cart\n r - Remove item from cart\n c - Change amount of item to buy\n i - Output item's descriptions \n o - Output shopping cart \n q - Quit")
        choice = input("\nPlease enter a choice:")
        if choice == "a":
            name = input("What is the item you wish to buy?")
            desc = input("What is the description of the item?")
            cost = input("What is the cost of the item?")
            amount = input("How many do you want to buy?")
            item = ItemToPurchase(name, desc, cost, amount)
            cart.addItem(item)
            print("\n" + str(amount) + " " + name + " @ $" + str(cost) + " each added to cart" )
        
        elif choice == "r":
            name = input("Please enter the name of the item you wish to remove: ")
            cart.removeItem(name)
            
        elif choice == "c":
            name = input("Please enter the name of the item you wish to modify: ")
            newAmount = input("What's the adjusted amount to buy?")
            cart.modifyItem(name, newAmount)
        
        elif choice == "i":
            cart.printDescription()
            
        elif choice == "o":
            cart.printCart()
            
        elif choice == "q":
            break
        
        else:
            print("Option not found, please try again.")
            menu()


def main():
    global cart
    cust = input("Please enter your name: ")
    date = input("Please enter the date: ")
    cart = ShoppingCart(cust, date)
    print("Customers Name : " + cust)
    print("Today's date: " + date)
    menu()

main()