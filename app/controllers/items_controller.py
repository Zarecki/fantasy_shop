from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from models.manufacturer import Manufacturer
import repositories.item_repository as item_repository
import repositories.manufacturer_repository as manufacturer_repository

item_blueprint = Blueprint("items", __name__)

# INDEX
@items_blueprint.route("/items")
def items():
    items = item_respository.select_all()
    return render_template("items/index.html", items=items)