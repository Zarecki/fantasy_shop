from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.item import Item

def save(manufacturer):
    sql = "INSERT INTO manufacturer (name, description, category) VALUES (%s, %s, %s)"
    values = [manufacturer.name, manufacturer.description, manufacturer.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for result in results:
        manufacturer = Manufacturer(result["name"], result["description"], result["category"], result["active"], result["id"])
        manufacturers.append(manufacturer)

    return manufacturers

def select(id):
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    manufacturer = Manufacturer(result["name"], result["description"], result["category"], result["active"], result["id"])
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, description, category, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.description, manufacturer.category, manufacturer.active, manufacturer.id]
    run_sql(sql, values)

def get_items_by_manufacturer(id):
    product_line = []

    sql = "SELECT items.* FROM items where items.manufacturer_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        item = Item(result["name"], result["description"], result["category"], result["buy_cost"], result["sell_price"], id, result["stock"], result["sold_out"], result["id"])
        product_line.append(item)

    return product_line