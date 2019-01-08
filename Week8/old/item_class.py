class Item:
    line_len =30

    def __init__(self,sku,name,price,taxable):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def print_item(self):
        item_line = self.name+"*"*(self.line_len-len(self.name))
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


item1 = Item(123,"pen",1.6,True)
item2 = Item(235,"pen",1.8,False)

print(item1.get_total())
item1.print_item()

print(item2.get_total())





