"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-cgrq32o2qv2dcb92g6a0-a.oregon-postgres.render.com",
    database="todo_p1oe",
    user="todo_p1oe_user",
    password="KyMOWhl8A6CUsgNrO1l26JSYx4BYiWEv")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
