from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from level_1 import atmosphere, usa, brazil, namibia


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    return render_template('new_game.html')


@app.route('/level_1', methods=['GET', 'POST'])
def level_1():

    year = atmosphere.year
    co2 = atmosphere.co2
    temp = atmosphere.temp
    sea_level = atmosphere.sea_level

    if request.method == 'POST':

        if request.form['emissions'] == 'decrease':
            atmosphere.year += 1
            atmosphere.co2 += 1.9
            atmosphere.temp += 0.65
            atmosphere.sea_level += 1.5
            return render_template('level_1.html',
                year=atmosphere.year,
                co2='{:.1f}'.format(atmosphere.co2),
                temp='{:.1f}'.format(atmosphere.temp),
                sea_level='{:.1f}'.format(atmosphere.sea_level),
                budget=usa.gdp,
                welfare=usa.happiness,
                approval=usa.approval,
                tech=usa.tech)

        if request.form['emissions'] == 'increase':
            atmosphere.year += 1
            atmosphere.co2 += 2.1
            atmosphere.temp += 1.06
            atmosphere.sea_level += 1.9
            return render_template('level_1.html',
                year=atmosphere.year,
                co2='{:.1f}'.format(atmosphere.co2),
                temp='{:.1f}'.format(atmosphere.temp),
                sea_level='{:.1f}'.format(atmosphere.sea_level),
                budget=usa.gdp,
                welfare=usa.happiness,
                approval=usa.approval,
                tech=usa.tech)

    elif request.method == 'GET':
        return render_template('level_1.html',
            year=atmosphere.year,
            co2='{:.1f}'.format(atmosphere.co2),
            temp='{:.1f}'.format(atmosphere.temp),
            sea_level='{:.1f}'.format(atmosphere.sea_level),
            budget=usa.gdp,
            welfare=usa.happiness,
            approval=usa.approval,
            tech=usa.tech)


@app.route('/level_2', methods=['GET', 'POST'])
def level_2():
    return render_template('2.html')


@app.route('/level_3', methods=['GET', 'POST'])
def level_3():
    return render_template('level_3.html')


@app.route('/level_4', methods=['GET', 'POST'])
def level_4():
    return render_template('level_4.html')


@app.route('/level_5', methods=['GET', 'POST'])
def level_5():
    return render_template('level_5.html')


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
