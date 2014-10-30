from django.db import models
# from PIL import Image

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	# adding three new fields
	tag = models.CharField(max_length=20, blank=True, null=True)
	image = models.ImageField(upload_to="images",blank=True, null=True)
	views = models.IntegerField(default=0)
	# this is not covered by the RP tutorial, just to be able to switch
	# between friendly urls and post slugs /blog/post/{{ post.slug }}
	# remember to update /blog/urls.py in this case
	# slug = models.CharField(max_length=100, unique=True)

	# customizing the models
	def __unicode__(self):
		# return self.title
		return str(self.id) + " / " + str(self.created_at) + " / " +\
			self.title + " / " + self.content + "\n" 