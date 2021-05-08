from flask_wtf import FlaskForm


class Atmosphere:
    def __init__(self, year, co2, temp, sea_level, forests):
        self.year = year
        self.co2 = co2 #ppm
        self.temp = temp #degC
        self.sea_level = sea_level #mm
        self.forests = forests

        def change_co2(rate):
            self.co2 += 1.9 + rate * (2.1 - 1.9)

        def change_temp(rate):
            self.temp += 0.65 + rate * (1.06 - 0.65)

        def change_sea_level(rate):
            self.sea_level += 0.17 + rate * (0.21 - 0.17)


class Government:
    def __init__(self, gdp, approval, happiness, tech):
        self.gdp = gdp
        self.approval = approval
        self.happiness = happiness
        self.tech = tech


class Economy:
    def __init__(self, manufacturing, agriculture, healthcare, research_economy):
        self.manufacturing = manufacturing
        self.agriculture = agriculture
        self.healthcare = healthcare
        self.research_economy = research_economy


class Mitigation:
    def __init__(self, renewable_energy, research_mitigation):
        self.renewable_energy = renewable_energy
        self.research_mitigation = research_mitigation


class Adaptation:
    def __init__(self, resilient_infrastructure, resilient_agriculture):
        self.resilient_infrastructure = resilient_infrastructure
        self.resilient_agriculture = resilient_agriculture


atmosphere = Atmosphere(year=1800, co2=300, temp=20, sea_level=0, forests=0)
usa = Government(gdp=1000, approval=0.8, happiness=0.7, tech=0.8)
brazil = Government(gdp=100, approval=0.4, happiness=0.6, tech=0.4)
namibia = Government(gdp=10, approval=0.2, happiness=0.5, tech=0.1)


# surface temp:
#     1800-2012: 0.65, 0.85, 1.06
#     1951-2012: 0.08, 0.12, 0.14
#     1998-2012: -0.05, 0.05, 0.15

# ocean temp (upper 75 meters):
#     1971-2012: 0.09, 0.11, 0.13

# sea level:
#     1901-2010: 0.17, 0.19, 0.21

# Level1: 1800-1900
# Level2: 1901-1951
# Level3: 1951-1970
# Level4: 1971-1997
# Level5: 1998-2012
