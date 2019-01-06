import datetime


#from datetime import datetime

class Item:
    line_len =30

    def __init__(self,sku,name,price,taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def print_item(self):
        price = self.get_item_base_price()
        #print("{:10.2f}
        dot = "."*(self.line_len-len(self.name))
        price = "   ${:6.2f}".format(float(price))
        tax =  '{:>11}'.format(str(self.taxable))
        item_line = self.name + " "+dot+price+tax
        print(item_line)

    def get_item_base_price(self):
        return self.price

    def get_item_tax(self):
        if (self.taxable == True):
            gst = self.price*0.05
            qst = self.price*0.09975
            return gst+qst
        else:
            return 0

    def get_total(self):
        return self.get_item_base_price() + self.get_item_tax()


class Order:

    def __init__(self):

        self.__item_list = []

    def add_item(self, item: Item):

        self.__item_list.append(item)

    def remove_item(self, sku: int):

        for current_item in self.__item_list:

            if current_item.get_sku() == sku:

                self.__item_list.remove(current_item)
                return True

        return False

    def get_total_price(self):
        total_price =0
        for current_item in self.__item_list:
            total_price += current_item.get_item_base_price()
        return total_price

    # def get_date(self):
    #     date_to_print = ""
    #     date_to_print += x.strftime("%Y-%m-%d %I:%M")
    #     return date_to_print += x.strftime("%p").lower()
    #     #print(date_to_print)

    def print_order(self):
        dtime = '{:%Y-%m-%d %I:%M %p}'.format(datetime.datetime.now())
        #print('{:>16}'.format(str(dtime)))
        #print(dtime)

        print("Than you for your order {:>30}".format(dtime))
        print("Order summary:" )
        print()

        price = '{:>35}'.format('Price')
        tax =  '{:>16}'.format('Taxable')
        print("Item"+price+tax)

        for current_item in self.__item_list:
            current_item.print_item()

order = Order()
i=0
while i<=6:
    new_item = Item("1245", "wert", 12, True)
    order.add_item(new_item)
    i+=1
order.print_order()

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