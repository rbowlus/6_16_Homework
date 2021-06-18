#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#THIS IS THE FINISHED ONE

from IPython.display import clear_output as co

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        print(f'{self.name}: ${self.price}')
        
    @staticmethod
    #A constant across the entire class
    def display_stock(all_stock):
        for stock in all_stock:
            Product.__repr__(stock)
        


class Trolley:
    def __init__(self):
        self.cart = []
    
    def add_item(self, item):
        found = False
        for y in self.cart:
            if y.name == item.name:
                found = True
                y.quantity += item.quantity
        if not found:
            self.cart.append(item)
        
    def remove_item(self, del_item, del_quantity):
        for x in self.cart:
            if del_item.lower() == x.name.lower():
                x.quantity -= del_quantity
                if x.quantity <= 0:
                    self.cart.remove(x)
                    break
                    
    def show_items(self):
        print('='*40)
        if not self.cart:
            print('You have no items in your cart.')
        else:
            print(self.cart)
        print('='*40)
        print(f"Total: ${sum([i.price * i.quantity for i in self.cart]):,.2f}")
             
               
        
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __repr__(self):
        return f'<Item: {self.name} [{self.quantity}] ${self.price:,.2f}>'
    
class ShoppingCart:
    @classmethod # <-- What is this?
    def show_instructions(self):
        print("""Type 'add' to add new product to your cart.
Type 'show' to list all products in your cart.
Type 'remove' if you want to remove an item from cart.
Type 'clear' if you would like to clear your cart.
Type 'quit' to exit the program.""")
    
    @classmethod
    def run(self):
        mango = Product("Mango", 1.99)
        apple = Product("Apple", 0.99)
        banana = Product("Banana", 0.79)
        peach = Product("Peach", 1.49)
        watermelon = Product("Watermelon", 4.99)
        dragonfruit = Product("Dragonfruit", 6.99)

        fruit_list = [mango, apple, banana, peach, watermelon, dragonfruit]
        
        done = False
        c = Trolley()

        while not done:

            ShoppingCart.show_instructions()
            choice = input('What is your choice? ').lower()
            co()

            if choice == 'add':
                print(f'Available Stock \n')
                Product.display_stock(fruit_list)
                item_name= input("Type in the product name.\n ").lower()
                item_quantity = int(input("Enter the quantity:\n"))
                
                found = False
                for obj in fruit_list:
                    if item_name == obj.name.lower():
                        found = True
                        c.add_item(Item(item_name, float(obj.price), item_quantity))
                 
                if not found:
                    print('We do not have that item.')
                
                c.show_items()

            elif choice == 'show': 
                c.show_items()
                input('Press any key continue')

            elif choice == 'remove':
                prod_del = input("Which item would you like removed? \n")
                quant_del = int(input("How many would you like removed? \n"))
                c.remove_item(prod_del, quant_del)
              
            elif choice == "clear":
                confirmation = input('Are you sure? Y/N?').lower()
                if confirmation =='y':
                    c.cart.clear()
                    input('Your items have been removed. Press any key to continue.')
            
            elif choice == 'quit':
                confirm = input('Are are you sure you want to quit? Y/N? ').lower()
                if confirm == 'y':
                    #print method with sum() function
                    c.show_items()
                    print('Have a good day!')
                    done = True
                elif confirm == 'n':
                    continue

ShoppingCart.run()


# In[ ]:





# In[ ]:




