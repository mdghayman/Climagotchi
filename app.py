from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import (LoginManager, UserMixin, login_user, login_required,
        logout_user, current_user)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    return render_template('new_game.html')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('model'))
        response = 'Invalid username or password'
    return render_template('login.html', form=form, response=response)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    response = None
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
            method='sha256')
        new_user = User(username=form.username.data, email=form.email.data,
            password=hashed_password)
        if User.query.filter_by(username=new_user.username).first():
            response = 'Please enter a unique username.'
        elif User.query.filter_by(email=new_user.email).first():
            response = 'Please enter a unique email address.'
        else:
            db.session.add(new_user)
            db.session.commit()
            response = 'New user has been created!'
    return render_template('signup.html', form=form, response=response)

if __name__ == '__main__':
    app.run()
