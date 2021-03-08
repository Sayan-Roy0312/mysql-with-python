from peewee import *;
import datetime
from collections import OrderedDict
#install pymsql 1st
db = MySQLDatabase("diary", host="localhost", port=3308,user="root",password="")


class Entry(Model):
	#content
	content = TextField()
	#timestamp
	timestamp = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db

def initialize():
	"""Create database and the table if they dont exist"""
	db.connect()
	db.create_tables([Entry], safe=True)


def menu_loop():
	"""Show the menu"""
	choice = None #initializing a var without a value

	while choice != 'q':
		print("Enter 'q' to exit the program.")
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__)) #value is going to be a function __doc__ print doc string for function
			choice = input('Action: ').lower().strip()

			if choice in menu:
				menu[choice]()

def add_entry():
	"""Add an entry"""

def view_entries():
	"""View previous entries"""

def delete_entry(entry):
	"""Delete an entry"""
menu = OrderedDict([
	('a', add_entry),
	('v', view_entries),

	])

if __name__ == '__main__':
	initialize()
	menu_loop()