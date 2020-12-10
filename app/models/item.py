class Item:
    def __init__(self, name, description, category, buy_cost, sell_price, manufacturer, stock=0, sold_out=False):
        self.name = name
        self.description = description
        self.category = category
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.manufacturer = manufacturer
        self.stock = stock
        self.sold_out = sold_out