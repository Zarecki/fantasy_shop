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
            self.low_stock = True

    def check_has_sold_out(self):
        if self.stock == 0:
            self.sold_out = True

    def stock_checks(self):
        self.check_has_low_stock()
        self.check_has_sold_out()