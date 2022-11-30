from datetime import datetime
from FightingFantasy import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    hero = db.relationship('Hero', backref='user', lazy='dynamic')
    enemy = db.relationship('Enemy', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hstam = db.Column(db.Integer, nullable=False)
    hskill = db.Column(db.Integer, nullable=False)
    hluck = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Hero stamina: %r, skill: %r, luck: %r>' % self.hstam, self.hskill, self.hluck


class Enemy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estam = db.Column(db.Integer, nullable=False)
    eskill = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Enemy stamina: %r, skill: %r, luck: %r>' % self.hstam, self.hskill, self.hluck
