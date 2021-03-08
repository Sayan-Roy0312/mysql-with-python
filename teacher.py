from peewee import *;


db = MySQLDatabase('school', host='localhost', port =3308, user='root', password='')

class Teacher (Model):
	#username = TextField()
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		database = db
		# db_table='Teacher'

teachers = [{
	'username': 'johnd',
	'points':4542
}, {
	'username': 'grayu',
	'points': 6721
}, {
	'username': 'fattyw',
	'points': 9121
}, {
	'username': 'leop',
	'points': 1099
}]

def add_teacher():
	for teacher in teachers:
		try:
			Teacher.create(username=teacher['username'],
			points=teacher['points'])
		except IntegrityError:
			teacher_record = Teacher.get(username=teacher['username'])
			teacher_record.points = teacher['points']
			teacher_record.save()
def top_teacher():
	teacher = Teacher.select().order_by(Teacher.points.desc()).get() #only gets the 1st record
	return teacher;

if __name__ == '__main__':
	db.connect()
	db.create_tables([Teacher], safe=True)
	add_teacher()
	print("Our top teacher right now is {0.username}.".format(top_teacher()))