class Item:
    def __init__(self, name, description, category, stock=0, buy_cost, sell_price, manufacturer, sold_out=False):
        self.name = name
        self.description = description
        self.category = category
        self.stock = stock
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.manufacturer = manufacturer
        self.sold_out = sold_out