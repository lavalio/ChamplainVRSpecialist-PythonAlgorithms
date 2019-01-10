#Python Lab
#Creating a Basic Order System using Object Oriented Techniques
# Group Nian & Ka Yan


import datetime
from item_class_v2 import Item

class Order:

    """here defined an Order class"""

    last_serial_used = 0

    def __init__(self):
        self.__item_list = []
        self.__purchase_date=datetime.datetime.now()
        self.__order_number = Order.last_serial_used + 1
        Order.last_serial_used = self.__order_number

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
        dash = '-' * (width+10)
        order_no ="{:06d}".format(self.__order_number)
        print("{} {:>24}".format("Order Number :", order_no) )
        #print("Item Number : {:>10}".format(self.get_item_count()))
        dtime = '{:%Y-%m-%d %I:%M %p}'.format(self.__purchase_date)
        print("Order Date: {:>40}".format(dtime))
        print()
        print("{} {:>38} ".format('Item','Price'))
        print(dash)
        self.print_items(width)
        print(dash)
        print()

        #print Subtotal
        dots_line = "." * (width - len("Subtotal"))
        sub_total_price = "${:0.2f}".format(float(self.get_total_price()))
        #print("{} {} {:<5} ".format('Sutotal ', dots_line, sub_total_price))
        print('Sutotal ', dots_line, sub_total_price)

        #print Tax
        dots_line = "." * (width - len("Tax XST"))
        total_gst = "${:0.2f}".format(float(self.get_total_gst()))
        total_qst = "${:0.2f}".format(float(self.get_total_qst()))
        #print("Tax GST " + dots_line + total_gst)
        #print("Tax QST " + dots_line + total_qst)
        #print("{} {} {:<5} ".format('Tax GST ', dots_line, total_gst))
        print('Tax GST ', dots_line, total_gst)
        #print("{} {} {:<5} ".format('Tax QST ', dots_line, total_qst))
        print('Tax QST ', dots_line, total_qst)


        #print total price
        dots_line = "." * (width - len("Total"))
        total=self.get_total_price() + self.get_total_gst() + self.get_total_qst()
        total_price = "${:0.2f}".format(float(total))
        print('TOTAL ', dots_line, total_price)
