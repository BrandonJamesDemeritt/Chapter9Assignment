'''
Created on Nov 15, 2022

@author: Brandon Demeritt
'''
from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, name, date):
        self.name = None
        self.date = "January 1, 2016"
        self.cartItems = []
        
        self.name = name
        self.date = date
        
    def __str__(self):
        result = "Customer name: " + str(self.name) + "\n"
        result += "Current date: " + str(self.date) + "\n"
        result += "Cart items: " + str(self.cartItems) + "\n"
        return result
    
    def addItem(self, ItemToPurchase):
        self.cartItems.append(ItemToPurchase)
        return
    
    def removeItem(self, itemToRemove):
        if self.cartItems:
            for item in self.cartItems:
                if itemToRemove == item.itemName:
                    self.cartItems.remove(item)
                    print("Item removed: " + str(item))
                    break
            else:
                print("Item not in cart. Nothing removed.")
        else:
            print("Nothing in cart.")

    def modifyItem(self, itemToModify, newAmount):
        for item in self.cartItems:
            if itemToModify == item.itemName:
                item.itemAmount = newAmount
                print(itemToModify + "amount changed to: " + str(newAmount))
                break
        else:
            print("Item not found, nothing changed.")
        
    def getNumItems(self):
        totalItems = 0
        for item in self.cartItems:
            totalItems += item.itemAmount
        
        return totalItems
            
    def getCost(self):
        totalCost = 0
        for x in self.cartItems:
            totalCost += float(x.itemPrice) * int(x.itemAmount)
        return totalCost
    
    def printDescription(self):
        print(self.name + "'s Shopping Cart - " + self.date + "\n")
        if self.cartItems:
            print("Item Descriptions: \n")
            for item in self.cartItems:
                print(item.printItemDescription())
        else:
            print("Cart is empty.")
        return
    
    def printCart(self):
        print("\n" + self.name + "'s Shopping Cart - " + self.date + "\n")
        if self.cartItems:
            for item in self.cartItems:
                print(str(item.itemAmount) + " " + item.printItemCost() + " each = " + "$" + str((float(item.itemPrice) * int(item.itemAmount))))
            print("\nTotal cost of all items in cart: $", self.getCost())
        else:
            print("Nothing found in cart")
        return
            