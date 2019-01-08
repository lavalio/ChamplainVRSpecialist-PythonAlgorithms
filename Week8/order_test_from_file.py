from order_class_v2 import Order
from item_class_v2 import Item

# Convert string to list

def convert(string):
	li = list(string.strip().split(","))
	return li

def convert_bool(string):
    li=convert(string)
    if li[3] == "False":
        li[3] = False
    else:
        li[3] = True
    return li

order = Order()
filename = 'items.txt'
with open(filename) as file_object:
     for line in file_object:
         #print(line)
         item = convert_bool(line)
         #print(item)

         new_item = Item(item[0], item[1], float(item[2]), item[3])
         order.add_item(new_item)

order.generate_receipt(30)

#Test remove
#order.remove_item("1236")
#order.generate_receipt(30)
