from flask import Flask, render_template

from controllers.items_controller import items_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint
from models.item import Item
from models.manufacturer import Manufacturer
import repositories.item_repository as item_repository
import repositories.manufacturer_repository as manufacturer_repository

app = Flask(__name__)

app.register_blueprint(items_blueprint)
app.register_blueprint(manufacturers_blueprint)

@app.route('/')
def home():
    items = item_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    number_of_items = len(items)
    number_of_manufacturers = len(manufacturers)
    total_items = sum(item.stock for item in items)
    projected_profit = (sum(item.sell_price for item in items) - sum(item.buy_cost for item in items))
    return render_template('index.html', number_of_items=number_of_items, number_of_manufacturers=number_of_manufacturers, total_items=total_items, projected_profit=projected_profit)

if __name__ == '__main__':
    app.run(debug=True)