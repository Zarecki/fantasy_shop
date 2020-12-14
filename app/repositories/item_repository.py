from db.run_sql import run_sql

from models.item import Item
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(item):
    sql = "INSERT INTO items (name, description, category, buy_cost, sell_price, manufacturer_id, stock, sold_out) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [item.name, item.description, item.category, item.buy_cost, item.sell_price, item.manufacturer.id, item.stock, item.sold_out]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id
    return item

def select_all():
    items = []
    
    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for result in results:
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        item  = Item(result["name"], result["description"], result["category"], result["buy_cost"], result["sell_price"], manufacturer, result["stock"], result["sold_out"], result["id"])
        items.append(item)

    return items

def select(id):
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    manufacturer = manufacturer_repository.select(result[0][6])
    item  = Item(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], manufacturer, result[0][7], result[0][8], result[0][0])
    return item

def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)

def delete_item(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(item):
    sql = "UPDATE items SET (name, description, category, buy_cost, sell_price, manufacturer_id, stock, sold_out) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id  = %s"
    values = [item.name, item.description, item.category, item.buy_cost, item.sell_price, item.manufacturer_id, item.stock, item.sold_out, item.id]
    run_sql(sql, values)


