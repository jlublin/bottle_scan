#!/usr/bin/env python3

import sys
import sqlite3

db = sqlite3.connect('./bottles.sqlite3')

c = db.cursor()

# TODO Should add type of liquid (table + id)
c.execute('CREATE TABLE bottles (id INTEGER, name TEXT, full_weight REAL, empty INTEGER)')
c.execute('CREATE TABLE measurements (id INTEGER, weight REAL, time TEXT)')

db.commit()
db.close()
