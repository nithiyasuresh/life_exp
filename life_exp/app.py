# import necessary libraries
import os
from flask import Flask, render_template, jsonify, request, redirect

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


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/countries")
def life():
    life_data = db.session.query(Life.Country, Life.Year, Life.Status, Life.Life_Expectancy,Life.Adult_Mortality, Life.Infant_Deaths, Life.Alcohol, Life.Percentage_Expenditure, Life.Hepatitis_B, Life.Measles, Life.BMI, Life.underfive_deaths, Life.Polio, Life.Total_expenditure, Life.Diphtheria, Life.Hiv_AIDS, Life.GDP, Life.Population, Life.thinness_1To19years, Life.thinness_5To9years, Life.Income_composition_of_resources, Life.Schooling, Life.region, Life.sub_region).all()
    return jsonify(life_data)


if __name__ == "__main__":
    app.run(debug=True)





# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["petName"]
#         lat = request.form["petLat"]
#         lon = request.form["petLon"]

#         pet = Pet(name=name, lat=lat, lon=lon)
#         db.session.add(pet)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("form.html")


# @app.route('/api/countries', methods=["GET"])
# def get_all_countries():
#     countries = get_all()
#     return jsonify(countries)



    # Country = db.Column(db.Float)
    # Year = db.Column(db.Integer)
    # Status = db.Column(db.Float)
    # Life_Expectancy = db.Column(db.Float)
    # Adult_Mortality = db.Column(db.Float)
    # Infant_Deaths = db.Column(db.Float)
    # Alcohol = db.Column(db.Float)
    # Percentage_Expenditure = db.Column(db.Float)
    # Hepatitis_B = db.Column(db.Float)
    # Measles = db.Column(db.Float)
    # BMI = db.Column(db.Float)
    # underfive_deaths = db.Column(db.Float)
    # Polio = db.Column(db.Float)
    # Total_expenditure = db.Column(db.Float)
    # Diphtheria = db.Column(db.Float)
    # Hiv_AIDS = db.Column(db.Float)
    # GDP = db.Column(db.Float)
    # Population = db.Column(db.Float)
    # thinness_1To19years = db.Column(db.Float)
    # thinness_5To9years = db.Column(db.Float)
    # Income_composition_of_resources = db.Column(db.Float)
    # Schooling = db.Column(db.Float)
    # region = db.Column(db.Float)
    # sub_region = db.Column(db.Float)
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