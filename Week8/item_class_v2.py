class Item:
    line_len =30

    def __init__(self,sku,name,price,taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def is_taxable(self):
        if (self.taxable == True):
            return True
        else:
            return False

    def get_price(self):
        return self.price

    def calculate_gst(self):
        if (self.taxable == True):
            return self.price*0.05
        else:
            return 0

    def calculate_qst(self):
        if (self.taxable == True):
            return self.price*0.09975
        else:
            return 0


    def print_item(self,width):
        price = self.get_price()
        dot = "."*(width-len(self.name))
        price = "   ${:6.2f}".format(float(price))
        tax =  '{:>11}'.format(str(self.taxable))
        item_line = self.name + " "+dot+price+tax
        print(item_line)