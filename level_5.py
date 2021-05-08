from flask_wtf import FlaskForm

class Atmosphere:
    def __init__(self, year, co2, temp, sea_level):
        self.year = year
        self.co2 = co2 #ppm
        self.temp = temp #degC
        self.sea_level = sea_level #mm

class Government:
    def __init__(self, gdp, health, happiness, tech):
        self.gdp = gdp
        self.health = health
        self.happiness = happiness
        self.tech = tech

atmosphere = Atmosphere(year=1998, co2=300, temp=20, sea_level=0)
government = Government(gdp=500, health=0.7, happiness=0.7, tech=0.7)
