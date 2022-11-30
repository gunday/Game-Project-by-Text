from flask import render_template, redirect, url_for, flash, request
from forms import HeroStats, LoginForm
from flask_login import login_required, login_user
from models import User, Hero, Enemy
from FightingFantasy import app, db, login_manager
import battle


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user, form.remember_me.data)
            flash('Logged in successfully as {}.'.format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password.')
    return render_template('login.html', form=form)


@app.route('/encounter', methods=['GET', 'POST'])
@login_required
def encounter():
    form = HeroStats()
    if form.validate_on_submit():
        hstam = int(form.hstam.data)
        hskill = int(form.hskill.data)
        hluck = int(form.hluck.data)
        estam = int(form.estam.data)
        eskill = int(form.eskill.data)
        print load_user
        hstats = Hero(hstam=hstam, hskill=hskill, hluck=hluck, user_id=load_user)
        estats = Enemy(estam=estam, eskill=eskill, user_id=load_user)
        db.session.add(hstats)
        db.session.add(estats)
        db.session.commit()

        return redirect(url_for('fight'))
    return render_template('encounter.html', form=form)


@app.route('/fight')
def fight():
    flash("Let the battle begin!")

    battle.round(hstam, hskill, hluck, estam, eskill)
    return render_template('fight.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
