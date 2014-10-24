from django.test import TestCase
from models import Post

# Create your tests here.
class  PostTest (object):
	# automatically created by Sublime Text 3
	"""unit testing"""
	def __init__(self, arg):
		super( PostTest , self).__init__()
		self.arg = arg

	# this is the actual test function for you test class
	def test_str(self):
		my_title = Post(title='This is basic title for  basic test case')
		self.assertEquals(
			str(my_title), 'This is basic title for  basic test case'
			)

