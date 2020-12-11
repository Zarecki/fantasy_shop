from db.run_sql import run_sql

from models.item import Item
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(item):
    sql = "INSERT INTO items (name, description, category, buy_cost, sell_price, manufacturer_id, stock, sold_out) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = [item.name, item.description, item.category, item.buy_cost, item.sell_price, item.manufacturer.id, item.stock, item.sold_out]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id

def select_all():
    items = []
    
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for item in results:
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        item  = Item(result["name"], result["description"], result["category"], result["buy_cost"], result["sell_price"], manufacturer, result["stock"], result["sold_out"], result["id"])
        items.append(item)

    return items

