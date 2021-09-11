# import necessary libraries
import os
import sqlite3
from typing import Counter
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Life

#define database GET Requests
def get_db():
    conn = sqlite3.connect(Life)
    return conn

# def get_by_country(country):
#     db = get_db()
#     cursor = db.cursor()
#     statement = "SELECT * FROM country_data WHERE Country LIKE ?"
#     cursor.execute(statement, [country])
#     return cursor.fetchall()

def get_all():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM LIFE"
    cursor.execute(query)
    return cursor.fetchall()

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# define App routes to call GET Methods
@app.route('/countries', methods=["GET"])
def get_all_countries():
    countries = get_all()
    return jsonify(countries)


if __name__ == "__main__":
    app.run()





# Query the database and send the jsonified results
# @app.route("/send", methods=["GET"])
# def send():
#     if request.method == "GET":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         life = Life(Country, lat=lat, lon=lon)
#         db.session.add(life)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")

# @app.route("/api/pals")
# def pals():
#     results = db.session.query(Pet.name, Pet.lat, Pet.lon).all()

#     hover_text = [result[0] for result in results]
#     lat = [result[1] for result in results]
#     lon = [result[2] for result in results]

#     pet_data = [{
#         "type": "scattergeo",
#         "locationmode": "USA-states",
#         "lat": lat,
#         "lon": lon,
#         "text": hover_text,
#         "hoverinfo": "text",
#         "marker": {
#             "size": 15,
#             "line": {
#                 "color": "rgb(8,8,8)",
#                 "width": 1
#             },
#         }
#     }]

    # return jsonify(pet_data)
