class Item:
    def __init__(self, name, description, category, buy_cost, sell_price, manufacturer, stock=0, sold_out=False, low_stock=False, id=None):
        self.name = name
        self.description = description
        self.category = category
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.manufacturer = manufacturer
        self.stock = stock
        self.sold_out = sold_out
        self.low_stock = low_stock
        self.id = id

    def check_has_low_stock(self):
        if self.stock <= 5:
            low_stock_result = True
        
        return low_stock_result

    def check_has_sold_out(self):
        sold_out_result = self.sold_out

        if self.stock > 0:
            sold_out_result = True

        return sold_out_result