from order_class_v2 import Order
from item_class_v2 import Item

order = Order()

while True:

    item_sku = input("What is the item sku? >")
    item_name = input("What is the the name of the item? >")
    item_price = input("What is the the price of the item? >")

    if input("Is the item taxable(y/n)? >").lower() == "y":
        item_taxable = True
    else:
        item_taxable = False

    new_item = Item(item_sku, item_name, float(item_price), item_taxable)
    order.add_item(new_item)

    if input("Enter another Item (y/n)? >").lower() == "n":
        break

order.generate_receipt(30)