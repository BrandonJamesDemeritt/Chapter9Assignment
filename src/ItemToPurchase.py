'''
Created on Nov 10, 2022

@author: Brandon Demeritt
'''

class ItemToPurchase:
    '''Build the ItemToPurchase class with the following specifications:

        Attributes
        item_name (string)
        item_price (float)
        item_quantity (int)
        Default constructor
        Initializes item's name = "none", item's price = 0, item's quantity = 0
        Method
        print_item_cost() 
        
        Extend the ItemToPurchase class to contain a new attribute.

        item_description (string) - Set to "none" in default constructor
        Implement the following method for the ItemToPurchase class.

        print_item_description() - Prints item_description attribute for an ItemToPurchase object. Has an ItemToPurchase parameter.
        '''
    
    
    def __init__(self, itemName, itemDescription, itemPrice, itemAmount):
        self.itemName = None
        self.itemDescription = None
        self.itemPrice = 0.0
        self.itemAmount = 0
        
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.itemPrice = itemPrice
        self.itemAmount = itemAmount
        
    def __str__(self):
        result = "Item name: " + str(self.itemName) +"\n" 
        result += "Item Description: " + str(self.itemDescription) + "\n"
        result += "Price of item: " + str(self.itemPrice) + "\n"
        result += "Amount of item: " + str(self.itemAmount) + "\n"
        return result
    
    def printItemCost(self):
        cost = str(self.itemName) + " cost: $" + str(self.itemPrice)
        return cost
    
    def printItemDescription(self):
        desc = str(self.itemName) +  " description: " + str(self.itemDescription)
        return desc
    
    
