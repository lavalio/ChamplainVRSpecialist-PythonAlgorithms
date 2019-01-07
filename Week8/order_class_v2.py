import datetime
from item_class_v2 import Item

class Order:

    last_serial_used = 0

    def __init__(self):

        self.__item_list = []
        self.order_number = Order.last_serial_used + 1
        Order.last_serial_used = self.order_number

    def add_item(self, item: Item):

        self.__item_list.append(item)

    def remove_item(self, sku: int):

        for current_item in self.__item_list:

            if current_item.get_sku() == sku:

                self.__item_list.remove(current_item)
                return True
        return False

    def get_item_count(self):
        return len(self.__item_list)

    def get_total_price(self):
        total_price =0
        for current_item in self.__item_list:
            total_price += current_item.get_price()
        return total_price

    def get_total_gst(self):
        gst = 0
        for current_item in self.__item_list:
            gst += current_item.calculate_gst()
        return gst

    def get_total_qst(self):
        qst = 0
        for current_item in self.__item_list:
            qst += current_item.calculate_qst()
        return qst

    def print_items(self,width):

        for current_item in self.__item_list:
            current_item.print_item(width)

    def generate_receipt(self,width):
        dash = '-' * 55
        print("Order Number : {:>10}".format(self.order_number))
        dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())
        print("Order Date: {:>40}".format(dtime))
        print()
        print("{} {:>34} {:>14} ".format('Item','Price','Taxable'))
        print(dash)
        self.print_items(width)
        print(dash)
        print()

        #print Subtotal
        dots_line = "." * (width - len("Subtotal"))
        sub_total_price = "   ${:6.2f}".format(float(self.get_total_price()))
        print("Sutotal " + dots_line + sub_total_price)

        #print Tax

        dots_line = "." * (width - len("Tax XST"))
        total_gst = "   ${:5.2f}".format(float(self.get_total_gst()))
        total_qst = "   ${:5.2f}".format(float(self.get_total_qst()))
        print("Tax GST " + dots_line + total_gst)
        print("Tax QST " + dots_line + total_qst)

        #print total price
        dots_line = "." * (width - len("Total"))
        total=self.get_total_price() + self.get_total_gst() + self.get_total_qst()
        total_price = "   ${:5.2f}".format(float(total))
        print("TOTAL " + dots_line + total_price)


#Test
order = Order()
i=0
price = 1
while i<=6:
    new_item = Item("1245", "wert", price, True)
    order.add_item(new_item)
    i+=1
    price+=2
order.generate_receipt(30)

#Menu
# while True:
#
#     item_sku = input("What is the item sku? >")
#     item_name = input("What is the the name of the item? >")
#     item_price = input("What is the the price of the item? >")
#     #item_taxable = input("Is the item taxable(y/n)? >")
#
#     if input("Is the item taxable(y/n)? >").lower() == "y":
#         item_taxable = True
#     else:
#         item_taxable = False
#
#     new_item = Item(item_sku, item_name, item_price, item_taxable)
#     order.add_item(new_item)
#
#     if input("Enter another(y/n)? >").lower() == "n":
#         break

#order.print_order()