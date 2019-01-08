from order_class_v2 import Order
from item_class_v2 import Item

item_list = [["1234","Bread",2.79,False],
             ["1235","Milk",4.99,False],
             ["1236","Chips",1.79,True],
             ["1237","Butter",11.09,True],
             ["1238","Potato", 2.29, True],
             ["1239","Chocola", 21.99, True]

             ]

order = Order()

for item in item_list:
    new_item = Item(item[0], item[1], item[2], item[3])
    order.add_item(new_item)

order.generate_receipt(30)

#Test remove
order.remove_item("1236")
order.generate_receipt(30)