#Python Lab
#Creating a Basic Order System using Object Oriented Techniques
# Group Nian & Ka Yan

from order_class_v2 import Order
from item_class_v2 import Item

# Convert a string to a list
def convert_to_list(string):
	li = list(string.strip().split(","))
	return li

#conver a string in the list to a boolean
def convert_bool(string):
    li=convert_to_list(string)
    if li[3] == "False":
        li[3] = False
    else:
        li[3] = True
    return li

def make_an_order():
    order = Order()
    filename = 'items.txt'
    with open(filename) as file_object:
        for line in file_object:
            item = convert_bool(line)
            new_item = Item(item[0], item[1], float(item[2]), item[3])
            order.add_item(new_item)
    order.generate_receipt(36)
    print()
    print()

i=0
while i<3:
    make_an_order()
    i+=1

