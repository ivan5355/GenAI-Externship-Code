# Step 1: Create the Inventory

# Start with an empty dictionary called inventory.
# Each key in the dictionary will represent an item name, and the value will be a tuple containing the quantity and price.

inventory = {}

# Step 2: Add, Remove, and Update Items

# Add functionality to:
# Add a new item to the inventory (e.g., "mango": (15, 3.0)).
# Remove an item from the inventory.
# Update the quantity or price of an existing item.

def add_item(item_name, quantity, price):
    if item_name  not in inventory:
        inventory[item_name] = (quantity, price)
        print(f"{item_name} added")
    else:
        print(f"{item_name} already in inventory")


def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]  
        print(f"{item_name} has been removed from inventory.")
    else:
        print(f"{item_name} is not in inventory.")

def update_item(item_name, quantity = None, price = None):
    
    if item_name in inventory:
        
        current_quantity, current_price = inventory[item_name]

        if quantity is not None:
            new_quantity = quantity
        else:
            new_quantity = current_quantity

        if price is not None:
            new_price = price
        else:
            new_price = current_price
        print(f"{item_name} uddated")
        inventory[item_name] =(new_quantity, new_price)
    else:
        print("f{item_name} is not in inventory")
        
add_item("mango", 15, 3.0)
print(inventory)

add_item("apple", 11,83.0)
print(inventory)

remove_item("apple")
print(inventory)
    
update_item("mango", price = 20)
print(inventory)
