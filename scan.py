#!/usr/bin/env python3

import sys
from datetime import datetime
import sqlite3

db = sqlite3.connect('./bottles.sqlite3')

def add_measurement(code, weight):

	time = datetime.utcnow().isoformat()
	c = db.cursor()
	c.execute('INSERT INTO measurements VALUES (?,?,?)', (code, weight, time))
	db.commit()


def add_bottle(code, name, weight, full):

	if(full):
		full_weight = weight
	else:
		full_weight = -1

	c = db.cursor()
	c.execute('INSERT INTO bottles VALUES (?,?,?,?)', (code, name, full_weight, 1 if full else 0))
	db.commit()

	add_measurement(code, weight)


def remove_bottle(code):

	c = db.cursor()
	c.execute('UPDATE bottles SET empty=1 WHERE id=?', (code,))
	db.commit()


def scan_bottle():

	code = input('Bar code: ')
	if(code == ''):
		return False

	weight = input('Weight: ')
	if(weight == ''):
		return False

	try:
		weight = int(weight)
	except ValueError:
		print('Bad weight input!')
		return False

	print('\nWeight: {}\tBar code: {}\n'.format(weight, code))
	add_measurement(code, weight)

	return True


def new_bottle():

	code = input('Bar code: ')
	if(code == ''):
		return False

	name = input('Name: ')
	if(name == ''):
		return False

	weight = input('Weight: ')
	if(weight == ''):
		return False

	try:
		weight = int(weight)
	except ValueError:
		print('Bad weight input!')
		return False

	full = (input('Full bottle (Y/N): ').upper() == 'Y')
	if(code == ''):
		return False

	print('\nNew bottle: Bar code: {}\tName: {}\tWeight: {}\t {}\n'.format(code, name, weight, 'Full' if full else 'Not full'))
	add_bottle(code, name, weight, full)

	return True


def empty_bottle():

	code = input('Bar code: ')
	if(code == ''):
		return False

	remove_bottle(code)

	return True


def menu():

	print('(s)can / (n)ew / (e)mpty / (q)uit')
	cmd = input('Action: ').upper()

	if(cmd == 'S' or cmd == 'SCAN'):
		while True:
			if(not scan_bottle()):
				break
		return

	if(cmd == 'N' or cmd == 'NEW'):
		new_bottle()

	if(cmd == 'E' or cmd == 'EMPTY'):
		empty_bottle()

	if(cmd == 'Q' or cmd == 'QUIT'):
		sys.exit()


if(__name__ == '__main__'):
	while True:
		menu()
