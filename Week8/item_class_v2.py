#Python Lab
#Creating a Basic Order System using Object Oriented Techniques
# Group Nian & Ka Yan


class Item:
    """here defined a Item class"""

    def __init__(self,sku,name,price:float,taxable):
        self.__sku = sku
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    def is_taxable(self):
        if (self.__taxable == True):
            return True
        else:
            return False

    def taxable_letter(self):
        if (self.is_taxable()):
            return "T"
        else:
            return ""

    def get_sku(self):
        return self.__sku

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def calculate_gst(self):
        if (self.__taxable == True):
            return self.__price*0.05
        else:
            return 0

    def calculate_qst(self):
        if (self.__taxable == True):
            return self.__price*0.09975
        else:
            return 0

    def print_item(self,width):
        price = self.get_price()
        dots = "."*(width-len(self.get_name()))
        #price = "   ${:6.2f}".format(float(price))
        price = "${:0.2f}".format(price)
        #tax_c =  '{:>11}'.format(self.get_taxable_character())
        #item_line = self.name + " "+dot+price+tax_c
        #print(item_line)

        print(self.get_name(),dots,price,self.taxable_letter())