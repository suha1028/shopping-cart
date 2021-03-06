# shopping_cart.py
#worked with Patrick Lazzaro on project
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
import datetime

#customizing tax rate
import os
import dotenv

dotenv.load_dotenv()
TAX_RATE = os.getenv("TAX_RATE", default="0.0875")

#welcome message and input

print("-------------------------------")
print("Hello! Please continue to input product identifiers until you are done. When you are done, please type DONE.")
print("-------------------------------")

options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "DONE"]
total_price = 0
product_ids = []

while True: 
    grocery_item = input("Please input a product identifier (1-20 are valid): ")
    if grocery_item == "DONE":
        break
    elif grocery_item not in options:
        print("Are you sure the product identifier is correct? Please try again!")
    else:
        product_ids.append(grocery_item)


#receipt
print("-------------------------------")
print("GEORGETOWN GROCERY")
print("www.georgetowngrocery.com")
print("-------------------------------")
now = datetime.datetime.now()
print("CHECKOUT AT: " + str(now.strftime("%Y-%m-%d %I:%M %p")))
print("-------------------------------")

#total price of selected items
for grocery_item in product_ids:
     matching_products = [item for item in products if str(item["id"]) == str(grocery_item)]
     matching_product = matching_products[0]
     total_price = total_price + matching_product["price"]
     print(f"SELECTED PRODUCT: " + matching_product["name"] + " (" + str(to_usd(matching_product["price"])) + ")")

print("-------------------------------")
print(f"SUBTOTAL: " +str(to_usd(total_price))) 

tax_rate = (f'{TAX_RATE}')
tax = total_price * float(tax_rate)
print(f"TAX: " + str(to_usd(tax)))

final_number = total_price + tax
print(f"TOTAL: " + str(to_usd(final_number)))

#ending message
print("-------------------------------")
print("Thanks for shopping at Georgetown Grocery! See you again soon!")
print("-------------------------------")




   
    



