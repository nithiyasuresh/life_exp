from .app import db


class Life(db.Model):
    __tablename__ = 'Life'

    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.Float)
    Year = db.Column(db.Integer)
    Status = db.Column(db.Float)
    Life_Expectancy = db.Column(db.Float)
    Adult_Mortality = db.Column(db.Float)
    Infant_Deaths = db.Column(db.Float)
    Alcohol = db.Column(db.Float)
    Percentage_Expenditure = db.Column(db.Float)
    Hepatitis_B = db.Column(db.Float)
    Measles = db.Column(db.Float)
    BMI = db.Column(db.Float)
    underfive_deaths = db.Column(db.Float)
    Polio = db.Column(db.Float)
    Total_expenditure = db.Column(db.Float)
    Diphtheria = db.Column(db.Float)
    Hiv_AIDS = db.Column(db.Float)
    GDP = db.Column(db.Float)
    Population = db.Column(db.Float)
    thinness_1To19years = db.Column(db.Float)
    thinness_5To9years = db.Column(db.Float)
    Income_composition_of_resources = db.Column(db.Float)
    Schooling = db.Column(db.Float)
    region = db.Column(db.Float)
    sub_region = db.Column(db.Float)

    def __repr__(self):
        return '<Life %r>' % (self.name)


class Life_2015(db.Model):
    __tablename__ = 'Life_2015'

    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.Float)
    Year = db.Column(db.Integer)
    Status = db.Column(db.Float)
    Life_Expectancy = db.Column(db.Float)
    Adult_Mortality = db.Column(db.Float)
    Infant_Deaths = db.Column(db.Float)
    Alcohol = db.Column(db.Float)
    Percentage_Expenditure = db.Column(db.Float)
    Hepatitis_B = db.Column(db.Float)
    Measles = db.Column(db.Float)
    BMI = db.Column(db.Float)
    underfive_deaths = db.Column(db.Float)
    Polio = db.Column(db.Float)
    Total_expenditure = db.Column(db.Float)
    Diphtheria = db.Column(db.Float)
    Hiv_AIDS = db.Column(db.Float)
    GDP = db.Column(db.Float)
    Population = db.Column(db.Float)
    thinness_1To19years = db.Column(db.Float)
    thinness_5To9years = db.Column(db.Float)
    Income_composition_of_resources = db.Column(db.Float)
    Schooling = db.Column(db.Float)
    region = db.Column(db.Float)
    sub_region = db.Column(db.Float)

    def __repr__(self):
        return '<Life_2015 %r>' % (self.name)

