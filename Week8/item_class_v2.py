class Item:
    line_len =30

    def __init__(self,sku,name,price:float,taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def is_taxable(self):
        if (self.taxable == True):
            return True
        else:
            return False

    def get_sku(self):
        return self.sku

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

    def get_taxable_character(self):
        if self.taxable==True:
            return "T"
        else:
            return "F"

    def print_item(self,width):
        price = self.get_price()
        dots = "."*(width-len(self.name))
        #price = "   ${:6.2f}".format(float(price))
        price = "   ${:6.2f}".format(price)
        #tax_c =  '{:>11}'.format(self.get_taxable_character())
        #item_line = self.name + " "+dot+price+tax_c
        #print(item_line)

        print("{} {} {} {:>5} ".format(self.name,dots,price,self.get_taxable_character()))