from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.manufacturer import Manufacturer
import repositories.item_repository as item_repository
import repositories.manufacturer_repository as manufacturer_repository

items_blueprint = Blueprint("items", __name__)

# INDEX
@items_blueprint.route("/items")
def items():
    items = item_respository.select_all()
    return render_template("items/index.html", items=items)

# SHOW
@items_blueprint.route("/items/<id>")
def show_item(id):
    item = item_repository.select(id)
    return render_template("items/show.html", item=item)

# NEW
@items_blueprint.route("/items", methods=["POST"])
def create_item():
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    buy_cost = request.form["buy_cost"]
    sell_price = request.form["sell_price"]
    manufacturer_id = request.form["manufacturer_id"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    stock = request.form["stock"]
    new_item = Item(name, description, category, buy_cost, sell_price, manufacturer, stock)
    item_repository.save(new_item)
    return redirect("/items")