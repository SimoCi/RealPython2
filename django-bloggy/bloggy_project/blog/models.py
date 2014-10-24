from django.db import models

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.TextField()

	# customizing the models
	def __unicode__(self):
		# return self.title
		return str(self.id) + " / " + str(self.created_at) + " / " +\
			self.title + " / " + self.content + "\n" 