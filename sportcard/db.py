from pymongo import MongoClient

from flask import Flask, current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        client = MongoClient()
        g.db = client.my_database
        g.db.players_collection = g.db.players
        current_app.config['DATABASE'] = 'players'
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
