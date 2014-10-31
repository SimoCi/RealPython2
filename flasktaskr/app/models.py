# models.py


from views import db

# make class Task that is a db.Model obj, it defines the tasks table
class Task(db.Model):

	__tablename__ = "tasks"

	# task_id auto-increments
	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.String, nullable=False)
	priority = db.Column(db.Integer, nullable=False)
	status = db.Column(db.Integer)

def __init__(self, name, due_date, priority, status):
	self.name = name
	self.due_date = due_date
	self.priority = priority
	self.status = status

def __repr__(self):
	return '<name %r>' % (self.body)