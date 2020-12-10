Thank you for downloading the Fantasy Shop inventory simulator!

In order to use this app you will need to make sure that you have downloaded and installed the following:
    Python3
    Flask
    PsycoPG2
    PostgreSQL

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------


In order to run this file:
    In Terminal -
        "createdb fantasy_shop",
        "psql -d fantasy_shop -f fantasy_shop.sql",
        "python3 console.py" (if you would like to seed the database with example data),
        copy and paste "FLASK_APP=app.py FLANK_ENV=development" into a file named "flaskenv" within the app folder,
        "flask run"

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

This app was created from the brief:
    Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

For which the MVP was:
    * The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
    * The inventory should track manufacturers, including a name and any other appropriate details.
    * The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
    * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
    * Show an inventory page, listing all the details for all the products in stock in a single view.
    * As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Extra notable features of this app:
