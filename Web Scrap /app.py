from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mm

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# mongod in cmd line in MacOS
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission")


# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mission_data = mongo.db.mission_data.find_one()

    # Return template and data
    return render_template("index.html", mission_data=mission_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mission_data = mongo.db.mission_data

    # Run the scrape function
    mars_data = scrape_mm.all_data()

    # Update the Mongo database using update and upsert=True
    mongo.db.mission_data.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
