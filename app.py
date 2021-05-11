from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from level_1 import atmosphere, low_income, middle_income, high_income


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


year = atmosphere.year
temp = atmosphere.temp
sea_level = atmosphere.sea_level


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/new_game', methods=['GET', 'POST'])
def new_game():

    # country_choices = ['USA', 'Australia', 'India', 'Brazil', 'Namibia']
    country_choices = ['Low Income', 'Middle Income', 'High Income']

    if request.method == 'POST':
        if request.form['country'] in country_choices:
            session['country'] = request.form['country']
            return redirect(url_for('level_1'))
        else:
            return render_template('new_game.html')

    elif request.method == 'GET':
        return render_template('new_game.html')


@app.route('/level_1', methods=['GET', 'POST'])
def level_1():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    return render_template('level_1.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        equality=top_ten_percent_income-1,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/investment', methods=['GET', 'POST'])
def investment():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['investment'] == 'manufacturing':
            pass
        if request.form['investment'] == 'agriculture':
            pass
        if request.form['investment'] == 'healthcare':
            pass
        if request.form['investment'] == 'research':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/mitigation', methods=['GET', 'POST'])
def mitigation():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['mitigation'] == 'renewable_energy':
            pass
        if request.form['mitigation'] == 'reforestation':
            pass
        if request.form['mitigation'] == 'research':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/adaptation', methods=['GET', 'POST'])
def adaptation():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['adaptation'] == 'resilient_infrastructure':
            pass
        if request.form['adaptation'] == 'climate_smart_agriculture':
            pass
        if request.form['adaptation'] == 'research':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/policy', methods=['GET', 'POST'])
def policy():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['policy'] == 'climate_white_paper':
            pass
        if request.form['policy'] == 'new_climate_bill':
            pass
        if request.form['policy'] == 'climate_policy_unit':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/diplomacy', methods=['GET', 'POST'])
def diplomacy():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['diplomacy'] == 'host_climate_conference':
            pass
        if request.method['diplomacy'] == 'contribute_to_climate_fund':
            pass
        if request.method['diplomacy'] == 'draft_climate_treaty':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/propaganda', methods=['GET', 'POST'])
def propaganda():

    country_instances = [low_income, middle_income, high_income]
    for country_instance in country_instances:
        if country_instance.name == session['country']:
            country = country_instance

    gdp_per_capita = country.gdp_per_capita
    top_ten_percent_income = country.top_ten_percent_income
    co2_per_capita = country.co2_per_capita
    research_percent_of_gdp = country.research_percent_of_gdp
    life_expectancy = country.life_expectancy
    forest_cover = country.forest_cover

    if request.method == 'POST':
        if request.form['propaganda'] == 'green_platform_to_campaign_for_government_control':
            pass
        if request.method['propaganda'] == 'trade_tariffs_on_foreign_goods_based_on_local_green_standards':
            pass
        if request.method['propaganda'] == 'insular_education_to_promote_local_climate_initiatives':
            pass

    elif request.method == 'GET':
        return render_template('investment.html',
        country=session['country'],
        year=atmosphere.year,
        gdp_per_capita=gdp_per_capita,
        top_ten_percent_income=top_ten_percent_income,
        research_percent_of_gdp=research_percent_of_gdp,
        life_expectancy=life_expectancy,
        co2='{:.1f}'.format(co2_per_capita),
        temp='{:.1f}'.format(atmosphere.temp),
        sea_level='{:.1f}'.format(atmosphere.sea_level),
        forest_cover='{:1f}'.format(forest_cover)
    )


@app.route('/how_to_play')
def how_to_play():
    return render_template('how_to_play.html')


@app.route('/about_climagotchi')
def about_climagotchi():
    return render_template('about_climagotchi.html')


@app.route('/about_climate_change')
def about_climate_change():
    return render_template('about_climate_change.html')


@app.route('/climate_change_evidence')
def climate_change_evidence():
    return render_template('climate_change_evidence.html')


@app.route('/climate_change_solutions')
def climate_change_solutions():
    return render_template('climate_change_solutions.html')


@app.route('/climate_finance')
def climate_finance():
    return render_template('climate_finance.html')


@app.route('/climate_finance_and_covid')
def climate_finance_and_covid():
    return render_template('climate_finance_and_covid.html')


if __name__ == '__main__':
    app.run()
