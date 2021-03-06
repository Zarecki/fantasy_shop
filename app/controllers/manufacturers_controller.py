from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import pdb

manufacturers_blueprint = Blueprint("manufacturers", __name__)

# INDEX
@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/index.html", manufacturers=manufacturers)

# SHOW
@manufacturers_blueprint.route("/manufacturers/<id>")
def show_manufacturer(id):
    items = manufacturer_repository.get_items_by_manufacturer(id)
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/show.html", items=items, manufacturer=manufacturer)

# NEW
@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/new.html", manufacturers=manufacturers)

# CREATE
@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    new_manufacturer = Manufacturer(name, description, category)
    new_manufacturer.activate()
    manufacturer_repository.save(new_manufacturer)
    return redirect("/manufacturers")

# EDIT
@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/edit.html", manufacturer=manufacturer)

# UPDATE
@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    active = request.form["active"]
    # pdb.set_trace()
    new_manufacturer = Manufacturer(name, description, category, active)
    if request.form["active"] == False:
        new_manufacturer.make_inactive()
    new_manufacturer.id = id
    manufacturer_repository.update(new_manufacturer)
    return redirect("/manufacturers")

# DELETE
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")

# GET ITEMS BY FILTER
@manufacturers_blueprint.route("/manufacturers/category", methods=["POST"])
def find_by_filter():
    form_data = request.form.to_dict()
    selected_filter = form_data["category"]
    manufacturers = manufacturer_repository.get_by_category(selected_filter)
    return render_template("/manufacturers/index.html", manufacturers=manufacturers)