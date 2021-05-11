from flask_wtf import FlaskForm


class Atmosphere:
    def __init__(self, year, temp, sea_level):
        self.year = year
        self.temp = temp #degC
        self.sea_level = sea_level #mm

        # def change_co2(rate):
        #     self.co2 += 1.9 + rate * (2.1 - 1.9)

        def change_temp(rate):
            self.temp += 0.65 + rate * (1.06 - 0.65)

        def change_sea_level(rate):
            self.sea_level += 0.17 + rate * (0.21 - 0.17)

atmosphere = Atmosphere(year=2000, temp=20, sea_level=0)


class Country:
    def __init__(self, name, gdp_per_capita, top_ten_percent_income, co2_per_capita, research_percent_of_gdp, life_expectancy, forest_cover):
        self.name = name
        self.gdp_per_capita = gdp_per_capita
        self.top_ten_percent_income = top_ten_percent_income
        self.co2_per_capita = co2_per_capita
        self.research_percent_of_gdp = research_percent_of_gdp
        self.life_expectancy = life_expectancy
        self.forest_cover = forest_cover

high_income = Country(name='High Income Country',
    gdp_per_capita=25103.2939763839,
    top_ten_percent_income=30.3,
    co2_per_capita=12.0408134356504,
    research_percent_of_gdp=2.32099168635611,
    life_expectancy=77.4493442982228,
    forest_cover=28.8209633722527)

middle_income = Country(name='Middle Income Country',
    gdp_per_capita=1264.82625991548,
    top_ten_percent_income=27.6,
    co2_per_capita=2.27059183623629,
    research_percent_of_gdp=0.647034783513819,
    life_expectancy=66.4028734575064,
    forest_cover=35.0986223770974)

low_income = Country(name='Low Income Country',
    gdp_per_capita=333.726703204851,
    top_ten_percent_income=46.1,
    co2_per_capita=0.422933079579211,
    research_percent_of_gdp=0.465793724546331,
    life_expectancy=53.5784738045263,
    forest_cover=25.131670584925)

# usa = Country(name='USA',
#     gdp_per_capita=36334.9087770589,
#     top_ten_percent_income=30.3,
#     co2_per_capita=20.1787505069199,
#     research_percent_of_gdp=2.62879,
#     life_expectancy=76.6365853658537,
#     forest_cover=33.1301735880689)

# australia = Country(name='Australia',
#     gdp_per_capita=21679.2478424147,
#     top_ten_percent_income=25.1,
#     co2_per_capita=17.2006098261369,
#     research_percent_of_gdp=1.57558,
#     life_expectancy=79.2341463414634,
#     forest_cover=17.1581557606446)

# india = Country(name='India',
#     gdp_per_capita=443.31419339174,
#     top_ten_percent_income=29.1,
#     co2_per_capita=0.976601686435581,
#     research_percent_of_gdp=0.75699,
#     life_expectancy=62.505,
#     forest_cover=22.7334950003195)

# brazil = Country(name='Brazil',
#     gdp_per_capita=3749.75324996168,
#     top_ten_percent_income=46.1,
#     co2_per_capita=1.87644130676787,
#     research_percent_of_gdp=0.75699,
#     life_expectancy=70.116,
#     forest_cover=65.9343586013156)

# namibia = Country(name='Namibia',
#     gdp_per_capita=2136.44024281489,
#     top_ten_percent_income=54.8,
#     co2_per_capita=0.915436614098857,
#     research_percent_of_gdp=0.14165,
#     life_expectancy=52.192,
#     forest_cover=9.78887633762101)


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
